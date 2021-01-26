from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from .views import HomePageView

urlpatterns=[
    path('',views.post_list, name='post_list'),
    path('post/<int:pk>/',views.post_detail,name='post_detail'),
    path('', HomePageView.as_view(), name='home'),
]