from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # search
    path('search/', views.search, name='search'),
    # student route
    path('students/', views.students, name='students'),
    path('students/<int:student_id>/', views.studentDetail, name='studentDetail'),
    path('students/<int:student_id>/ratings/', views.studentRatings, name='studentRatings'),
    # item route
    path('items/', views.items, name='items'),
    path('items/<int:item_id>/', views.itemDetail, name='itemDetail'),
    path('items/<int:item_id>/ratings/', views.itemRatings, name='itemRatings'),
    # rating route
    path('ratings/', views.ratings, name='ratings'),
    path('ratings/<int:rating_id>/', views.ratingDetail, name='ratingDetail'),
    path('ratings/<int:student_id>/<int:item_id>/rate/', views.rate, name='rate'),
    # machinelearning training tf routes
    # todo
]