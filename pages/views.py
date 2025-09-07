from django.shortcuts import render

# Create your views here.

def home(request):
    print('testeando home')
    return render(request, 'pages/home.html')


def test(request):
    print(request)
    return render(request, 'pages/test.html')
