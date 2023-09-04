from django.urls import path
from gs5 import views

urlpatterns = [
    path('', views.index_view, name="gs5_index")
]