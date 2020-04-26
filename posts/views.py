from django.shortcuts import render
from .serializers import *
from authors.models import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

# Create your views here.

class PostView(APIView):
    permission_classes = [IsAuthenticated, ]
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            post = Post()
            post.author = Author.objects.get(user=request.user)
            post.title = request.data.get('title')
            post.content = request.data.get('content')
            post.save()
            return Response({'detail': 'The post has successfully been saved.'}, status=201)
        else:
            return Response(serializer.errors, status=400)