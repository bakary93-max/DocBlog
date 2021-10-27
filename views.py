from django.http import HttpResponse
from datetime import  datetime
from django.shortcuts import render


def index(request):
    date = datetime.today()
    print(date)
    print(type(date))
    return render(request, "index.html", context= {"prenom":date})