from django.contrib.auth.hashers import make_password
from food_delivery_app.apps import serializers
from food_delivery_app.apps import utils as cutils
from .models import User


class UserSerializer(cutils.DynamicPrefixMixin, serializers.BaseSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        password = validated_data.pop("password")
        hashed_password = make_password(password)
        user = User.objects.create(password=hashed_password, **validated_data)
        return user
