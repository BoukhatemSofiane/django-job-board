from django.db import models

# Create your models here.
JOB_TYPE = (#hena pcq 3andena ikhtiyarat 
    ('Full Time','Full Time'),
    ('Part Time','Part Time')
)
class Job(models.Model):
    title = models.CharField(max_length=200) # fist column 
    # location
    job_type = models.CharField(max_length=15, choices=JOB_TYPE)# hena fl choices zdena el 9iyam li rahom el fo9
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

# 3onewan el wadhifa
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name