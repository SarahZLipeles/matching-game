from otree.api import Currency as c, currency_range
from ._builtin import Page
from .models import Constants
from custom_templates.custom_funcs import get_box



class Practice(Page):
    form_model = 'player'
    form_fields = ['counting_box']
    def vars_for_template(self):
        img, num_zeros = get_box()
        return {
            "img": img,
            "answer": num_zeros,
            'participant_vars': self.participant.vars
        }

page_sequence = [Practice]
