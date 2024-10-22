from django.urls import path, include

from .views import PostsAllView, PostsCreateView, PostsDestroyView, PostsSingleView, PostsUpdateView, CommentsAllView, \
    CommentsCreateView, CommentsSingleView, CommentsUpdateView, CommentsDestroyView

urlpatterns = [
    path('posts', PostsAllView.as_view(), name='posts'),
    path('post/create', PostsCreateView.as_view(), name='post-create'),
    path('post/<int:pk>', PostsSingleView.as_view(), name='post-single'),
    path('post/<int:pk>/update', PostsUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostsDestroyView.as_view(), name='post-delete'),

    path('comments', CommentsAllView.as_view(), name='comments'),
    path('comment/create', CommentsCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>', CommentsSingleView.as_view(), name='comment-single'),
    path('comment/<int:pk>/update', CommentsUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete', CommentsDestroyView.as_view(), name='comment-delete'),
]
