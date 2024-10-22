from rest_framework import serializers
from .models import Post, Comment
from accounts.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'text', 'image', 'created_at', 'updated_at']
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']

    def create(self, validated_data):
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)


class CommentSerializer(serializers.ModelSerializer):
    post = PostSerializer(read_only=True)  
    post_id = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(),
                                                 write_only=True) 
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"

    def create(self, validated_data):

        post = validated_data.pop('post_id')

   
        validated_data['post'] = post
        validated_data['author'] = self.context['request'].user

      
        return super().create(validated_data)
