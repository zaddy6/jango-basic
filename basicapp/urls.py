from django.urls import path
from basicapp import views


app_name = 'matics_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('formpage/', views.form_view, name='form')
]