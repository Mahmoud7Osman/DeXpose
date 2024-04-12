from django.db import models

class Addresses(models.Model):
    addressId = models.CharField(max_length=10)
    domainName = models.CharField(max_length=30)
    ipv4Address = models.CharField(max_length=15)
    port = models.CharField(max_length=5)
