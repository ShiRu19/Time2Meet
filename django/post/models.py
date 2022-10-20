from django.db import models

class Project(models.Model):
    class Meta:
        verbose_name = '專案列表'
        verbose_name_plural = '專案列表'

    projectName = models.CharField('專案名稱', max_length=20, blank=False)

    def __str__(self):
        return self.projectName

class User(models.Model):
    class Meta:
        verbose_name = '使用者列表'
        verbose_name_plural = '使用者列表'

    userName = models.CharField('使用者名稱', max_length=100, blank=False)
    userPassword = models.CharField('使用者密碼', max_length=20, blank=True)

    def __str__(self):
        return self.userName
