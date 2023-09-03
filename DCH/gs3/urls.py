from django.urls import path
from gs3 import views

urlpatterns = [
    path('', views.index_view, name="gs3_index")
]