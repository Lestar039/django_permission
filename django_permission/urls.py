from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('my_permission/', include('my_permission.urls')),
]
