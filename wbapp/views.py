from django.shortcuts import render
from django.views.generic.list import ListView
from .models import CFS
from django.http import JsonResponse


def index(request):
    content = {
        'text': 'hello'
    }

    return render(request, 'base.html', content)


class CFSActiveList(ListView):
    model = CFS
    template_name = 'cfs.html'
    ordering = ['beat']


def cfsfeed(request):
    info = CFS.objects.all().values('beat', 'address', 'is_active')
    infolist = list(info)
    return JsonResponse(infolist, safe=False)







