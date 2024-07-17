from django.contrib import admin
from django.urls import path
from .views import HomeViewPage,BookListViewPage,BookDetailsViewPage

urlpatterns = [
    path('',HomeViewPage.as_view(),name='Home'),
    path('book',BookListViewPage.as_view(),name='Book'),
    path('<int:pk>',BookDetailsViewPage.as_view(),name='Book_detals'),
   
]
