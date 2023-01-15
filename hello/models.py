from django.db import models
from django.utils import timezone

ticket_type = (
    ("Student", "Student"),
    ("Child", "Child"),
    ("Adult", "Adult"),
)

age_rating = (
    ("U", "U"),
    ("PG", "PG"),
    ("12", "12"),
    ("12A", "12A"),
    ("15", "15"),
    ("18", "18"),
    
)


class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"


class ageRating(models.Model):
    ageID = models.AutoField(primary_key=True,unique=True)
    ageRating = models.CharField(max_length=10, choices=age_rating, default="000000")
    
    def __str__(self):
        return self.ageRating

class Showings(models.Model):
    showingID = models.AutoField(primary_key=True,unique=True)
    showingTime = models.TimeField()

class Film(models.Model):
    filmID = models.AutoField(primary_key=True,unique=True)
    filmName = models.CharField(max_length=50)
    filmLength = models.TimeField()
    
    def __str__(self):
        return self.filmName

class Booking(models.Model):
    bookingID = models.AutoField(primary_key=True,unique=True)
    date = models.DateField()
    time = models.TimeField()
    seatNum = models.IntegerField()
    filmName = models.ForeignKey(Film, related_name='+', on_delete=models.CASCADE,default='000000')
    ageRating = models.ForeignKey(ageRating, related_name='+', on_delete=models.CASCADE,default='000000')
    ticketType = models.CharField(max_length=20, choices=ticket_type, default="Student")

    def __str__(self):
        return self.bookingID
