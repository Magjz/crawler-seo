#crawler/views.py

from django.shortcuts import render, redirect
from crawler.models import Project
from django.views.generic.edit import ProcessFormView
from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from crawler.forms import ProjectForm
import datetime



@method_decorator(login_required, name='dispatch')
class Project(ListView): 
    template_name = "core/pages/project.html"

    def get(self, request): 
        form = ProjectForm()
        projects = Project.objects.all()
        
        return render(request, self.template_name, {'form' : form})
    
    def post(self, request): 
        form = ProjectForm(request.POST)
        if form.is_valid(): 
            post            = form.save(commit=False)
            name            = form.cleaned_data['name']
            domain          = form.cleaned_data['domain']
            post.user_id    = request.user.id
            post.created_at = datetime.datetime.now()
            post.save()
            form = ProjectForm()
        
            return redirect('projet')

        args = {'form' : form}
        return render(request, self.template_name, args)



class ProjectDetail(TemplateView):
    pass

@method_decorator(login_required, name='dispatch')
class Crawler(TemplateView):
    template_name = "core/pages/param-crawl.html"

@method_decorator(login_required, name='dispatch')
class CrawlerDetail(TemplateView):
    template_name = "core/pages/param-crawl.html"
    