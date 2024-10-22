from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import PostSerializer, CommentSerializer
from rest_framework.exceptions import NotAuthenticated, PermissionDenied
from .models import Post, Comment
from .permissions import IsAuthorOrReadOnly


class PostsAllView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny, ]


class PostsCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        if self.request.user.is_anonymous:
            raise NotAuthenticated("Foydalanuvchi tizimga kirmagan.")

        serializer.save(author=self.request.user)


class PostsSingleView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AllowAny, ]
    lookup_field = 'pk'


class PostsUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly, ]


class PostsDestroyView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly, ]


class CommentsAllView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny, ]


class CommentsCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        if self.request.user.is_anonymous:
            raise NotAuthenticated("Foydalanuvchi tizimga kirmagan.")

        serializer.save(author=self.request.user)


class CommentsSingleView(generics.RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny, ]
    lookup_field = 'pk'


class CommentsUpdateView(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly, ]


class CommentsDestroyView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly, ]
