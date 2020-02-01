from aldryn_apphooks_config.app_base import CMSConfigApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _
from .cms_appconfig import FaqConfig


@apphook_pool.register
class FaqApp(CMSConfigApp):
    name = _("Faq App")
    app_name = "faq"
    app_config = FaqConfig

    def get_urls(self, page=None, language=None, **kwargs):
        return ["faq.urls"]
