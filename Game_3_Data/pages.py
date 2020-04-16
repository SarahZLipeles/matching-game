
from ._builtin import Page, WaitPage
from .models import Constants
from custom_templates.custom_funcs import (
    get_game_stats
)
import json

class Data(Page):
    def is_displayed(self):
        return self.session.config['data_pages_enabled']
    def vars_for_template(self):
        game_name = Constants.game_name
        
        self.player.switch = float(self.participant.vars['game_3_switch'])
        
        participants = self.session.config["sample_participants"]
        # restrict to specified number of sample participants
        participants = participants[:self.session.config["num_sample_participants"] + 1]

        self.player.calc_stats(game_name, participants)
        
        def win_condition(i):
            if float(i) >= float(self.player.switch):
                return i * (
                    self.player.place == 1 and
                    ((self.player.won_tiebreaker is None) or 
                    self.player.won_tiebreaker)
                )
            else:
                return i

        potential_payouts = self.player.calc_potential_payouts(
            self.session.config['round_values'],
            win_condition
        )

        self.player.value_chosen = float(self.participant.vars['game_3_value'])
        self.player.payout = potential_payouts[self.participant.vars['game_3_value']]

        return {
            'data' : self.player.data()
            }



page_sequence = [Data]