from django.db import models
from cms.models import CMSPlugin
from polls.models import Question
from polls_cms_integration.cms_appconfig import PollsApphookConfig
# from aldryn_apphooks_config.fields import AppHookConfigField


class PollPluginModel(CMSPlugin):
    poll = models.ForeignKey(Question, on_delete=models.PROTECT)

    def __str__(self):
        return self.poll.question_text

# Model not needed.
# All necessary information is in in cms_appconfig.PollsApphookConfig
'''
class PollsApphookModel(models.Model):
    app_config = AppHookConfigField(PollsApphookConfig)
    poll = models.ForeignKey(Question, on_delete=models.PROTECT)

    def __str__(self):
        return self.poll.question_text
'''
