from django.contrib import admin
from .models import Employer

@admin.register(Employer)
class EmployerAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'contact_person_name', 'email', 'phone_number', 'user')
    list_filter = ('created_at',)
    search_fields = ('company_name', 'contact_person_name', 'email', 'user__email')
    raw_id_fields = ('user',)