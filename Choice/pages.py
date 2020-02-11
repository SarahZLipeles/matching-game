from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time


class Instructions(Page):
    pass

class Selection(Page):
    form_model = 'player'
    form_fields = ['attention_check', 'game_3_switch']
    def before_next_page(self):
        # user has 5 minutes to complete as many pages as possible
        self.participant.vars['game_3_switch'] = self.player.game_3_switch
        self.participant.vars['expiry'] = time.time() + 60*3


page_sequence = [Instructions, Selection]
