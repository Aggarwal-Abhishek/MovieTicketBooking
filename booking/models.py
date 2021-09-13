from django.db import models
from django.conf import settings

class Theatre(models.Model):
    city_choice = (
        ('DELHI', 'Delhi'),
        ('NOIDA', 'Noida'),
        ('Ghaziabad', 'Ghaziabad'),
        ('Modinagar', 'Modinagar')
    )
    name = models.CharField(max_length=50, null=False)
    city = models.CharField(max_length=9, choices=city_choice, null=False)

    def __str__(self):
        return f'{self.name}: {self.city}'

class Movie(models.Model):
    name = models.CharField(max_length=50, null=False)
    length = models.IntegerField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    trailer = models.URLField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)
    time = models.DateTimeField()
    amount = models.IntegerField(default=0)

    def __str__(self):
        return f'({self.movie}) - {self.theatre} - {str(self.time)}'

class Seat(models.Model):
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    seat_name = models.CharField(unique=True, max_length=2, null=False, blank=False)

    class Meta:
        unique_together = ('show', 'seat_name')
    
    def __str__(self):
        return f'{self.show} | {self.seat_name}'

class Booked(models.Model):
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    booked_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, blank=True)
    time = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return f'Booked by {self.booked_by} at {self.time}'


