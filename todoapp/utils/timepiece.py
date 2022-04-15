from datetime import datetime

from django.utils import timezone


def now():
    return timezone.localtime(timezone.now())


def today():
    return now().date()


def from_timestamp(timestamp):
    return datetime.fromtimestamp(float(timestamp), tz=timezone.utc)
