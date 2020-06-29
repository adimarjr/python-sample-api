from django.db import models

class ItemQuerySet(models.QuerySet):
    def t(self):
        return ""

class ItemManager(models.Manager):
    def get_querySet(self):
        return ItemQuerySet(self.model, using=self._db)

class Item(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    timeStamp = models.DateTimeField(auto_now_add=True)

    objects = ItemManager()

    def __str__(self):
        return self.name or ""