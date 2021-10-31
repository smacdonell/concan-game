from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponseRedirect

import logging


class LobbyView(TemplateView):
    template_name = 'template/lobby.html'
    logger = logging.getLogger('logger')

    def get(self, request):
        context = {}
        return render(request, 'lobby/lobby.html', context)

    def post(self, request):
        self.logger.info(request)
