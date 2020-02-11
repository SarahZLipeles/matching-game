from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time

class Game_1(Page):
    form_model = 'player'
    form_fields = ['counting_box']
    def time_remaining(self):
        return self.participant.vars['expiry'] - time.time()
    def is_displayed(self):
        return self.time_remaining() > 0
    def get_timeout_seconds(self):
        remaining_time = self.time_remaining()
        return remaining_time
    def app_after_this_page(self, upcoming_apps):
        if self.time_remaining() <= 0:
            self.participant.vars['piece_rate_score'] = self.player.get_score()
            return upcoming_apps[0]
    def vars_for_template(self):
        return {
            "score": self.player.get_score(),
            "round": self.player.round_number-1
        }


page_sequence = [Game_1]
