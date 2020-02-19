from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time


class Instructions(Page):
    def vars_for_template(self):
        return {
            "participant_vars": str(self.participant.vars)
        }

class Selection(Page):
    form_model = 'player'
    form_fields = ['attention_check', 'game_4_switch']
    def before_next_page(self):
        # user has 5 minutes to complete as many pages as possible
        self.participant.vars['game_4_switch'] = self.player.game_4_switch
        self.participant.vars['expiry'] = time.time() + 90
    def vars_for_template(self):
        game_1_score = 0
        try: # try catch since apps are skipped in testing
            game_1_score = int(self.participant.vars['game_1_score'])
        except:
            pass
        return {
            'game_1_score': game_1_score,
            "participant_vars": str(self.participant.vars)
        }


page_sequence = [Instructions, Selection]
