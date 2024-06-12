from django.urls import path
from . import views
from carmart.views import home
urlpatterns = [
    path('buy/<int:id>',views.buy,name='buy'),
    path('details/<int:id>',views.details,name='details'),
    path('brand/<slug:category_slug>',home,name='brand'),
]
