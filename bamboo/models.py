from django.db import models

class Method(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', blank=True,null=True)
    num_calls = models.IntegerField()
    total_time = models.FloatField()
    per_call_time = models.FloatField()
