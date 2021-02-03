from django.contrib import admin
from . models import mentors,m_team,main_project,related_project,all_research,all_blog,contact
# Register your models here.
admin.site.register(mentors)
admin.site.register(m_team)
admin.site.register(main_project)
admin.site.register(related_project)
admin.site.register(all_research)
admin.site.register(all_blog)
admin.site.register(contact)