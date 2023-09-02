from django.urls import path
from gs1 import views

urlpatterns = [
    path('', views.index_view, name="gs1_index")
]