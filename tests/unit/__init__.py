# -*- coding: utf-8 -*-

import asyncio
import atexit
import os

from toxiccommon import common_setup, exchanges
from toxicpoller import create_settings

from tests import TEST_DATA_DIR

POLLER_DATA_PATH = TEST_DATA_DIR

os.environ['TOXICPOLLER_SETTINGS'] = os.path.join(
    POLLER_DATA_PATH, 'toxicpoller.conf')

create_settings()

from toxicpoller import settings  # noqa

loop = asyncio.get_event_loop()
loop.run_until_complete(common_setup(settings))

from toxiccommon.coordination import ToxicZKClient  # noqa: E402


def clean():
    if ToxicZKClient._zk_client:
        try:
            loop.run_until_complete(ToxicZKClient._zk_client.close())
        except Exception:
            pass

    try:
        loop.run_until_complete(exchanges.conn.disconnect())
    except Exception:
        pass


atexit.register(clean)
