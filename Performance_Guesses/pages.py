from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Performance_Guesses(Page):
    form_model = 'player'
    form_fields = ['belief_piece_rate', 'belief_tournament']
    def before_next_page(self):
        self.participant.vars['belief_piece_rate'] = self.player.belief_piece_rate
        self.participant.vars['belief_tournament'] = self.player.belief_tournament
    def vars_for_template(self):
        return {
            "participant_vars": str(self.participant.vars)
        }


page_sequence = [Performance_Guesses]
