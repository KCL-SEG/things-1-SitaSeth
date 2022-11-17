from django.shortcuts import render

# Create your views here.

#First view
def home(request):
    return render(request, 'home.html')
