class Sample (models.Model):
	song=models.CharField(max_length=50)
	artist=models.CharField(max_length=50)

class Song (models.Model): 
	song=models.CharField(max_length=50)
	artist=models.CharField(max_length=50)
	samples=models.ManyToManyField(Sample)