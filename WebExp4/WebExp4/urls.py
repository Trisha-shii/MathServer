from django.contrib import admin
from django.urls import path
from gst_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.gst_amt_calculator, name='gst_amt'),
]
