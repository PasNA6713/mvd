from django.urls import path

from . import views


urlpatterns = [
    path("", views.MapItemListView.as_view()),
    path("<int:pk>/", views.MapItemRetrieveView.as_view()),
    path("some/", views.GetSomeMapItems.as_view()),
    path('range/',views.GetRangeMapItems.as_view()),

    path("create/", views.MapItemCreateView.as_view()),
    path("destroy/<int:pk>/", views.MapItemDestroyView.as_view()),
   
    path('plot-diagram/<str:column>/', views.DiagramPlotView.as_view()),
    path('plot-bar/', views.BarPlotView.as_view()),
    
    path('get-filter-params/', views.GetFilterParams.as_view()),
]