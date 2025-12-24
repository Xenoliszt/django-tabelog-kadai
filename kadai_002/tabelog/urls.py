# store_app/urls.py

from django.urls import path
from . import views

app_name = 'tabelog'

urlpatterns = [
    path('store/', views.store_list, name='store_list'),
    path('category/<int:category_id>/', views.store_category, name='store_category'),
    path('food/<int:food_category_id>/', views.food_category, name='food_category'),
    path('store/<int:store_id>/', views.store_detail, name='store_detail'),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
]
