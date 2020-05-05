from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Performance_Guesses(Page):
    form_model = 'player'
    form_fields = ['belief_game_1', 'belief_game_2']
    def before_next_page(self):
        self.participant.vars['belief_game_1'] = self.player.belief_game_1
        self.participant.vars['belief_game_2'] = self.player.belief_game_2
    def vars_for_template(self):
        return {
            'participant_vars': self.participant.vars
        }


page_sequence = [Performance_Guesses]
