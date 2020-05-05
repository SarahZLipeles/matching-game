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
    name_in_url = 'Survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    payment_game = models.IntegerField()
    scheme_tournament = models.BooleanField()
    score = models.IntegerField()
    win = models.BooleanField()
    payout = models.CurrencyField()
    participant_vars = models.LongStringField()
    game_1_group_scores = models.StringField()
    game_2_group_scores = models.StringField()
    place_game_1 = models.IntegerField()
    place_game_2 = models.IntegerField()
