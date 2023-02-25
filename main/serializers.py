from rest_framework import serializers
from rest_framework.serializers import HyperlinkedIdentityField
from .models import Comment

class CommentListSerializer(serializers.ModelSerializer):
    url = HyperlinkedIdentityField(view_name='comment-view')
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Comment
        fields = ['id', 'name', 'email', 'image', 'url', 'created_at']

    def create(self, validated_data):
        image = validated_data.pop('image', None)
        comment = Comment.objects.create(**validated_data)
        
        if image:
            comment.image = image
            comment.save()

        return comment

class CommentDetailSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Comment
        fields = ['id', 'name', 'email', 'content', 'image', 'created_at']

class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['name', 'email', 'content', 'image']

class CommentUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['name', 'email', 'content', 'image']

class CommentDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id']

class CommentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'image']