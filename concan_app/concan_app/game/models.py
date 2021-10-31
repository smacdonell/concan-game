from django.db import models


class GameStatus(models.Model):
    LOBBY = 'lobby'
    IN_PROGRESS = 'in progress'
    FINISHED = 'finished'
    REF_CODE = [
        (LOBBY, 'Game is in the lobby phase, allowing players to join'),
        (IN_PROGRESS, 'Game is in progress'),
        (FINISHED, 'Game is finished')
    ]
    ref_code = models.CharField(choices=REF_CODE, max_length=24)

    class Meta:
        db_table = 'game_status'


class GameAccess(models.Model):
    PUBLIC = 'public'
    PRIVATE = 'private'
    REF_CODE = [
        (PUBLIC, 'Anyone can join this game'),
        (PRIVATE, 'Only players with the code can join this game')
    ]
    ref_code = models.CharField(choices=REF_CODE, max_length=24)


class Game(models.Model):
    created_date = models.DateTimeField('date created', auto_now=True)
    name = models.CharField(max_length=32)
    game_status = models.ForeignKey(GameStatus, on_delete=models.CASCADE)
    game_access = models.ForeignKey(GameAccess, on_delete=models.CASCADE)
    game_code = models.CharField(max_length=4)


class GameState(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    state_id = models.CharField(max_length=64)


class Player(models.Model):
    name = models.CharField(max_length=24)
    score = models.IntegerField(default=0)
    turn_index = models.IntegerField(default=0)
    opened = models.BooleanField(default=False)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
