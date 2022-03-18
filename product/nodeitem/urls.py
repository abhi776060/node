
from django.urls import path
from . import views


urlpatterns = [
    path('node/login',views.login,name='login' ),
    path('node/logout',views.logout,name='logout' ),
    path('node/mobile_items',views.mobile_item,name='mobile_items' ),
    path('node/mobile_items/<str:pk>',views.mobile_detail,name='mobile_detail' ),
    path('node/laptop_items',views.laptop_item,name='mobile_items' ),
    path('node/laptop_items/<str:pk>',views.laptop_detail,name='mobile_detail' ),
  
   

]
