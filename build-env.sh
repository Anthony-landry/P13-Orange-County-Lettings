#!/usr/bin/env bash

set -xe

python -m venv venv
source venv/bin/activate
pip install --requirement requirements.txt