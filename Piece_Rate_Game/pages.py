from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time

class Game_1(Page):
    form_model = 'player'
    form_fields = ['counting_box']
    def get_timeout_seconds(self):
        time_remaining = self.participant.vars['expiry'] - time.time()
        return time_remaining
    def before_next_page(self):
        self.player.round_number = 1000
    def app_after_this_page(self, upcoming_apps):
        if self.participant.vars['expiry'] - time.time() <= 0:
            return upcoming_apps[0]
    pass


page_sequence = [Game_1]
