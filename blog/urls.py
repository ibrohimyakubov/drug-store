from django.urls import path
from rest_framework import routers
from blog import views
from blog.views import CommentsOfPostsView

router = routers.SimpleRouter()
router.register('comments', CommentsOfPostsView)

urlpatterns = router.urls + [
    path('create/', views.blog_create, name='blog-create'),
    path('update/<int:pk>/', views.blog_update, name='blog-update'),
    path('delete/<int:pk>/', views.blog_delete, name='blog-delete'),
    path('get-post/<int:pk>/', views.get_post, name='get-post'),
]
