from django.db import models
# Create your models here.


class User(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)

    def __str__(self):
        return "Пользователь %s %s" % (self.name, self.email,)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
