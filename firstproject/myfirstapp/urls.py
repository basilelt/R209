from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('index/', views.index),
    path('admin/', admin.site.urls),
    path('myfirstapp/', include('myfirstapp.urls'))
]