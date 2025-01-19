from django.db import models
from food_delivery_app.apps.users import enums
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    role = models.CharField(
        max_length=30, choices=enums.Role.choices, default=enums.Role.CUSTOMER
    )
    gender = models.CharField(
        max_length=20,
        choices=enums.Gender.choices,
        default=enums.Gender.PREFER_NOT_TO_SAY,
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, default="")
    phone_number = models.CharField(max_length=15, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        db_table = "users"


class Address(models.Model):
    address_id = models.BigAutoField(primary_key=True)
    address_line_1 = models.TextField()
    address_line_2 = models.TextField(null=True, default="")
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "addresses"


# class Customer(models.Model):
#     customer_id = models.BigAutoField(primary_key=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="customers")
#     dob = models.DateField()
#     prefered_language = models.CharField(
#         max_length=15, choices=enums.Language.choices, default=enums.Language.ENGLISH
#     )
#     prefered_payment_method = models.CharField(
#         max_length=25,
#         choices=enums.PaymentMethod.choices,
#         default=enums.PaymentMethod.CASH_ON_DELIVERY,
#     )
#     total_spent = models.DecimalField(max_digits=10, decimal_places=2)
#     last_order_date = models.DateTimeField(null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         db_table = "customers"


# class UserAddress(models.Model):
#     """
#     Represents a user's address, linking a user to an address with an optional default setting
#     and an address type for categorization.
#     """

#     user_address_id = models.BigAutoField(primary_key=True)
#     customer_id = models.ForeignKey(
#         Customer, on_delete=models.CASCADE, related_name="user_addresses"
#     )
#     address_id = models.ForeignKey(
#         Address, on_delete=models.CASCADE, related_name="user_addresses"
#     )
#     is_default = models.BooleanField(default=False)
#     address_type = models.CharField(
#         max_length=10,
#         choices=enums.AddressType.choices,
#         default=enums.AddressType.HOME,
#     )

#     class Meta:
#         db_table = "user_addresses"
