# -*- coding: utf-8 -*-

import os
import sys
from unittest import TestCase

from tests import TEST_DATA_DIR

PYVERSION = ''.join([str(n) for n in sys.version_info[:2]])
REPO_DIR = os.path.join(TEST_DATA_DIR, 'repo')
OTHER_REPO_DIR = os.path.join(TEST_DATA_DIR, 'fork-repo')
SLAVE_ROOT_DIR = TEST_DATA_DIR
SOURCE_DIR = os.path.join(TEST_DATA_DIR, '..')
TOXICPOLLER_CMD = os.path.join(SOURCE_DIR, 'toxicpoller', 'cmds.py')

toxicpoller_conf = os.environ.get('TOXICPOLLER_SETTINGS')
if not toxicpoller_conf:
    toxicpoller_conf = os.path.join(SLAVE_ROOT_DIR, 'toxicpoller.conf')
    os.environ['TOXICPOLLER_SETTINGS'] = toxicpoller_conf


class BaseFunctionalTest(TestCase):
    """An AsyncTestCase that a slave process on
    setUpClass and stops it on tearDownClass"""

    @classmethod
    def start_poller(cls):
        start_poller()

    @classmethod
    def stop_poller(cls):
        stop_poller()

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.start_poller()

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        cls.stop_poller()


def start_poller():
    """Starts an slave server in a new process for tests"""

    toxicpoller_conf = os.environ.get('TOXICPOLLER_SETTINGS')
    pidfile = 'toxicpoller{}.pid'.format(PYVERSION)
    cmd = ['export', 'PYTHONPATH="{}"'.format(SOURCE_DIR), '&&', 'python',
           TOXICPOLLER_CMD, 'start', SLAVE_ROOT_DIR, '--daemonize',
           '--pidfile', pidfile, '--loglevel', 'debug']

    if toxicpoller_conf:
        cmd += ['-c', toxicpoller_conf]

    os.system(' '.join(cmd))


def stop_poller():
    """Stops the test slave"""
    pidfile = 'toxicpoller{}.pid'.format(PYVERSION)
    cmd = ['export', 'PYTHONPATH="{}"'.format(SOURCE_DIR), '&&',
           'python', TOXICPOLLER_CMD, 'stop', SLAVE_ROOT_DIR,
           '--pidfile', pidfile, '--kill']

    os.system(' '.join(cmd))
