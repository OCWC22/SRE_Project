#!/bin/bash
gunicorn --bind 0.0.0.0:9001 app:app
