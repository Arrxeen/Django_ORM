from django.db import models


class User(models.Model):
    class Role(models.TextChoices):
        admin = 'admin', 'ADMIN'    
        user = "user", "USER"
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    role = models.CharField(max_length=100, choices= Role.choices, default=Role.user)

    def __str__(self):
        return self.name


class Task(models.Model):
    class Statuse(models.TextChoices):
        in_work= 'done', 'DONE'
        processing = 'processing', 'PROCESSING'
        no_work= 'no work', 'NO WORK'
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=100, choices= Statuse.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey("User", on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title

    