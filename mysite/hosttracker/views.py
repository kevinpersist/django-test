from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.

def login(request):
    return render_to_response('hosttracker/login.html', {'test':'OK'})
