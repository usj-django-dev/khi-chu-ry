from django.db import models

# Create your models here.

class Musician(models.Model):
    #id = models.AutoFiled(Primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Album(models.Model):
    #id = models.AutoFiled(Primary_key=True)
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    rating = (
    (1,  "Worst"),
    (2,  "Bad"),
    (3,  "Not Bad"),
    (4,  "Good"),
    (5,  "Excelient!"),
    )

    num_stars = models.IntegerField(choices=rating)
    def __str__(self):
        return self.name + ", Rating: " + str(self.num_stars)
