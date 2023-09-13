from django.db import models
from django.utils import timezone

from django.conf import settings 

class Calendar(models.Model):

    name    = models.CharField(verbose_name="カレンダー名", max_length=100)
    dt      = models.DateTimeField(verbose_name="投稿日時",default=timezone.now)

    user    = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="投稿者", on_delete=models.CASCADE)
    share   = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name="公開範囲", through="CalendarUser", related_name="calendar_share" )


class Schedule(models.Model):

    calendar    = models.ForeignKey(Calendar, verbose_name="カレンダー", on_delete=models.CASCADE )

    start_dt    = models.DateTimeField(verbose_name="開始日時")
    end_dt      = models.DateTimeField(verbose_name="終了日時")

    content     = models.CharField(verbose_name="内容", max_length=500)
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="投稿者", on_delete=models.CASCADE)


class CalendarUser(models.Model):

    calendar    = models.ForeignKey(Calendar, verbose_name="カレンダー", on_delete=models.CASCADE)
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="対象ユーザー", on_delete=models.CASCADE)

    read        = models.BooleanField(verbose_name="読み込み権限", default=False)
    write       = models.BooleanField(verbose_name="書き込み権限", default=False)
    chat        = models.BooleanField(verbose_name="チャット権限", default=False)


## カレンダーに紐付けるメッセージ
"""
class CalendarMessage(models.Model):

    calendar    = models.ForeignKey(Calendar, verbose_name="カレンダー", on_delete=models.CASCADE)
    dt          = models.DateTimeField(verbose_name="投稿日時",default=timezone.now)

    user        = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="投稿者", on_delete=models.CASCADE)
    content     = models.CharField(verbose_name="内容", max_length=500)
"""
