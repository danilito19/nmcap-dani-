import django_tables2 as tables
from .models import Projects

class ProjectsTable(tables.Table):
	approp_title = tables.Column(verbose_name= 'Project Name')
	year = tables.Column(verbose_name= 'Year')
	county = tables.Column(verbose_name= 'County')
	state_amount = tables.Column(verbose_name= 'State Amount Budgeted')
	expended_amount_state = tables.Column(verbose_name= 'State Expended Amount')
	amount_reauthorized = tables.Column(verbose_name= 'Amount Reauthorized')
	current_balance = tables.Column(verbose_name= 'Current Balance')


	class Meta:
		model = Projects
		fields = ('approp_title', 'year', 'county', 'state_amount', 'expended_amount_state', 'current_balance','amount_reauthorized',) # fields to display

		        # for CSS tags
		attrs = {"class": "table"}

class ResultsTable(tables.Table):
	approp_title = tables.Column(verbose_name= 'Project Name')
	year = tables.Column(verbose_name= 'Year')
	county = tables.Column(verbose_name= 'County')
	state_amount = tables.Column(verbose_name= 'State Amount Budgeted')
	expended_amount_state = tables.Column(verbose_name= 'State Expended Amount')
	amount_reauthorized = tables.Column(verbose_name= 'Amount Reauthorized')
	current_balance = tables.Column(verbose_name= 'Current Balance')


	class Meta:
		model = Projects
		fields = ('approp_title', 'year', 'county', 'state_amount', 'expended_amount_state', 'current_balance','amount_reauthorized',) # fields to display

		        # for CSS tags
		attrs = {"class": "table"}
