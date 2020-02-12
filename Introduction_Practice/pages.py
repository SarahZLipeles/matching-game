from otree.api import Currency as c, currency_range
from ._builtin import Page
from .models import Constants



class Practice(Page):
    form_model = 'player'
    form_fields = ['counting_box']
    def vars_for_template(self):
        return {
            "participant_vars": str(self.participant.vars)
        }

page_sequence = [Practice]
