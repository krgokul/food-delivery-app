# utils.py
from django.utils import timezone
import pytz
import constants as const


def convert_utc_to_timezone(utc_datetime, tz_name=const.TIME_ZONE):
    """
    Convert a UTC datetime to a specific timezone (default: local timezone).
    """
    # Ensure the passed datetime is timezone-aware
    if utc_datetime and utc_datetime.tzinfo is None:
        utc_datetime = timezone.make_aware(utc_datetime, timezone.utc)

    # If a specific timezone is provided, use it; otherwise, use the default local timezone
    if tz_name:
        target_timezone = pytz.timezone(tz_name)
    else:
        target_timezone = timezone.get_current_timezone()

    # Convert UTC to the target timezone
    return utc_datetime.astimezone(target_timezone)
