from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:id>', views.cust_rec, name='rec'),
    path('delete_rec/<int:id>', views.delete_rec, name='dele_rec'),
    path('add_rec/', views.add_rec, name='add_rec'),
    # path('update_rec/', views.update_rec, name='update_rec'),
    path('update/<int:pk>', views.update_rec, name='update_record'),

]