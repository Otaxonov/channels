from django.urls import path
from gs4 import views

urlpatterns = [
    path('<str:group_name>/', views.index_view, name="gs2_index")
]