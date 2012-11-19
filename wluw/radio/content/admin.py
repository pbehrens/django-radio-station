from django.core.urlresolvers import reverse
from radio.content.models import Post
from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE



class TinyMCETestPageAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ('post'):
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30},
                mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list')},
            ))
        return super(TinyMCETestPageAdmin, self).formfield_for_dbfield(db_field, **kwargs)

    
    
admin.site.register(Post, TinyMCETestPageAdmin)
