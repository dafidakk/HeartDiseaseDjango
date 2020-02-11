from django.db import models

# Create your models here.

class approvals(models.Model):
	GENDER_CHOICES =(
	 	('Erkek',' 1'),
		('Kadın', '0')
	)
	CHEST_PAIN_CHOICES = (
		('0',' 0'),
		('1', '1'),
		('2', '2'),
		('3', '3'),
		('4', '4')
	)
	FASTING_BLOOD_SUGAR_CHOICES = (
		('0', '0'),
		('1', '1')
	)
	ELECTROCARDIOGRAPHIC_CHOICES = (
		('0', '0'),
		('1', '1'),
		('2', '2')
	)
	ANJINA_CHOICES = (
		('Evet', '1'),
		('Hayır', '0')
	)
	SLOPE_CHOICES= (
		('0', '0'),
		('1', '1'),
		('2', '2')
	)




	firstname=models.CharField(max_length=15)
	lastname=models.CharField(max_length=15)
	Age=models.IntegerField(default=0)
	Sex=models.CharField(max_length=15,choices=GENDER_CHOICES)
	Cp=models.IntegerField(default = 0, choices=CHEST_PAIN_CHOICES)
	Trestbps=models.IntegerField(default = 0)
	Chol=models.IntegerField(default = 0)
	Fbs=models.IntegerField(default = 0, choices= FASTING_BLOOD_SUGAR_CHOICES)
	Restecg=models.IntegerField(default = 0,choices= ELECTROCARDIOGRAPHIC_CHOICES)
	Thalach=models.IntegerField(default = 0)
	Exang=models.CharField(max_length=15,choices= ANJINA_CHOICES)
	Oldpeak=models.IntegerField(default = 0)
	Slope=models.IntegerField(default = 0,choices=SLOPE_CHOICES)
	Ca =models.IntegerField(default = 0,choices=[('0', 0),('1', 1),('2', 2),('3', 3),('4',4)])
	Thal=models.IntegerField(default = 0,choices=[('0', 0),('1', 1),('2', 2),('3', 3)])
	def __str__(self):
		return '{}, {}'.format(self.lastname, self.firstname)
