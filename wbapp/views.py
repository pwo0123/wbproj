from django.shortcuts import render


def index(request):
    content = {
        'text': 'hello'
    }

    return render(request, 'base.html', content)
