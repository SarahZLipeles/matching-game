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
    name_in_url = 'Game_2_Game'
    players_per_group = None
    num_rounds = 50


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    counting_box = models.BooleanField(blank=True)
    def get_score(self):
        score = 0
        try:
            for p in self.in_previous_rounds():
                score += p.counting_box
        except:
            pass
        return score
