from aldryn_apphooks_config.app_base import CMSConfigApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _
from .cms_appconfig import PollsApphookConfig

from django.urls import path
from . import views


@apphook_pool.register
class PollsApphookApp(CMSConfigApp):
    name = _("Polls App")
    app_name = "polls_app"
    app_config = PollsApphookConfig

    def get_urls(self, page=None, language=None, **kwargs):
        return [
            path('', views.single)
        ]
        # return ["polls.urls"]
