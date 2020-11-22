from django.db import models


class Blocks(models.Model):
    block_name = models.CharField('имя блока', max_length=50)

    def __str__(self):
        return self.block_name

    class Meta:
        verbose_name = 'Блок'
        verbose_name_plural = 'Блоки'


class Elements(models.Model):
    blocks = models.ForeignKey(Blocks, on_delete=models.CASCADE)
    element_name = models.CharField('имя элемента', max_length=50)
    element_text = models.TextField('текст елемента')

    def __str__(self):
        return self.element_name

    class Meta:
        verbose_name = 'Элемент'
        verbose_name_plural = 'Элементы'
