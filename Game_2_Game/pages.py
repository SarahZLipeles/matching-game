from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time
from custom_templates.custom_funcs import get_box

class Game_2(Page):
    form_model = 'player'
    form_fields = ['counting_box']
    def time_remaining(self):
        return self.participant.vars['expiry'] - time.time()
    def is_displayed(self):
        self.participant.vars['game_2_score'] = self.player.get_score()
        return self.time_remaining() > 0
    def get_timeout_seconds(self):
        remaining_time = self.time_remaining()
        return remaining_time
    def app_after_this_page(self, upcoming_apps):
        if self.time_remaining() <= 0:
            self.participant.vars['game_2_score'] = self.player.get_score()
            return upcoming_apps[0]
    def vars_for_template(self):
        img, num_zeros = get_box()
        return {
            "img": img,
            "answer": num_zeros,
            'participant_vars': self.participant.vars,
            "score": self.player.get_score(),
            "round": self.player.round_number-1
        }


page_sequence = [Game_2]
