from django.db import models
from django.template.defaultfilters import slugify


class Category(models.Model):
    """字段名不能有两个下划线如：name__first等 因为两个下划线是Django的查询语法;
    使用Django的ImageField需要提前安装pillow模块，pip install pillow即可"""
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)  # 添加slug字段是为了在url中用caregory的name属性而不用数字以增加url的可读性例如：rango/category/python 而不用rango/category/1

    class Meta:
        verbose_name_plural = 'Categories'  # 默认情况下，在admin上显示的是Categorys，但是这不是英文的正确的复数形式，所以通过这个参数重命名为人类可读的形式

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """save function update slug when the name of category is changed"""
        self.slug = slugify(self.name)  # 把空格转换成连字符“-”(有空格在url中是unsafe)
        super().save(*args, **kwargs)
        """在这里遇到一个坑就是调用父类的时候没有把*和**符号带上即super().save(args, kwargs),
        导致报错:ValueError: Cannot force an update in save() with no primary key,"""


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title