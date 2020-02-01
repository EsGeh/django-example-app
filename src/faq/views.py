from aldryn_apphooks_config.mixins import AppConfigMixin
from django.views import generic
from .models import Entry


class IndexView(AppConfigMixin, generic.ListView):
    model = Entry
    template_name = 'faq/index.html'

    def get_queryset(self):
        qs = super(IndexView, self).get_queryset()
        return qs.namespace(self.namespace)

    def get_paginate_by(self, queryset):
        try:
            return self.config.paginate_by
        except AttributeError:
            return 10
