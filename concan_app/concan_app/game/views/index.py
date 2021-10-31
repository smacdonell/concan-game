from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from ..models import Game
from ..models import GameStatus
from ..models import GameAccess
from ..forms.index_forms import NewGameForm
from ..forms.index_forms import JoinExistingGameForm
from ..properties.property_reader import PropertyReader

import logging


class IndexView(TemplateView):
    template_name = 'index/index.html'
    logger = logging.getLogger('logger')

    """
     Constructs the forms and objects needed for the splash page 
    """
    def construct_context(self, request, *args, **kwargs):
        if request.method == 'GET':
            new_game_form = NewGameForm()
            join_existing_game_form = JoinExistingGameForm()
        else:
            new_game_form = NewGameForm(request.POST)
            join_existing_game_form = JoinExistingGameForm(request.POST)

        lobby_status = GameStatus.objects.get(ref_code='LOBBY')
        open_lobbies = Game.objects.filter(game_status=lobby_status)

        return {
            'new_game_form': new_game_form,
            'join_existing_game_form': join_existing_game_form,
            'open_lobbies': open_lobbies
        }

    def get(self, request, *args, **kwargs):
        context = self.construct_context(request, *args, **kwargs)
        PropertyReader.read_string('DEFAULT', 'test');
        return render(request, 'index/index.html', context)

    def post(self, request, *args, **kwargs):
        self.logger.info(request.POST)

        new_game_form = NewGameForm(request.POST)
        join_existing_game_form = JoinExistingGameForm(request.POST)

        new_game = 'start_new_sub' in request.POST
        if new_game_form.is_valid() or join_existing_game_form.is_valid():
            if new_game:
                self.create_new_game(request)
            else:
                self.join_existing_game(request)

            return HttpResponseRedirect('/lobby')

        return render(request, 'index/index.html',
            self.construct_context(request, *args, **kwargs))

    def create_new_game(self, request):
        access = GameAccess.objects.get(ref_code='PUBLIC')
        status = GameStatus.objects.get(ref_code='LOBBY')
        game = Game(name=request.POST['game_name'], game_code='1234', game_access=access, game_status=status)
        game.save()

    def join_existing_game(self, request):
        print()

