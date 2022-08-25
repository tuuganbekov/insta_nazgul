from django.shortcuts import render


def get_cabinet(request):
    return render(request, 'cabinet.html', {})