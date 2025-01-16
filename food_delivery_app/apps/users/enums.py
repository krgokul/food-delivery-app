from django.db import models


class Role(models.TextChoices):
    CUSTOMER = "customer"
    ADMIN = "admin"
    RESTAURANT_OWNER = "restaurant_owner"
    DELIVERY_PARTNER = "delivery_partner"


class Gender(models.TextChoices):
    MALE = "male"
    FEMALE = "female"
    NON_BINARY = "non_binary"
    PREFER_NOT_TO_SAY = "prefer_not_to_say"


class AddressType(models.TextChoices):
    HOME = "home"
    OFFICE = "office"
    HOTEL = "hotel"
    OTHER = "other"


class PaymentMethod(models.TextChoices):
    CREDIT_CARD = "credit_card"
    DEBIT_CARD = "debit_card"
    NET_BANKING = "net_banking"
    UPI = "upi"
    WALLET = "wallet"
    CASH_ON_DELIVERY = "cash_on_delivery"


class Language(models.TextChoices):
    ENGLISH = "english"
    TAMIL = "tamil"
    TELUGU = "telugu"
    HINDI = "hindi"
