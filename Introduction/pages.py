from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from custom_templates.custom_funcs import get_box


class Intro(Page):
    def vars_for_template(self):
        return {
            'participant_vars': self.participant.vars
        }
    pass

class Instructions(Page):
    def vars_for_template(self):
        return {
            'participant_vars': self.participant.vars
        }
    pass

class Counting_Task(Page):
    def vars_for_template(self):
        img, num_zeros = get_box()
        return {
            "img": "boxes/" + img,
            "answer": num_zeros,
            'participant_vars': self.participant.vars
        }




page_sequence = [Intro, Instructions, Counting_Task]
