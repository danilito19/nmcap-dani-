from django.shortcuts import render
from .models import Projects
from django_tables2   import RequestConfig
from .tables  import ProjectsTable
from django.template import RequestContext
from django.shortcuts import render_to_response


years = Projects.objects.values_list('year').distinct()
counties = Projects.objects.values_list('county').distinct()


def pretty_results(input_array):
  final = []
  for i in input_array:
    for string in i:
      final.append(string)
  return final


def projects(request):
  projects = ProjectsTable(Projects.objects.all().defer('email'))
  RequestConfig(request, paginate={"per_page": 100}).configure(projects)
  return render(request, "projects.html", {"projects": projects, 'years':
           pretty_results(years), 'counties': pretty_results(counties),
           'searchPath': request.build_absolute_uri()})

def search(request):
  searchVectors = ['q', 'year', 'county', 'expended_amount']
  for i in searchVectors:
    if i in request.GET and request.GET[i]:

      # import pdb; pdb.set_trace()
      kwargs = {}

      project_name = request.GET.get('q', None)
      if project_name:
        kwargs['approp_title__contains'] = project_name
      # kwargs = {
      #   'approp_title__contains': request.GET.get('q')
      # }

      year = request.GET.get('year', None)
      if year:
        kwargs['year'] = year

      county = request.GET.get('county', None)
      if county:
        kwargs['county'] = county

      expended_amount = request.GET.get('expended_amount', None)
      if expended_amount:
        kwargs['expended_amount'] = expended_amount

      results = Projects.objects.filter(**kwargs)
      results_table = ProjectsTable(results.defer('email'))
      RequestConfig(request, paginate={"per_page": 100}).configure(results_table)
      

      return render(request, 'results.html', 
          {'projects': results_table, 'query': request.GET.get('q'), 'years':
           pretty_results(years), 'counties': pretty_results(counties),
           'searchPath': request.get_full_path(), 'basePath': request.build_absolute_uri('/')})


      break
  # if 'q' in request.GET and request.GET['q']:
