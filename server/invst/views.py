from django.http import HttpResponse

def index(response):
    output = 'hi'
    return HttpResponse(output)
