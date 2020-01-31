from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time


class Instructions(Page):
    form_model = 'player'
    form_fields = ['counting_box']

    def before_next_page(self):
        # user has 5 minutes to complete as many pages as possible
        self.participant.vars['expiry'] = time.time() + 90
    pass



page_sequence = [Instructions]
