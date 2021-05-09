from django.urls import path

from . import views


urlpatterns = [
    path('get/<str:file_format>/', views.GetMapItemsFileView.as_view()),
    path('cluster/<int:number>/<str:file_format>/', views.GetClusterFileView.as_view()),
    path("upload/", views.UploadImg.as_view()),

    path("view/<int:pk>/", views.ImgRetrieveView.as_view()),
    path("view/formated/<int:pk>/", views.FormatedImgRetrieveView.as_view()),
]