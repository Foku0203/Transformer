# pretrained/views.py
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'pretrain/home.html')  # ใช้เทมเพลตที่เราสร้างไว้

def train(request):
    return HttpResponse("Train page OK")

def predict(request):
    return HttpResponse("Predict page OK")