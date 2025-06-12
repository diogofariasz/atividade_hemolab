from django.shortcuts import render

# Create your views here.

def main_view(request):
    return render(request, 'main.html')

def pag1_view(request):
    return render(request, 'pag1.html')

def pag2_view(request):
    return render(request, 'pag2.html')