from drf_yasg import openapi


def get_post_id():
    user_id = openapi.Parameter('post_id', openapi.IN_QUERY,
                                description='post id ni kiriting',
                                type=openapi.TYPE_INTEGER)
    return [user_id]
