from django.db import models


class Account(models.Model):
    name = models.CharField(
        max_length=50,
    )
    email = models.CharField(
        max_length=100,
    )
    join_date = models.DateTimeField(
        auto_now_add=True,
         null=True
    )
    def __str__(self):
        return self.name