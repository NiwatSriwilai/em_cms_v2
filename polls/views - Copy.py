from django.http import HttpResponse

#HttpResponse("Hello, world. You're at the polls index.")
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
