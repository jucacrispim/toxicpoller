#!/bin/bash

pylint toxicpoller/
if [ $? != "0" ]
then
    exit 1;
fi

flake8 toxicpoller/

if [ $? != "0" ]
then
    exit 1;
fi

flake8 tests
exit $?;
