from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .models import slider

context={
    'slider':slider.objects.all()
}
aa={
    'aa':'leee'
}
urlpatterns=[
    path('',views.home,name="home"),
    path('register/',views.Registerform,name="register"),
    path('login/',auth_views.LoginView.as_view(template_name="web/login.html"),aa,name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name="web/logout.html"),name="logout"),
    path('checkout/',views.checkout,name='checkout'),

]