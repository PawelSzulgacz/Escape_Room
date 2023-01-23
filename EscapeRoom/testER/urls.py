from django.urls import path
from  .views import *
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='Escape_Room_app'),
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('new', PostCreateView.as_view(), name='post-form-room'),
    path('<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('<int:pk>/reservation/new', views.ReservationCreateView.as_view(), name='add_reservation'),
    path('reservations/', views.your_reservations, name='reservations'),
    path('<int:pk>/review/new', ReviewCreateView.as_view(), name='make-review'),
    path('company/new', ErCreateView.as_view(), name='add-er'),
    path('company/<int:pk>/delete', ErDeleteView.as_view(), name='er-delete'),
    path('company/<int:pk>/update', ErUpdateView.as_view(), name='er-update'),
    path('companies/yours', views.your_er, name='yours-er'),
    path('companies', erListView.as_view(), name='all-er'),
    path('company/<int:pker>/rooms', rooms_from_company, name='er-rooms'),
    path('search', search_room, name='search-room'),
]

