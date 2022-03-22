from django.urls import path
from . import views

urlpatterns = [
    path('',views.CovidListCreateAPIView.as_view(),name="data-list"),
    path('<int:pk>/',views.CovidDetailAPIView.as_view(),name="data-detail"),
    path('<int:pk>/update',views.CovidUpdateAPIView.as_view(),name="edit-data-detail"),
    path('<int:pk>/delete',views.CovidDestroyAPIView.as_view()),
] 