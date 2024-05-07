from django.db import models
# from mptt.models import MPTTModel, TreeForeignKey
from tree_queries.models import TreeNode
from tree_queries.query import TreeQuerySet
from tree_queries.fields import TreeNodeForeignKey


class Menu(models.Model):
    name = models.CharField(max_length=30, verbose_name='Name')

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name


class MenuItem(TreeNode):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, verbose_name='Меню', default="")
    name = models.CharField(max_length=100, unique=True)
    url = models.CharField('URL', max_length=255)
    position = models.PositiveIntegerField('Position', default=1)
    parent = TreeNodeForeignKey("self",
                                blank=True,
                                null=True,
                                on_delete=models.CASCADE,
                                verbose_name=("parent"),
                                related_name="children")
    objects = TreeQuerySet.as_manager()

    class Meta:
        ordering = ("menu__id", "-parent__id", "position", "name")
        verbose_name = 'Элемент Меню'
        verbose_name_plural = 'Элементы Меню'

    def __str__(self):
        return str(self.name)
