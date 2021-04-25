from django.urls import path

from . import views


urlpatterns = [
    path('<str:file_format>/', views.GetMapItemsFileView.as_view()),
    path('cluster/<int:number>/<str:file_format>/', views.GetClusterFileView.as_view()),
    # path("upload/", views.UploadFileView.as_view()),
    # path("get/", views.CreateFileView.as_view()),
    # path("get/<int:key>/<str:file_format>/", views.DownloadFileView.as_view()),
]