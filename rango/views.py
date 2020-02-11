
#  import the HttpResponse⁷ object from the django.http module
from django.shortcuts import render
from django.http import HttpResponse


# View file consists of series of individual functions

# Input:    takes in a HttpRequest object from the django.http module
# Output:   return a HttpResponse object that takes a string parameter representing the content of the page we wish to send to the client requesting the view
def index(request):
    return HttpResponse("Rango says hey there partner!  <a href='/rango/about/'>About</a>")

def about(request):
    return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")
