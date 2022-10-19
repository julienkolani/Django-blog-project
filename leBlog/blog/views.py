from django.shortcuts import render

# Create your views here.

from django.urls                    import reverse_lazy
from blog.models                    import blog
from django.shortcuts               import render
from django.views.generic           import ListView , CreateView ,UpdateView ,DetailView,DeleteView
from django.utils.decorators        import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

class blogHome(ListView):
    model = blog
    context_object_name = "posts"
    
    def get_queryset(self) :
        queryset = super().get_queryset()
        
        return queryset
    
    

class blogCreate(CreateView):
    model = blog
    fields = ['title','content',]
    success_url = reverse_lazy("blog:home")
    template_name = "blog/blog_create.html"
 
class blogUpdate(UpdateView):
    model= blog
    context_object_name = "post"
    fields = ['title','content','published']
    success_url = reverse_lazy("blog:home")
    template_name = "blog/blog_edit.html"
    
class blogDetail(DetailView):
    model = blog
    context_object_name = "post"
    
class blogDelete(DeleteView):
    model = blog
    context_object_name = "post"
    success_url = reverse_lazy("blog:home")
    
