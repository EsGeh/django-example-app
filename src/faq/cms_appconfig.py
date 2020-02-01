from aldryn_apphooks_config.models import AppHookConfig
from aldryn_apphooks_config.utils import setup_config
from app_data import AppDataForm
from django.db import models
from django import forms
from django.utils.translation import ugettext_lazy as _


class FaqConfig(AppHookConfig):
    paginate_by = models.PositiveIntegerField(
        _('Paginate size'),
        blank=False,
        default=5,
    )


class FaqConfigForm(AppDataForm):
    title = forms.CharField()
setup_config(FaqConfigForm, FaqConfig)
