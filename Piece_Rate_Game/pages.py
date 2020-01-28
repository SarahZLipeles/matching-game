from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time

class Game_1(Page):
    form_model = 'player'
    form_fields = ['counting_box']
    def get_timeout_seconds(self):
        return self.participant.vars['expiry'] - time.time()
    def app_after_this_page(self, upcoming_apps):
        if self.participant.vars['expiry'] - time.time() <= 0:
            return upcoming_apps[0]
    pass


page_sequence = [Game_1]
