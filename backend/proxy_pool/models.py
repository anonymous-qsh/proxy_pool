from django.db import models

from utils.date_time import now


class Proxy(models.Model):
    address = models.CharField(max_length=32, help_text='代理地址', unique=True)
    checked_time_stamp = models.IntegerField(default=now)

    class Meta:
        db_table = 'proxy'

