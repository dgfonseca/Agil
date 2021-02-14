from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'deportistas/', views.deportistas, name="deportistas"),
    url(r'^add/$', views.add_deportista, name='addDeportista'),
    url(r'^addUser/$', views.add_user_view, name="addUser"),
    url(r'^registerUser', views.add_user, name="registrarUsuario"),
    url(r'login/$', views.login_view, name='login'),
    url(r'^loginUser', views.login_user, name='loginUser'),
    url(r'^logout/$', views.logout_view, name='logout'),
]