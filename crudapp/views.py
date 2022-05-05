from multiprocessing import context
from django.shortcuts import render,redirect
from django.views import View
from .models import NameList, BlogPost
from .forms import CreateNameListForm
from .tasks import update_verify
# Create your views here.


# Add item page 
class AddHomeView(View):
    template_name = 'index.html'
    
    def get(self, request, *args, **kwargs):
        context = {}
        update_verify(10)


        return render(request, self.template_name, context)

    # Post request 
    def post(self, request, *args, **kwargs):
        context = {}


        form = CreateNameListForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success'] = True
        


        return render(request, self.template_name, context)



# This view displays ever list and every status 
class ListItems(View):
    template_name = 'list.html'

    def get(self, request, *args, **kwargs):
        context = {}

        name_list = NameList.objects.all()
        context['name_list'] = name_list
        return render(request, self.template_name, context)


# This view displays ever list and every status 
class BlogView(View):
    template_name = 'blog.html'

    def get(self, request, *args, **kwargs):
        
        context = {}

        blog_post = BlogPost.objects.last()
        context['blog_post'] = blog_post
        return render(request, self.template_name, context)
