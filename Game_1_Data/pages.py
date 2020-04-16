
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

        participants = self.session.config["sample_participants"]
        participants = participants[:self.session.config["num_sample_participants"] + 1]
        
        self.player.calc_stats(game_name, participants)

        potential_payouts = self.player.calc_potential_payouts(['0.50'])
        
        self.player.payout = potential_payouts['0.50']

        return {
            'data' : self.player.data()
            }



page_sequence = [Data]