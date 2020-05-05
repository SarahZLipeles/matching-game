from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import time
from custom_templates.custom_funcs import get_box


class Instructions(Page):
    form_model = 'player'
    form_fields = ['counting_box']

    def before_next_page(self):
        # user has 90 seconds to complete as many pages as possible
        self.participant.vars['expiry'] = time.time() + self.session.config["seconds_for_counting_task"]
    def vars_for_template(self):
        img, num_zeros = get_box()
        return {
            "img": "boxes/" + img,
            "answer": num_zeros,
            'participant_vars': self.participant.vars
        }



page_sequence = [Instructions]
