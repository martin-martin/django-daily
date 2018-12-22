from django.shortcuts import render


def write(request):
    return render(request, 'canvas.html')