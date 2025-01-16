from django.db import models
from food_delivery_app.apps.users import enums


class User(models.Model):
    user_id = models.BigAutoField(primary_key=True)
    role = models.CharField(max_length=30, choices=enums.Role.choices)
    gender = models.CharField(
        max_length=20,
        choices=enums.Gender.choices,
        default=enums.Gender.PREFER_NOT_TO_SAY,
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, default="")
    email = models.EmailField(max_length=255, unique=True)
    password = models.TextField()
    phone_number = models.CharField(max_length=15, blank=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "users"


class Address(models.Model):
    address_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_addresses"
    )
    address_type = models.CharField(
        max_length=10, choices=enums.AddressType.choices, default=enums.AddressType.HOME
    )
    address_line_1 = models.TextField()
    address_line_2 = models.TextField(null=True, default="")
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=20)
    is_default = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "addresses"


class Customer(models.Model):
    address_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_customers"
    )
    dob = models.DateField()
    prefered_language = models.CharField(
        max_length=15, choices=enums.Language.choices, default=enums.Language.ENGLISH
    )
    prefered_payment_method = models.CharField(
        max_length=25,
        choices=enums.PaymentMethod.choices,
        default=enums.PaymentMethod.CASH_ON_DELIVERY,
    )
    total_spent = models.DecimalField(max_digits=10, decimal_places=2)
    last_order_date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
