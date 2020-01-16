from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Game_1(Page):
    timeout_seconds = 300
    form_model = 'player'
    form_fields = ['Game_1_Box', "Game_1_Total"]
    pass

class Instructions(Page):
    pass



page_sequence = [Instructions, Game_1]
