from rest_framework import serializers

from .models import Blog, CommentOfPost


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        exclude = ['author']


def recursive_comment_of_post(parent, request) -> list:
    data = []
    if len(parent) > 0:
        for i in parent:
            data.append(CommentsOfPostsRecursiveSerializer(instance=i, context={'request': request}).data)
            if i.children.all():
                if len(recursive_comment_of_post(i.children.filter(parent=None), request)) > 0:
                    for j in recursive_comment_of_post(i.children.filter(parent=None), request):
                        data.append(j)
    return data


class CommentsOfPostsRecursiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentOfPost
        fields = "__all__"

    def to_representation(self, instance):
        request = self.context['request']
        data = super(CommentsOfPostsRecursiveSerializer, self).to_representation(instance)
        data['replies'] = recursive_comment_of_post(instance.children.all().order_by("-created_at"),
                                                    request) if instance.children.all() else []
        return data



