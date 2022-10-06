from django.db import models

class Post(models.Model):
    class Meta:
        verbose_name = '時間表'
        verbose_name_plural = '時間表'

    projectName = models.CharField('專案名稱', max_length=20)
    userName = models.CharField('使用者名稱', max_length=100)

    def __str__(self):
        return self.projectName
