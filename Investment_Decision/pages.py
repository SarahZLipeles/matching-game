from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time


class Instructions(Page):
    form_model = 'player'
    form_fields = ['Points_A', 'Points_B']
    def error_message(self, values):
        if values['Points_A'] + values['Points_B']  != 100:
            return 'The points must add up to 100'
        else:
            self.participant.vars['game_5_values'] = str(self.player.values)
    def before_next_page(self):
        # user has 5 minutes to complete as many pages as possible
        self.participant.vars['expiry'] = time.time() + 90
    def vars_for_template(self):
        return {
            "participant_vars": str(self.participant.vars)
        }



page_sequence = [Instructions]
