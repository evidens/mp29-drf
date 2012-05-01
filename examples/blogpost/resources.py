from django.core.urlresolvers import reverse
from djangorestframework.resources import ModelResource
from blogpost.models import BlogPost, Comment
from django.contrib.auth.models import User

class BasicBlogPostResource(ModelResource):
    model = BlogPost

class AuthorResource(ModelResource):
    model = User
    fields = ('username', 'email')

class BlogPostResource(ModelResource):
    """
    A Blog Post has a *title* and *content*, and can be associated with zero or more comments.
    """
    model = BlogPost
    fields = ('created', 'title', ('author', AuthorResource), 'slug', 'content', 'url', 'comments')
    ordering = ('-created',)

    def comments(self, instance):
        return reverse('comments', kwargs={'blogpost': instance.key})

class CommentResource(ModelResource):
    """
    A Comment is associated with a given Blog Post and has a *username* and *comment*, and optionally a *rating*.
    """
    model = Comment
    fields = ('username', 'comment', 'created', 'rating', 'url', 'blogpost')
    ordering = ('-created',)

    def blogpost(self, instance):
        return reverse('blog-post', kwargs={'key': instance.blogpost.key})
