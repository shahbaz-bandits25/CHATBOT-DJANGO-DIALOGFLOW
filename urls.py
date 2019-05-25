from django.urls import path
from .views import inp_msg

app_name = "mydoc"

urlpatterns = [
    path('', inp_msg),
]