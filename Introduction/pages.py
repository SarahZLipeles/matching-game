from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    def vars_for_template(self):
        return {
            "participant_vars": str(self.participant.vars)
        }
    pass

class Instructions(Page):
    def vars_for_template(self):
        return {
            "participant_vars": str(self.participant.vars)
        }
    pass

class Counting_Task(Page):
    form_model = 'player'
    form_fields = ['counting_box']
    def vars_for_template(self):
        return {
            "participant_vars": str(self.participant.vars)
        }




page_sequence = [Intro, Instructions, Counting_Task]
