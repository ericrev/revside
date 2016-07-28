#!/bin/sh
celery -A frontend worker -l info
