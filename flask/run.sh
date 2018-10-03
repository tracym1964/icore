#!/usr/bin/env bash

su -m guser -c "gunicorn -w 1 -b 0.0.0.0:8000 app:app --reload"