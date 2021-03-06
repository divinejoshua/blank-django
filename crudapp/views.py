from multiprocessing import context
from django.shortcuts import render,redirect
from django.views import View
from .models import NameList, BlogPost, NumberGuess
from .forms import CreateNameListForm

# The background task 
from .tasks import update_verify

# For caching
from django.core.cache import cache

# Create your views here.


# Add item page 
class AddHomeView(View):
    template_name = 'index.html'
    
    def get(self, request, *args, **kwargs):
        context = {}
        
        return render(request, self.template_name, context)

    # Post request 
    def post(self, request, *args, **kwargs):
        context = {}


        form = CreateNameListForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()

            # Get instance ID 
            instance = NameList.objects.last()
            key = instance.pk
            update_verify.delay(key)

            context['success'] = True
        


        return render(request, self.template_name, context)

    

# This view displays ever list and every status 
class ListItems(View):
    template_name = 'list.html'

    def get(self, request, *args, **kwargs):
        context = {}

        name_list = NameList.objects.all().order_by('-id')
        context['name_list'] = name_list
        return render(request, self.template_name, context)


# This view displays ever list and every status 
class BlogView(View):
    template_name = 'blog.html'

    def get(self, request, *args, **kwargs):
        
        context = {}


        # check if cache exist
        if cache.get('cached_blog_post'):
                context['blog_post'] = cache.get('cached_blog_post')
        else:
            # Get the value from the database 
            blog_post = BlogPost.objects.last()
            
             # Setting the cache 
            # cache.set(key, value, timeout=DEFAULT_TIMEOUT in seconds)
            cache.set('cached_blog_post', blog_post, 20)
            context['blog_post'] = blog_post
            
        return render(request, self.template_name, context)




# This view displays a list of numbers added to the database at a certain time (Celery beat)
class NumberView(View):
    template_name = 'numbers.html'

    def get(self, request, *args, **kwargs):
        
        context = {}
        number_list = NumberGuess.objects.all().order_by('-id')
        context['numberlist'] = number_list
        return render(request, self.template_name, context)