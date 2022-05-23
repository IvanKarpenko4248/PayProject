from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=20, verbose_name="Название")
    description = models.TextField(verbose_name="Описание", default='', blank=True)
    price = models.FloatField(verbose_name='Стоимость', default=0, blank=True)

    def save(self, *args, **kwargs):
        self.price = round(self.price, 2)
        super().save(args, kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'
