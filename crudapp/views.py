from django.shortcuts import render,redirect
from django.views import View

# Create your views here.


# Add item page 
class AddHomeView(View):
    template_name = 'index.html'
    
    def get(self, request, *args, **kwargs):
        context = {}


        return render(request, self.template_name, context)

    # Post request 
    def get(self, request, *args, **kwargs):
        context = {}


        return render(request, self.template_name, context)



# This view displays ever list and every status 
class ListItems(View):
    template_name = 'list.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
