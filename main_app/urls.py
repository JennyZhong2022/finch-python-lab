from django.urls import path
from . import views

urlpatterns=[
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('finches/',views.finches_index,name='index'),
  path('finches/<int:finch_id>',views.finches_detail, name='detail'),
  path('finches/create', views.FinchCreate.as_view(), name='finches_create'),
  # pk=finch_id
  path('finches/<int:pk>/update', views.FinchUpdate.as_view(), name='finches_update'),
  path('finches/<int:pk>/delete', views.FinchDelete.as_view(), name='finches_delete'),
  path('finches/<int:finch_id>/add_feeding',views.add_feeding, name='add_feeding'),

  path('finches/<int:finch_id>/assoc_travel/<int:travel_id>',views.assoc_travel, name='assoc_travel'),
  path('finches/<int:finch_id>/assoc_travel_remove/<int:travel_id>',views.assoc_travel_remove, name='assoc_travel_remove'),

  path('travel/',views.TravelList.as_view(),name='travel_index'),
  path('travel/<int:pk>',views.TravelDetail.as_view(),name='travel_detail'),
  path('travel/create',views.TravelCreate.as_view(),name='travel_create'),
  path('travel/<int:pk>/update',views.TravelUpdate.as_view(),name='travel_update'),
  path('travel/<int:pk>/delete',views.TravelDelete.as_view(),name='travel_delete'),
  


]