# Nesting resources

~~~ {#mycode .python .numberLines}
from django.contrib.auth.models import User 

class AuthorResource(ModelResource):
    model = User
    fields = ('username', 'email')

class BlogPostResource(ModelResource):
    model = BlogPost
    fields = (..., 
              ('author', AuthorResource),
              ...)
~~~

* Define your resource

* Instead of string, give a tuple of (name, ResourceClass)
