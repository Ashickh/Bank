from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('add/', views.person_create_view, name='person_add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),
    path('ajax/load-cities/', views.load_branches, name='ajax_load_branches'),

]