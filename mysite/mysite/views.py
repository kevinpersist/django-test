from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from books.models import Book

import datetime
import MySQLdb
import csv

def hello(request):
    return HttpResponse("Hello world")

#def current_datetime(request):
#    now = datetime.datetime.now()
#    html = '<html><body>It is now %s.</body></html>' % now
#    return HttpResponse(html)

#def current_datetime(request):
#    now = datetime.datetime.now()
#    t = Template("<html><body>It is now {{ current_date }}.</body></html>")
#    html = t.render(Context({'current_date':now}))
#    return HttpResponse(html)

#def current_datetime(request):
#    now = datetime.datetime.now()
#    fp = open('/home/djcode/mysite/template/mytemplate.html')
#    t = Template(fp.read())
#    html = t.render(Context({'current_date': now}))
#    return HttpResponse(html)

def current_datetime1(request):
    now = datetime.datetime.now()
    t = get_template('currente_datetime.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)

def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('currente_datetime.html', {'current_date': now})

def hours_ahead1(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render_to_response('hours_ahead.html', {'hour_offset': dt})

def book_list(request):
    books = Book.objects.order_by('name')
    return render_to_response('book_list.html', {'books': books})

def request_info(request):
    #html = 'path:' + request.path + ' host:' + request.get_host() # ' is_secure' + request.is_secure()
    #return HttpResponse("<p>Welcome to the page at %s<p>The host is %s." % (request.path, request.get_host()))
    #return HttpResponse(request.META)
    values = request.META.items()
    values.sort()
    #html = []
    #for k, v in values:
    #    html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    #return HttpResponse('<table>%s</table>' % '\n'.join(html))
    return render_to_response('display_meta.html', {'values': values})

def year_archive(request, year):
    year = year
    return HttpResponse("year: %s" % year)

def month_archive(request, year, month):
    year = year
    month = month
    return HttpResponse("year: %s, month: %s" % (year, month))

def foobar_view(request, template_name):
    m_list = 'test'
    return render_to_response(template_name, {'m_list': m_list})

def views_myview(request, month, day):
    month = month
    day = day
    return HttpResponse("month: %s, day: %s." % (month, day))

###return image
def my_image(request):
    image_data = open("/home/djcode/mysite/static/image.png", "rb").read()
    return HttpResponse(image_data, mimetype="image/png")

###create csv file
UNRULY_PASSENGERS = [146,184,235,200,226,251,299,273,281,304,203]

def unruly_passengers_csv(request):
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=unruly.csv'

    writer = csv.writer(response)
    writer.writerow(['Year', 'Unruly Airline Passengers'])
    for (year, num) in zip(range(1995, 2006), UNRULY_PASSENGERS):
        writer.writerow([year, num])
    return response

###create PDF
from reportlab.pdfgen import canvas

def hello_pdf(request):
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Dispositon'] = 'attachment; filename=hello.pdf'

    p = canvas.Canvas(response)
    p.drawString(0, 0, '''def hello_pdf(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(mimetype='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=hello.pdf'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response''')

    p.showPage()
    p.save()
    return response

def show_color(request):
    if "favorite_color" in request.COOKIES:
        return HttpResponse("Your favorite color is %s" % request.COOKIES['favorite_color'])
    else:
        return HttpResponse("Your don't have a favorite color.")

def set_color(request):
    if "favorite_color" in request.GET:
        response = HttpResponse("Your favorite color is now %s" % request.GET["favorite_color"])
        response.set_cookie("favorite_color", request.GET["favorite_color"])
        #request.session['favorite_color'] = request.GET["favorite_color"]
        return response

    else:
        return HttpResponse("You didn't give a favorite color.")

def test_icon(request):
    return render_to_response('test_icon.html', {'values': 'values'})
