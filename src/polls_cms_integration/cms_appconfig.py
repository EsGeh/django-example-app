from polls.models import Question
from aldryn_apphooks_config.models import AppHookConfig
from aldryn_apphooks_config.utils import setup_config
from app_data import AppDataForm
from django.db import models
from django import forms
from django.utils.translation import ugettext_lazy as _


class PollsApphookConfig(AppHookConfig):
    poll = models.ForeignKey(Question, on_delete=models.PROTECT)

class PollsApphookConfigForm(AppDataForm):
    pass

setup_config(PollsApphookConfigForm, PollsApphookConfig)
