from __future__ import absolute_import
from celery import shared_task
from celery.decorators import task
import time


@shared_task
def test(param):
	time.sleep(20)
	return 4444444


@task(name="sum_two_numbers")
def add(x, y):
    return x + y
