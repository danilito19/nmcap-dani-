from django.contrib import admin
from .models import Projects
# Register your models here.

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('idno', 'admin_agency', 'email', 'url', 'approp_title', 'fund_code', 'eligibility', 'category', 'subcategory', 'county', 'state_amount', 'amount_reauthorized', 'expended_amount_state', 'expended_amount_local', 'current_balance', 'current_balance_local', 'reversion_amount', 'local_fiscal_agent', 'project_phase', 'project_status', 'goal_milestone_last_quarter', 'goal_milestone_next_quarter', 'progress', 'reporter_notes', 'public_description', 'photo', 'sponsors', 'contractor_vendor', 'contractor_location','reporter_name', 'reporter_org')
    list_filter = ('county', 'category', 'admin_agency')
    search_fields = ('county', 'local_fiscal_agent')
admin.site.register(Projects, ProjectsAdmin)