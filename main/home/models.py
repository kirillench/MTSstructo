from django.db import models

class OrganizationalMember(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя")
    surname = models.CharField(max_length=255, verbose_name="Фамилия")
    position = models.CharField(max_length=255, verbose_name="Должность")
    email = models.EmailField(unique=True, verbose_name="Email")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    supervisor = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True, related_name='subordinates', verbose_name="Ссылка на руководителя"
    )  # Ссылка на руководителя

    def __str__(self):
        return f"{self.name} {self.surname} ({self.position})"

    class Meta:
        verbose_name = "Член организации"
        verbose_name_plural = "Члены организации"

