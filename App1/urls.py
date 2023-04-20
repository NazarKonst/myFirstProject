from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello),
    path('about/', views.about),
    path('item/<int:id_num>/', views.fu_item),
    path('items/', views.fu_items),
]
