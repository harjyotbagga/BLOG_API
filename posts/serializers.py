from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'timestamp']
    # def create(self, validated_data):
    #     author = request.user.pk
    #     return Post.objects.create(author=author)