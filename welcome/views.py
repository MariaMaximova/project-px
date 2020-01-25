import datetime
from django.shortcuts import render


# def index(request):
#    return HttpResponse('Hello world from Django')

def main_view(request):
    if request.method == 'GET':
        return render(
            request, "main.html", context={
                "now": datetime.datetime.now()
            }
        )


def about_view(request):
    if request.method == "GET":
        return render(
            request, "about.html",
            context={"now": datetime.datetime.now()}
        )


def upload_file(request):
    if request.method == 'POST':
        pass