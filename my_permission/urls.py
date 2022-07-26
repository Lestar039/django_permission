from django.urls import path
from . import views


urlpatterns = [
    path('first', views.show_first_table, name='first'),
    path('second', views.show_second_table, name='second'),
    path('third', views.show_third_table, name='third'),
]

handler404 = "django_permission.views.page_not_found_view"
