from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', verbose_name='用户')
    number = models.CharField(max_length=11, verbose_name='电话号码')
    followers = models.ManyToManyField(
        'UserProfile',
        related_name='following',
        blank=True,
        verbose_name='关注TA的人'
    )

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.username
