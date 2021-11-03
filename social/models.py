import uuid

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

MODO = (
    ('Business', 'Business'),
    ('Social', 'Social'),
    ('Otro', 'Otro')
)

COLOR = (
    ('fucsia', 'fucsia'),
    ('blanco', 'blanco'),
    ('negro', 'negro'),
    ('rojo', 'rojo'),
    ('azul', 'azul'),
    ('verde', 'verde'),
    ('amarillo', 'amarillo'),
    ('naranja', 'naranja'),
    ('gris', 'gris'),
    ('violeta', 'violeta')
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombreB = models.CharField(default='Sin nombre', max_length=50)
    nombreS = models.CharField(default='Sin nombre', max_length=50)
    nombreO = models.CharField(default='Sin nombre', max_length=50)
    imageB = models.ImageField(upload_to='photos', default='batman.png')
    imageS = models.ImageField(upload_to='photos', default='batman.png')
    imageO = models.ImageField(upload_to='photos', default='batman.png')
    modo = models.CharField(default='Business', max_length=50, choices=MODO)
    colorBoton = models.CharField(default='negro', max_length=50, choices=COLOR)
    colorFondo = models.CharField(default='negro', max_length=50, choices=COLOR)
    portadaB = models.ImageField(upload_to='photos', default='portada.jpg')
    portadaS = models.ImageField(upload_to='photos', default='portada.jpg')
    portadaO = models.ImageField(upload_to='photos', default='portada.jpg')

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
    tipo = models.TextField(default='url', null=False, blank=False)
    modo = models.CharField(default='business', max_length=50, choices=MODO, null=True, blank=True)
<<<<<<< HEAD
    content = models.TextField()
    archivo = models.FileField(upload_to = 'static', null=True, blank=True)
    company = models.TextField(null=True)
    location = models.TextField()
    phone = models.TextField()
    mail = models.TextField()
    website = models.TextField()
=======
    content = models.TextField(null=True, blank=True)
    archivo = models.FileField(upload_to='static', null=True, blank=True)
    company = models.TextField(null=True, blank=True)
    location = models.TextField(null=True, blank=True)
    phone = models.TextField(null=True, blank=True)
    mail = models.TextField(null=True, blank=True)
    website = models.TextField(null=True, blank=True)
>>>>>>> 0da4793... fix
    lookup_id = models.UUIDField(default=uuid.uuid4, db_index=True)
    order = models.IntegerField(blank=False, default=100_000)

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
            models.Index(fields=['from_user', 'to_user', ]),
        ]
