from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class profile(models.Model):
	objects = None
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics', blank=True, null=True)

	# @property
	# def __str__(self):
	# 	return f'{self.user.username} Profile'

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		# print(self.image.default)

		# img = Image.open(self.image.path)
		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img = Image.open(self.image.path)
			img.save(self.image.path)

