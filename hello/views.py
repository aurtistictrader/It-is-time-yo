from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from time import strftime

from .forms import NameForm
from .models import Reminder

# Create your views here.
def index(request):

    return render(request, 'submit.html', {'form': NameForm(), 'greetings': Reminder.objects.all()})

def submit(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            my_model = Reminder()
            my_model.username = form.cleaned_data.get('username')
            my_model.message = form.cleaned_data.get('message')
            my_model.time_left = form.cleaned_data.get('time_left')
            my_model.time_created = strftime("%Y-%m-%d %H:%M:%S")
            my_model.save()	
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'submit.html', {'form': form, 'greetings': Reminder.objects.all() })

def db(request):

    greeting = Reminder()
    greeting.save(using='default')

    greetings = Reminder.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

