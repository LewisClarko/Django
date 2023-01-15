from django.shortcuts import redirect, render
from django.utils.timezone import datetime
from django.views.generic import ListView

from hello.forms import LogMessageForm, BookingForm #, FilmForm
from hello.models import LogMessage, Booking, Film


class HomeListView(ListView):
    """Renders the home page, with a list of all polls."""

    model = LogMessage
    

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

class BookingListView(ListView):
    """Renders the home page, with a list of all polls."""

    model = Booking

    def get_context_data(self, **kwargs):
        context = super(BookingListView, self).get_context_data(**kwargs)
        return context
    


def about(request):
    """Renders the about page."""
    return render(request, "hello/about.html")


def contact(request):
    """Renders the contact page."""
    return render(request, "hello/contact.html")


def hello_there(request, name):
    """Renders the hello_there page.
    Args:
        name: Name to say hello to
    """
    return render(
        request, "hello/hello_there.html", {"name": name, "date": datetime.now()}
    )
    

def log_message(request):
    form = LogMessageForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
        else:
            return render(request, "hello/log_message.html", {"form": form})
    else:
        return render(request, "hello/log_message.html", {"form": form})


def create_booking(request):
    form = BookingForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.save()
            return redirect("home")
        else:
            return render(request, "hello/create_booking.html", {"form": form})
    else:
        return render(request, "hello/create_booking.html", {"form": form})

def updateBooking(request, pk):
    booking = Booking.objects.get(pk=pk)
    form = BookingForm(request.POST or None, instance=booking)

    if request.method == "POST":
        if form.is_valid():
            booking = form.save(commit=False)

            booking.save()
            return redirect("home")
    else:
        return render(request, "hello/create_booking.html", {"form": form})
    
def deleteBooking(request, pk):
    booking = Booking.objects.get(pk=pk)
    booking.delete()
    return redirect("home")



# def create_film(request):
#     form = FilmForm(request.POST or None)
#     if request.method == "POST":
#         if form.is_valid():
#             message = form.save(commit=False)
#             message.save()
#             return redirect("home")
#         else:
#             return render(request, "hello/create_film.html", {"form": form})
#     else:
#         return render(request, "hello/create_film.html", {"form": form})
    