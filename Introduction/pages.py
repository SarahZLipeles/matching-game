from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Intro(Page):
    pass

class Instructions(Page):
    pass

class Matching_Task(Page):
    form_model = 'player'
    form_fields = ['counting_box']
    pass

class Practice(Page):
    form_model = 'player'
    form_fields = ['counting_box']
    pass




page_sequence = [Intro, Instructions, Matching_Task, Practice]
