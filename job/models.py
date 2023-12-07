from django.db import models

# Create your models here.


class Job(models.Model):
    title = models.CharField(max_length=256, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    salary = models.IntegerField(verbose_name="Зарплата")
    qualifications = models.JSONField(verbose_name="Требования")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"


class Response(models.Model):
    cover_letter = models.TextField(verbose_name="Сопроводительное Письмо")
    job = models.ForeignKey("Job", on_delete=models.PROTECT) #Protect won't let you delete a job line, Use Cascade for the opposite
    user = models.ForeignKey("User", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Response on {self.job.title}"

    class Meta:
        verbose_name = "Отклик"
        verbose_name_plural = "Отклики"


class User(models.Model):
    name = models.CharField(max_length=30, verbose_name="Имя")
    last_name = models.CharField(max_length=30, verbose_name="Фамилия")
    phone_number = models.CharField(max_length=40, verbose_name="Hомер телефона")
    email = models.EmailField()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"{self.name}"
