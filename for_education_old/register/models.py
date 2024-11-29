from django.db import models

# Create your models here.


# class Todo(models.Model):
#     title = models.CharField(max_length=200, null=False, blank=False)
#     created = models.DateTimeField(auto_now_add=True, null=False, blank=False)
#     deadline = models.DateTimeField(null=False, blank=False)
#     description = models.TextField(null=True, blank=True)
#     finished = models.DateTimeField(null=True)

#     def __str__(self):
#         return self.title

class RegisterClient(models.Model):
    name = models.CharField(verbose_name="Nome", max_length=200, null=False, blank=False)
    email = models.EmailField(verbose_name="E-mail", max_length=200, null=False, blank=False)
    phone = models.CharField(verbose_name="Celular", max_length=200, null=False, blank=False)
    password = models.CharField(verbose_name="Senha", max_length=200, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return self.name