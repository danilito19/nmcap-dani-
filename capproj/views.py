from django.shortcuts import render
from .models import Projects
from django_tables2   import RequestConfig
from .tables  import ProjectsTable
from django.template import RequestContext
from django.shortcuts import render_to_response

# Create your views here.

def projects(request):
	projects = ProjectsTable(Projects.objects.all().defer('email'))
	RequestConfig(request, paginate={"per_page": 100}).configure(projects)
	return render(request, "base.html", {"projects": projects})

def search(request):
  if 'q' in request.GET and request.GET['q']:
      q = request.GET['q']
      # import pdb; pdb.set_trace()
      results = Projects.objects.filter(approp_title__contains=q)
      results_table = ProjectsTable(results.defer('email'))
      RequestConfig(request, paginate={"per_page": 100}).configure(results_table)
      return render(request, 'results.html', 
          {'results_table': results_table, 'q': q})