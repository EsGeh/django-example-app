from django.shortcuts import render

from aldryn_apphooks_config.utils import get_app_instance
from django.http import HttpResponse
from polls.views import DetailView


def single(request):
    namespace, config = get_app_instance(request)
    poll = config.poll
    return HttpResponse( str(poll) )

    # (why does this not work?):
    # return DetailView.as_view()(request, pk = poll.pk )

