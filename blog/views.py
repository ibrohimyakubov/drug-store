from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from user.models import Adminstrator
from . import filter_params
from .models import Blog, CommentOfPost
from .serializers import BlogSerializer, CommentsOfPostsRecursiveSerializer


@api_view(['POST'])
@permission_classes((IsAdminUser,))
def blog_create(request):
    admin = Adminstrator.objects.get(user=request.user)
    blog = Blog(author=admin)

    if request.method == 'POST':
        serializer = BlogSerializer(blog, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'blog has created successfully'
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes((IsAdminUser,))
def blog_update(request, pk):
    try:
        blog = Blog.objects.get(id=pk)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = BlogSerializer(blog, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'Blog has updated successfully'
            return Response(data=data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes((IsAdminUser,))
def blog_delete(request, pk):
    try:
        admin = Adminstrator.objects.get(user=request.user)
        blog = Blog.objects.get(id=pk)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    except Adminstrator.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        if admin:
            operation = blog.delete()
            data = {}
            if operation:
                data['success'] = 'delete successfully'
            else:
                data['failure'] = 'fail deleted blog'
            return Response(data=data)
        elif admin.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CommentsOfPostsView(ModelViewSet):
    queryset = CommentOfPost.objects.all()
    serializer_class = CommentsOfPostsRecursiveSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = super(CommentsOfPostsView, self).get_queryset()
        query_params = self.request.query_params
        post_id = query_params.get("post_id")
        if post_id:
            queryset = queryset.filter(owner__id=post_id)
            queryset = queryset.filter(parent=None)
            return queryset
        return queryset

    def get_serializer_context(self):
        return {'request': self.request}

    @swagger_auto_schema(manual_parameters=filter_params.get_post_id())
    def list(self, request, *args, **kwargs):
        return super(CommentsOfPostsView, self).list(kwargs)


@api_view(['GET'])
def get_post(request, pk):
    if request.method == 'GET':
        comment = CommentOfPost.objects.filter(post_id=pk)
        serializer = CommentsOfPostsRecursiveSerializer(comment, context={'request': request}, many=True)
        return Response(serializer.data)
