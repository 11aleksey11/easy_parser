from django.http import HttpResponse


def load_main_page(request):
    return HttpResponse('This is first page')
