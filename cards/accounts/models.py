from django.db import models


class Account(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        default='User',
        blank=False
    )
    email = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        default='aaa'
    )
    join_date = models.DateTimeField(
        auto_now_add=True,
         null=True
    )
    def __str__(self):
        return self.name
    #xd