from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time


class Instructions(Page):
    form_model = 'player'
    form_fields = ['Points_A', 'Points_B']
    def error_message(self, values):
        print('values is', values)
        if values['Points_A'] + values['Points_B']  != 100:
            return 'The numbers must add up to 100'
    def before_next_page(self):
        # user has 5 minutes to complete as many pages as possible
        self.participant.vars['expiry'] = time.time() + 90
    pass



page_sequence = [Instructions]
