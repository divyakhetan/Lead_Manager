from django.shortcuts import render

# Create your views here.

def index(request):
    # will directly look up in the templates folder
    return render(request, 'frontend/index.html')

