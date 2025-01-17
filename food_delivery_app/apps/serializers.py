import pytz

from rest_framework import serializers
from django.utils.timezone import localtime

from food_delivery_app.apps import constants as const


class BaseSerializer(serializers.ModelSerializer):
    def convert_utc_to_local_timezone(self, utc_datetime_obj, local_tz=const.TIME_ZONE):
        """Convert UTC datetime to the specified local timezone."""
        timezone = pytz.timezone(local_tz)
        localized_time = localtime(utc_datetime_obj, timezone)
        return localized_time.strftime(const.DATETIME_FORMAT_WITH_OFFSET)

    def to_representation(self, instance):
        """Customize the serialized representation."""
        representation = super().to_representation(instance)

        # Remove password if present in the response
        representation.pop("password", None)

        # Convert UTC to local timezone for specified fields
        for field in ["created_at", "updated_at"]:
            if hasattr(instance, field):
                utc_datetime_obj = getattr(instance, field)
                if utc_datetime_obj:
                    representation[field] = self.convert_utc_to_local_timezone(
                        utc_datetime_obj
                    )

        return representation
