# Defining fields

~~~ {#mycode .python .numberLines}
class BlogPostResource(ModelResource):
    model = BlogPost
    fields = ('created', 'title', 'slug', 
              'content', 'url', 'comments')
~~~

* A tuple of the names of your desired fields
