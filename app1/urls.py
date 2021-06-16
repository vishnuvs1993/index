from django.urls import path,include
from . import views

urlpatterns = [
    path('helo',views.hello),

    path('hii',views.hi),
    path('fun',views.sample)
]
