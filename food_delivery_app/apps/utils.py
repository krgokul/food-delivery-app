from rest_framework.response import Response
from rest_framework import status
from food_delivery_app import apps


class DynamicPrefixMixin:
    # Mapping model classes to prefsixes
    MODEL_PREFIX_MAP = {apps.users.models.User: "User"}

    def get_prefix(self, instance):
        """Determine the prefix based on the instance."""
        # Get the prefix using the model class, default to "item"
        return self.MODEL_PREFIX_MAP[type(instance)]

    def add_message(self, response, instance, action):
        """Add custom message with dynamic prefix for create/update actions."""
        prefix = self.get_prefix(instance)
        action_message = f"{prefix} Record {action} successfully."
        response.data["message"] = action_message
        return response

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return self.add_message(response, response.instance, "created")

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return self.add_message(response, response.instance, "updated")

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        prefix = self.get_prefix(instance)
        super().destroy(request, *args, **kwargs)
        return Response(
            {"message": f"{prefix} Record deleted successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )
