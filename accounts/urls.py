from django.urls import path 
from . import views 

urlpatterns=[
    path('signup/',views.registrationView.as_view(),name='registration'),
    path('login/',views.loginView.as_view(),name='login'),
    path('change/',views.change_pass,name='change'),
    path('change2/',views.change_pass2,name='change2'),
    path('logout/',views.logoutview.as_view(),name='logout'),
    path('profile/',views.profile,name='profile'),
    path('edit/<int:id>',views.update,name='update'),
]