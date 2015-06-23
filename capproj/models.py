from django.db import models

# Create your models here.
class Projects(models.Model):
    idno = models.CharField(max_length=10, blank=True, null=True)
    admin_agency = models.CharField(max_length=500, blank=True, null=True)
    email = models.CharField(max_length=500, blank=True, null=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    year = models.CharField(max_length=4)
    approp_title = models.CharField(max_length=500)
    fund_code = models.CharField(max_length=500, blank=True, null=True)
    eligibility = models.CharField(max_length=500, blank=True, null=True)
    bond_sale_date = models.CharField(max_length=500, blank=True, null=True)
    bond_series_number = models.CharField(max_length=500, blank=True, null=True)
    amount_of_bond = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=500, blank=True, null=True)
    subcategory = models.CharField(max_length=500, blank=True, null=True)
    county = models.CharField(max_length=500, blank=True, null=True)
    state_amount = models.IntegerField(blank=True, null=True)
    amount_reauthorized = models.IntegerField(blank=True, null=True)
    reversion_date = models.CharField(max_length=500, blank=True, null=True)
    valid_encumbrance = models.IntegerField(blank=True, null=True)
    expended_amount = models.IntegerField(blank=True, null=True)
    aipp_amount_bof = models.IntegerField(blank=True, null=True)
    reversion_amount = models.IntegerField(blank=True, null=True)
    appropriation_balance = models.IntegerField(blank=True, null=True)
    last_update = models.CharField(max_length=500, blank=True, null=True)
    icip_project_number = models.CharField(max_length=500, blank=True, null=True)
    icip_priority_number = models.CharField(max_length=500, blank=True, null=True)
    local_fiscal_agent = models.CharField(max_length=500, blank=True, null=True)
    amount_obligated = models.IntegerField(blank=True, null=True)
    project_end_date = models.CharField(max_length=500, blank=True, null=True)
    expended_amount_state = models.IntegerField(blank=True, null=True)
    aipp_amount = models.IntegerField(blank=True, null=True)
    reauth_of_balance_to_new = models.IntegerField(blank=True, null=True)
    reauth_to_project_number = models.CharField(max_length=500, blank=True, null=True)
    reversion_amount_two = models.IntegerField(blank=True, null=True)
    project_status = models.TextField(blank=True, null=True)
    goal_milestone_last_quarter = models.TextField(blank=True, null=True)
    goal_milestone_next_quarter = models.TextField(blank=True, null=True)
    project_phase = models.CharField(max_length=500, blank=True, null=True)
    current_balance = models.IntegerField(blank=True, null=True)
    last_agency_update = models.CharField(max_length=500, blank=True, null=True)
    last_submission_date = models.CharField(max_length=500, blank=True, null=True)
    expended_amount_local = models.IntegerField(blank=True, null=True)
    current_balance_local = models.IntegerField(blank=True, null=True)
    project_status_local = models.TextField(blank=True, null=True)
    goal_milestone_last_quarter_local = models.TextField(blank=True, null=True)
    goal_milestone_next_quarter_local = models.TextField(blank=True, null=True)
    valid_contracts_in_place = models.NullBooleanField()
    no_activity_for_month = models.NullBooleanField()
    last_submission_date_local = models.CharField(max_length=500, blank=True, null=True)
    last_update_local = models.CharField(max_length=500, blank=True, null=True)
    PROGRESS_CHOICES = (
                        ("C", "Completed"),
                        ("S", "Started"),
                        ("N", "Not started"),
                        ("P", "Partially completed"),
                        ("?", "Unclear")
                        )
    progress = models.CharField(
                                max_length=30,
                                choices = PROGRESS_CHOICES,
                                default='?'
                                )
    contractor_vendor = models.CharField(max_length=500, blank=True, null=True)
    contractor_location = models.CharField(max_length=500, blank=True, null=True)
    sponsors = models.CharField(max_length=1000, blank=True, null=True)
    reporter_notes = models.TextField(blank=True, null=True)
    public_description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to='media', blank=True, null=True)
    reporter_name = models.CharField(max_length=500, blank=True, null=True)
    reporter_org = models.CharField(max_length=500, blank=True, null=True)

