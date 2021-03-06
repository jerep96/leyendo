from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

MODO = (
	('Business', 'Business'),
	('Social', 'Social'),
	('Otro', 'Otro')
	)

COLOR = (
	('fucsia','fucsia'),
	('blanco','blanco'),
	('negro','negro'),
	('rojo','rojo'),
	('azul','azul'),
	('verde','verde'),
	('amarillo','amarillo'),
	('naranja','naranja'),
	('gris','gris'),
	('violeta','violeta')
	)


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='photos', default='batman.png')
	modo = models.CharField(default='Business', max_length=50, choices=MODO)
	colorBoton = models.CharField(default='negro', max_length=50, choices=COLOR)
	colorFondo= models.CharField(default='negro', max_length=50, choices=COLOR)
	portada = models.ImageField(upload_to='photos', default='portada.jpg')


	def __str__(self):
		return f'Perfil de {self.user.username}'


class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
	timestamp = models.DateTimeField(default=timezone.now)
	content = models.TextField()

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return f'{self.user.username}: {self.content}'


class Url(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='urls')
	timestamp = models.DateTimeField(default=timezone.now)
	title = models.TextField()
	modo = models.CharField(default='business', max_length=50, choices=MODO)
	content = models.TextField()

	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return f'{self.user.username}: {self.title}'


class Relationship(models.Model):
	from_user = models.ForeignKey(User, related_name='relationships', on_delete=models.CASCADE)
	to_user = models.ForeignKey(User, related_name='related_to', on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.from_user} to {self.to_user}'

	class Meta:
		indexes = [
		models.Index(fields=['from_user', 'to_user',]),
		]










