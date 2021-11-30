from django.urls import path
from . import views

# localhost:8000/
urlpatterns = [
# localhost:8000/
     path('', views.Home.as_view(), name="home"),
# localhost:8000/about/
     path('about/', views.about, name="about"),
# localhost:8000/forums/
     path('forums/', views.forums_index, name='forums_index'), 
# localhost:8000/forums/:forum_id
     path('forums/<int:forum_id>/', views.forums_detail, name='forums_detail'),
# localhost:8000/forums/create
     path('forums/create/', views.ForumCreate.as_view(), name='forums_create'),
# localhost:8000/forums/:pk/update
     path('forums/<int:pk>/update', views.ForumUpdate.as_view(), name="forums_update"),
# localhost:8000/forums/:pk/delete
     path('forums/<int:pk>/delete', views.ForumDelete.as_view(), name="forums_delete"),
# localhost:8000/forums/:forum_id/add_post/
     path('forums/<int:forum_id>/add_posts/', views.add_posts, name="add_posts"),
     path('posts/create/', views.PostCreate.as_view(), name='posts_create'),
     path('posts/<int:pk>/', views.PostDetail.as_view(), name='posts_detail'),
     path('posts/', views.PostList.as_view(), name='posts_index'),
     path('posts/<int:pk>/update/', views.PostUpdate.as_view(), name='posts_update'),
     path('posts/<int:pk>/delete/', views.PostDelete.as_view(), name='posts_delete'),
     path("accounts/signup/", views.signup, name="signup")

]
