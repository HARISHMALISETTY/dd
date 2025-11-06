from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
def sample(request):
    return HttpResponse('hello')
def sample1(request):
    return JsonResponse({"name":"hariah"})
def dynamicResponse(request):
    name=request.GET.get('name','') 
    gender=request.GET.get('gender','')
    return HttpResponse(f"{name} of {gender}")
def multiplication_table(request):
    n = int(request.GET.get("n", ""))
    upto = int(request.GET.get("upto", "10"))
    lines = [f"{n}x{i}={n*i}" for i in range(1, upto + 1)]
    return JsonResponse(lines, safe=False)  
