from django.db import models


class Brand(models.Model):
    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описание', blank=True)
    image = models.ImageField('Логотип', upload_to='brands/')

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return {self.name}


class Product(models.Model):

    volumes = [
        ('30мл', '30мл'),
        ('50мл', '50мл'),
        ('100мл', '100мл')
]

    name = models.CharField('Название', max_length=100)
    brand = models.CharField('Бренд', max_length=70)
    price = models.DecimalField('Стоимость', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField('Количество')
    description = models.TextField('Описание', blank=True)
    image = models.ImageField('Изображение', upload_to='products/')
    volume = models.CharField('Объем', max_length=10, choices=volumes)
    date_create = models.DateField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['-date_create']

    def __str__(self):
        return f'{self.name} за {self.price}'
