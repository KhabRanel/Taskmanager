from django.shortcuts import render


def index(request):
    data = {

    }
    return render(request, 'tasks/index.html', context=data)