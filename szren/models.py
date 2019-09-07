from django.db import models

# Create your models here.


class Professional(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True)
    number = models.CharField(max_length=12, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"专业信息"
        verbose_name_plural = verbose_name


class Subjects(models.Model):
    pro = models.ForeignKey(Professional, blank=True, null=True,
                            related_name='sz_pro', verbose_name="所属专业", on_delete=models.CASCADE)
    name = models.CharField(max_length=128, blank=True, null=True)
    number = models.CharField(max_length=12, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"科目信息"
        verbose_name_plural = verbose_name


class MultipleChoice(models.Model):
    pro = models.ForeignKey(Professional, blank=True, null=True,
                            related_name='mu_pro', verbose_name="所属专业", on_delete=models.CASCADE)
    subject = models.ForeignKey(Subjects, blank=True, null=True,
                                related_name='mu_sub', verbose_name="所属科目", on_delete=models.CASCADE)
    title = models.CharField(u'题目', max_length=520, blank=True, null=True)
    options = models.TextField(u'选项', blank=True, null=True)
    result = models.CharField(u'答案', max_length=13, blank=True, null=True)
    create_time = models.DateTimeField(u'新建时间', auto_now_add=True, blank=True, null=True)
