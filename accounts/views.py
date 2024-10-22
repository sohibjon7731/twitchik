from django.core.serializers import serialize
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, GenericAPIView, CreateAPIView, DestroyAPIView

from .serializers import UserSerializer, FollowSerializer
from rest_framework.response import Response
from .models import UserData, Follow
from rest_framework import status
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LogoutView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"status": "user is seccessfully logout"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UsersListView(ListAPIView):
    permission_classes = (IsAdminUser,)
    queryset = UserData.objects.all()
    serializer_class = UserSerializer


class CurrentUserView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        if request.user.is_authenticated:
            serializer = UserSerializer(request.user)
            return Response(serializer.data)
        else:
            return Response({"detail": "User is not authenticated"}, status=401)


class FollowUserView(CreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated, ]

    def post(self, request, *args, **kwargs):
        data = {
            'follower': request.user.id,
            'followed': kwargs['user_id']
        }
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UnfollowUserView(DestroyAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated, ]

    def delete(self, request, *args, **kwargs):
        follow = Follow.objects.filter(follower=request.user, followed_id=kwargs['user_id'])
        if follow.exists():
            follow.delete()
            return Response({"detail": "You have unfollowed this user"}, status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "You are not following this user"}, status=status.HTTP_400_BAD_REQUEST)


class ListFollowingView(ListAPIView):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return Follow.objects.filter(follower=self.request.user)


class ListFollowersView(ListAPIView):
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        return Follow.objects.filter(followed=self.request.user)
