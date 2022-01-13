from django.shortcuts import render
from django.http import HttpResponse
# from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'home.html', {'name':"Sai"})

# @csrf_exempt
def add(request):
    # val1 = request.GET['num1']
    # val2 = request.GET['num2']
    # val1 = request.GET['num1']
    val1 =int(request.POST.get('num1'))
    val2 =int(request.POST.get('num2'))
    res = val1+val2
    return render(request, 'result.html', {'result' :res})

#
