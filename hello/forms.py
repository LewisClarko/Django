from django import forms

from hello.models import LogMessage, Booking, Film

class LogMessageForm(forms.ModelForm):
    class Meta:
        model = LogMessage
        fields = ("message",)  # NOTE: the trailing comma is required
        
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ("bookingID","date","time","seatNum","filmName","ageRating","ticketType")  # NOTE: the trailing comma is required     
        
# class FilmForm(forms.ModelForm):
#     class Meta:
#         model = Film
#         fields = ("filmID","filmName","filmLength","ageRating",)  # NOTE: the trailing comma is required     
        