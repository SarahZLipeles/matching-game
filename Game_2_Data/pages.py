
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
        (
            self.player.score,
            self.player.group_scores,
            self.player.place,
            self.player.won_tiebreaker
        ) = get_game_stats(
            game_name,
            self.player,
            participants)
        potential_payouts = {}
        for i in self.session.config['round_values']:
            potential_payouts[i] = float(i) * self.player.score * (
                self.player.place == 1 and
                (self.player.won_tiebreaker is None or 
                self.player.won_tiebreaker)
            )
        self.player.potential_payouts = json.dumps(potential_payouts)
        data = {
            'score': self.player.score,
            'group_scores': self.player.group_scores,
            'place': self.player.place,
            'won_tiebreaker': self.player.won_tiebreaker,
            'potential_payouts': self.player.potential_payouts
        }
        # headers = ['score', 'group_scores', 'place', 'tiebreaker']
        return {
            'data' : data
            }



page_sequence = [Data]
