from django.http import HttpResponse
from django.template import loader


def index_view(request):
    template = loader.get_template('main/index.html')
    return HttpResponse(template.render(request=request))


def mentions_view(request):
    template = loader.get_template('main/mentions.html')
    return HttpResponse(template.render(request=request))
