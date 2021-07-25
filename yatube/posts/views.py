from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Главная страниц')


def group_posts(request):
    return HttpResponse('По группам')
