from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Game_4'
    players_per_group = None
    num_rounds = 1
    round_values = ["0.50","0.75","1.00","1.25","1.50","1.75","2.00","2.25","2.50"]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    attention_check = models.BooleanField()
    game_4_switch = models.StringField()
