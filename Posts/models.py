from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Posts(models.Model):
	title = models.CharField(max_length=225)
	url = models.TextField()
	pub_date = models.DateTimeField()
	vote_total = models.IntegerField(default=1)
	icon = models.ImageField(upload_to='images/')
	image = models.ImageField(upload_to='images/')
	body = models.TextField()
	explored_by = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

	def summary(self):
		return self.body[:100]

	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e %Y')