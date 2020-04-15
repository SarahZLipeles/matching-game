from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,

)



author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Game_2_Data'
    players_per_group = 4
    num_rounds = 1
    game_name = "game_2"


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    score = models.IntegerField()
    group_scores = models.StringField(max_length=16) # unless we have 3 figure scores, list string shouldn't exceed 16 chars
    place = models.IntegerField()
    won_tiebreaker = models.BooleanField()
    potential_payouts = models.LongStringField()
    pass
