from django.shortcuts import render
from .access import start_payment
from django.http import JsonResponse
import logging

# Create your views here.
def handle_mpesa(request):
    if request.method == "POST":
        start_payment()
        return JsonResponse({'status': 'OK'})
    
def get_response(request):
    return JsonResponse({'response': request})


