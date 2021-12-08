from django.db import models

from user.models import Adminstrator


class Setting(models.Model):
    STATUS = (
        ('True', 'Mavjud'),
        ('False', 'Mavjud emas'),
    )
    user = models.ForeignKey(Adminstrator, on_delete=models.CASCADE)
    title = models.CharField(max_length=222)
    description = models.TextField(max_length=255)
    company = models.CharField(max_length=150)
    address = models.CharField(max_length=155, blank=True)
    phone = models.CharField(max_length=155, blank=True)
    email = models.CharField(max_length=155, blank=True)
    icon = models.ImageField(upload_to='media/images/setting/', blank=True)
    facebook = models.CharField(max_length=155, blank=True)
    instagram = models.CharField(max_length=155, blank=True)
    twitter = models.CharField(max_length=155, blank=True)
    youtube = models.URLField()
    aboutus = models.TextField(blank=True)
    contact = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'setting'
        verbose_name_plural = 'settings'

    def __str__(self):
        return self.title
