from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('template/',views.template, name='template'),
	path('contact/',views.contact, name='contact'),
	path('stores/',views.stores, name='stores'),
	path('listNewStore/', views.List_New_Store, name="listNew"),
	path('howitworks/', views.howitworks, name="howitworks"),
	path('article/', views.article, name="article"),
	path('store/<int:store_id>/', views.storeDetails, name='storeDetails')
]