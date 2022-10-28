from django.db import models

class Project(models.Model):
    class Meta:
        verbose_name = '專案列表'
        verbose_name_plural = '專案列表'
        db_table='project'

    projectName = models.CharField('專案名稱', max_length=20, blank=False)
    availableTime = models.CharField('可用時間', max_length=500, blank=True)
    
    def __str__(self):
        return self.projectName

class User(models.Model):
    class Meta:
        verbose_name = '使用者列表'
        verbose_name_plural = '使用者列表'
        db_table='user'

    userName = models.CharField('使用者名稱', max_length=100, blank=False)
    userPassword = models.CharField('使用者密碼', max_length=20, blank=True)
    availableTime = models.CharField('可用時間', max_length=500, blank=True)

    def __str__(self):
        return self.userName

class Participation(models.Model):
    class Meta:
        verbose_name = '專案參與列表'
        verbose_name_plural = '專案參與列表'
        db_table='participation'

    projectId = models.CharField('專案ID', max_length=20, blank=False)
    userId = models.CharField('使用者ID', max_length=20, blank=False)

    def __str__(self):
        return self.projectId

class ParticipationDetail(models.Model):
    class Meta:
        verbose_name = '專案參與列表'
        verbose_name_plural = '專案參與列表'

    projectId = models.ForeignKey(
        Project, related_name="project", on_delete=models.DO_NOTHING
    )
    userId = models.ForeignKey(
        User, related_name="user", on_delete=models.DO_NOTHING
    )

    #projectId = models.CharField('專案ID', max_length=20, blank=False)
    #userId = models.CharField('使用者ID', max_length=20, blank=False)

    def __str__(self):
        return self.projectId