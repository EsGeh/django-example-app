from django.contrib import admin
from .cms_appconfig import FaqConfig
from .models import Entry
from aldryn_apphooks_config.admin import ModelAppHookConfig, BaseAppHookConfig

class EntryAdmin(ModelAppHookConfig, admin.ModelAdmin):
    list_display = (
        'question',
        'answer',
        'app_config',
    )
    list_filter = (
        'app_config',
    )
admin.site.register(Entry, EntryAdmin)


class FaqConfigAdmin(BaseAppHookConfig, admin.ModelAdmin):
    def get_config_fields(self):
        return (
            'paginate_by',
            'config.title',
        )
admin.site.register(FaqConfig, FaqConfigAdmin)
