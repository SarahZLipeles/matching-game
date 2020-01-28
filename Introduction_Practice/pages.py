from otree.api import Currency as c, currency_range
from ._builtin import Page
from .models import Constants



class Practice(Page):
    form_model = 'player'
    form_fields = ['counting_box']

page_sequence = [Practice]
