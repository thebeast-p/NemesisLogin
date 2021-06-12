from django.urls import path
from . import views

urlpatterns = [
    path('',views.login, name="Login" ),
    path('check',views.check, name="Submit" ),
    #path('retry',views.retry, name="Submit" ),
    path('signup',views.signup, name="Signup" ),
    path('details',views.display, name="Display" )
]
