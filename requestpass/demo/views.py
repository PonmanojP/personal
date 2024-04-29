from django.shortcuts import render
from django.http import JsonResponse
from .models import FoodRequest

def user_page(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        food_details = request.POST.get('food_details')
        FoodRequest.objects.create(user_name=user_name, food_details=food_details)
        return JsonResponse({'status': 'success'})
    return render(request, 'user_page.html')

def restaurant_page(request):
    requests = FoodRequest.objects.filter(status='Pending')
    return render(request, 'restaurant_page.html', {'requests': requests})

def accept_request(request, request_id):
    food_request = FoodRequest.objects.get(pk=request_id)
    food_request.status = 'Accepted'
    food_request.save()
    return JsonResponse({'status': 'success'})
