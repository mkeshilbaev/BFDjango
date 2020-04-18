from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse

def index(request):
    print(request)
    return HttpResponse('madi')

