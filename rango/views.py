
#  import the HttpResponse object from the django.http module
from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

# Input:    takes in a HttpRequest object from the django.http module
# Output:   return a HttpResponse object that takes a string parameter representing the content of the page we wish to send to the client requesting the view
def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by the number of likes in descending order.
    # Retrieve the top 5 only -- or all if less than 5.
    # Place the list in our context_dict dictionary (with our boldmessage!)
    # that will be passed to the template engine.
    category_list = Category.objects.order_by('-likes')[:5] # in descending order, retrieve top 5 categories
    print(category_list)
    context_dict = {}
    # context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    # return HttpResponse("Rango says here is the about page. <a href='/rango/about.html'>Index</a>")
    # ### Chapter 4
    return render(request, 'rango/about.html')
