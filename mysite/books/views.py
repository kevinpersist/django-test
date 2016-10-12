from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

from models import Book

# Create your views here.
def search_form(request):
    return render_to_response('search_form.html')

#def search(request):
#    if 'q' in request.GET:
#        message = 'You searched for: %r' % request.GET['q']
#    else:
#        message = 'You submitted an empty form.'
#    return HttpResponse(message)

#def search(request):
#    if 'q' in request.GET:
#        q = request.GET['q']
#        if q != '': 
#            books = Book.objects.filter(title__icontains=q)
#            return render_to_response('search_results.html', {'books': books, 'query': q})
#        else:
#            return render_to_response('search_form.html', {'error': True})

#def search(request):
#    error = False
#    if 'q' in request.GET:
#        q = request.GET['q']
#        if not q:
#            error = True
#        else:
#            books = Book.objects.filter(title__icontains=q)
#            return render_to_response('search_results.html', {'books': books, 'query': q})
#    return render_to_response('search_form.html', {'error': error})

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html', {'books': books, 'query': q})
    return render_to_response('search_form.html', {'errors': errors})

def contact(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Enter a valid e-mail address')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    return render_to_response('contact_form.html', {
        'errors': errors,
        'subject': request.POST.get('subject', ''),
        'message': request.POST.get('message', ''),
        'email': request.POST.get('email', ''),
        })
