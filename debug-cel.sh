#!/bin/sh
celery -A frontend worker -l info --concurrency=1 -P solo
