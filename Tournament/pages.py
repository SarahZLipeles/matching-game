from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time


class Instructions(Page):
    def before_next_page(self):
        # user has 90 seconds to complete as many pages as possible
        self.participant.vars['expiry'] = time.time() + 90
    def vars_for_template(self):
        return {
            "participant_vars": str(self.participant.vars)
        }


page_sequence = [Instructions]
