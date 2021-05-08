from django.urls import path

from . import views


urlpatterns = [
    path('start/', views.StartCrawlerView.as_view()),
    path('news/', views.NewsList.as_view({'get': 'list'})),
    path('news/<int:pk>/', views.NewsList.as_view({'get': 'retrieve'})),
]