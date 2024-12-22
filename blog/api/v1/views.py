
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from blog.api.v1.serializer import PostSerializer
from ...models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework import mixins


class PostList(GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    """ getting a list of post and creating new posts"""
    permission_classes =[IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    
    """ retrieving a list of posts"""
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
          
    """creating a post with provided data"""    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
# class PostList(ListCreateAPIView):
#     """ getting a list of post and creating new posts"""
#     permission_classes =[IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer
#     queryset = Post.objects.filter(status=True)


   
class PostDetail(GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    """ getting detail of the post and edit plus removing it"""
    permission_classes =[IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    # lookup_field = "id"
    """retrieving the post data"""
    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
     
    # """editing the post data"""
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    
    """ deleting the post object """
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)