
from ._builtin import Page, WaitPage
from .models import Constants
from custom_templates.custom_funcs import (
    get_game_stats
)
import json
import random

class Data(Page):
    def is_displayed(self):
        return self.session.config['data_pages_enabled']
    def vars_for_template(self):
        game_name = Constants.game_name
        participants = self.session.config["sample_participants"]
        participants = participants[:self.session.config["num_sample_participants"] + 1]
        
        self.player.calc_stats(game_name, participants)
        #calculate potential payouts, applying win condition (lambda function)
        potential_payouts = self.player.calc_potential_payouts(
            self.session.config['round_values'],
            lambda i:
                i * (self.player.place == 1 and
                    (self.player.won_tiebreaker is None or 
                    self.player.won_tiebreaker))
        )

        self.participant.vars['game_2_value'] = random.choice(self.session.config['round_values'])
        self.player.value_chosen = float(self.participant.vars['game_2_value'])
        self.player.payout = potential_payouts[self.participant.vars['game_2_value']]
        return {
            'data' : self.player.data()
            }



page_sequence = [Data]