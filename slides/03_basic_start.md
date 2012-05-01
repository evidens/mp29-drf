# Simplest implementation

~~~ {#mycode .python .numberLines}
from djangorestframework.resources 
    import ModelResource
from blogpost.models import BlogPost

class BasicBlogPostResource(ModelResource):
    model = BlogPost
~~~

* Default behaviour: show everything

* Great for quick hacking

* Rather insecure
