from django.urls import path
from . import views

# localhost:8000/
urlpatterns = [
    # localhost:8000/
    path('', views.home, name="home"),
    # localhost:8000/about/
    path('about/', views.about, name="about"),
    # localhost:8000/forums/
    path('forums/', views.Forums_index, name='forums_index'),
    # localhost:8000/forums/:forum_id
    path('forums/<int:forum_id>/', views.Forums_detail, name='forums_detail'),
    # localhost:8000/forums/create
    path('forums/create/', views.ForumCreate.as_view(), name='forums_create'),
    # localhost:8000/forums/:pk/update
    path('forums/<int:pk>/update', views.ForumUpdate.as_view(), name="forums_update"),
    # localhost:8000/forums/:pk/delete
    path('forums/<int:pk>/delete', views.ForumDelete.as_view(), name="forums_delete"),
    # localhost:8000/forums/:forum_id/add_post/
    path('forums/<int:forum_id>/add_posts/',
         views.add_posts, name="add_posts"),

]
