from django.contrib.auth.models import User
from django.db import models
from user.models import Adminstrator


class Blog(models.Model):
    STATUS = (
        ('True', 'Have'),
        ('False', 'Have not'),
    )
    title = models.CharField(max_length=222, unique=True)  # trans
    description = models.TextField(blank=True)  # trans
    image = models.ImageField(upload_to='images/', blank=True)
    slug = models.SlugField(null=False, unique=True)
    status = models.CharField(max_length=10, choices=STATUS)
    # likes = models.ManyToManyField(User, blank=True, related_name='blog_posts')
    post_view = models.IntegerField(default=0, null=True, blank=True)

    author = models.ForeignKey(Adminstrator, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-create_at',)
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'

    # def total_likes(self):
    #     return self.likes.count()
    #
    # @property
    # def get_products(self):
    #     return Post.objects.filter(categories__title=self.title)
    #
    def __str__(self):
        return self.title
    #
    # def image_tag(self):
    #     return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    #
    # image_tag.short_description = 'Image'
    #
    # def avaregereview(self):
    #     reviews = Comment.objects.filter(post=self, status='True').aggregate(avarage=Avg('rate'))
    #     avg = 0
    #     if reviews["avarage"] is not None:
    #         avg = float(reviews["avarage"])
    #     return avg
    #
    # def countreview(self):
    #     reviews = Comment.objects.filter(post=self, status='True').aggregate(count=Count('id'))
    #     cnt = 0
    #     if reviews["count"] is not None:
    #         cnt = int(reviews["count"])
    #     return cnt


class CommentOfPost(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comment')
    parent = models.ForeignKey(
        'self', verbose_name="Parents", on_delete=models.SET_NULL, blank=True, null=True, related_name="children")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(null=True, blank=True, max_length=255)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        full_name = self.owner.username
        # return full_name if full_name else self.owner.username
        if full_name:
            return full_name
        else:
            return self.owner.username

# class Comment(models.Model):
#     STATUS = (
#         ('True', 'Mavjud'),
#         ('False', 'Mavjud Emas'),
#     )
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
#     user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profiles')
#     email = models.EmailField()
#     subject = models.CharField(max_length=55, blank=True)  # trans
#     comment = models.TextField(max_length=255, blank=True)  # trans
#     active = models.BooleanField(default=True)
#     ip = models.CharField(max_length=20, blank=True)
#     status = models.CharField(max_length=15, choices=STATUS, default='True')
#     create_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return 'Comment {} by {}'.format(self.comment, self.user)
#
