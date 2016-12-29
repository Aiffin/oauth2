from django.db import models

# Create your models here.
class Register(models.Model):
	name=models.CharField(max_length=30)
	ph_no=models.CharField(max_length=10)
	address=models.TextField()
	date=models.DateTimeField(auto_now_add=True)
	linenos=models.BooleanField(default=False)

	class Meta:
		ordering=('name',)