from django.contrib import admin
from django.urls import path
from phoneinfo import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin page URL
    path('', views.phone_info, name='phone_info'),  # Root URL mapped to the phone_info view
]
