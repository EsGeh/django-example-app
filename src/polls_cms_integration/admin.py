from django.contrib import admin
from .cms_appconfig import PollsApphookConfig
# from .models import PollsApphookModel
from aldryn_apphooks_config.admin import ModelAppHookConfig, BaseAppHookConfig


'''
class PollsApphookAdmin(ModelAppHookConfig, admin.ModelAdmin):
    list_display = (
        'poll',
        'app_config',
    )
admin.site.register(PollsApphookModel, PollsApphookAdmin)
'''


class PollsApphookConfigAdmin(BaseAppHookConfig, admin.ModelAdmin):
    def get_config_fields(self):
        return (
            'poll',
        )
admin.site.register(PollsApphookConfig, PollsApphookConfigAdmin)
