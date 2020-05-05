from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time
import json


class Instructions(Page):
    form_model = 'player'
    form_fields = ['Points_A', 'Points_B']
    def error_message(self, values):
        if values['Points_A'] + values['Points_B']  !=  50:
            return 'The points must add up to   50'
        else:
            self.participant.vars['game_5_values'] = json.dumps(values)

    def before_next_page(self):
        # user has 90 seconds to complete as many pages as possible
        self.participant.vars['expiry'] = time.time() + self.session.config["seconds_for_counting_task"]
    def vars_for_template(self):
        return {
            'participant_vars': self.participant.vars
        }



page_sequence = [Instructions]
