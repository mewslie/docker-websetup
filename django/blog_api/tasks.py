from __future__ import absolute_import, unicode_literals

from celery import shared_task

#task for testing
@shared_task
def add(x, y):
    return x + y