
#  import the HttpResponse object from the django.http module
from django.shortcuts import render
from django.http import HttpResponse

# Input:    takes in a HttpRequest object from the django.http module
# Output:   return a HttpResponse object that takes a string parameter representing the content of the page we wish to send to the client requesting the view
def index(request):
    # return HttpResponse("Rango says hey there partner!  <a href='/rango/about/'>About</a>")
    # ### Chapter 4
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    # return HttpResponse("Rango says here is the about page. <a href='/rango/about.html'>Index</a>")
    # ### Chapter 4
    return render(request, 'rango/about.html')
