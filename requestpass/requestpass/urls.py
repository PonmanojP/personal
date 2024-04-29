from django.urls import path
from demo import views

urlpatterns = [
    path('user/', views.user_page, name='user_page'),
    path('restaurant/', views.restaurant_page, name='restaurant_page'),
    path('accept/<int:request_id>/', views.accept_request, name='accept_request'),
]
