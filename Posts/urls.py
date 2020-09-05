from django.urls import path
from Posts import views


urlpatterns = [
    path('create', views.create , name='create'),
    path('<int:post_id>', views.details , name='details'),
    path('<int:post_id>/upvote', views.upvote , name='upvote'),

]