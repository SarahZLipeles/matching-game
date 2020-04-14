
from ._builtin import Page, WaitPage
from .models import Constants
from custom_templates.custom_funcs import (
    get_game_stats
)

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
            self.player.tiebreaker
        ) = get_game_stats(
            game_name,
            self.player,
            participants)
        data = {
            'score': self.player.score,
            'group_scores': self.player.group_scores,
            'place': self.player.place,
            'tiebreaker': self.player.tiebreaker
        }
        # headers = ['score', 'group_scores', 'place', 'tiebreaker']
        return {
            'data' : data
            }



page_sequence = [Data]
