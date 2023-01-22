from django.urls import path
from  .views import PostListView, PostDetailView, PostCreateView, PostUpdateView,PostDeleteView,ReservationCreateView,your_reservations,ReviewCreateView
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
]

