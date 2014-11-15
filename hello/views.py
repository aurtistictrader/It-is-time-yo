from django.shortcuts import render
from django.http import HttpResponse

from .models import Reminder

# Create your views here.
def index(request):
    return HttpResponse('Hello from Python!')


def db(request):

    greeting = Reminder()
    greeting.save(using='default')

    greetings = Reminder.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

