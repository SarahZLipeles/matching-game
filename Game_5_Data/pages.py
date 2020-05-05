
from ._builtin import Page, WaitPage
from .models import Constants
from custom_templates.custom_funcs import (
    get_game_stats
)
import json

class Data(Page):
    def is_displayed(self):
        if self.session.config['data_pages_enabled']:
            return True
        else:
            return self.vars_for_template()
    def vars_for_template(self):
        game_name = Constants.game_name

        points_AB = json.loads(self.participant.vars['game_5_values'])
        print(points_AB)
        points_A = float(points_AB['Points_A'])/100
        points_B = float(points_AB['Points_B'])/100

        def payment_condition(i):
            i = i * (
                self.player.place == 1 and
                ((self.player.won_tiebreaker is None) or 
                self.player.won_tiebreaker)
            ) * 5 * points_B + i * points_A
            return i

        participants = self.session.config["sample_participants"]
        participants = participants[:self.session.config["num_sample_participants"] + 1]
        
        self.player.calc_stats(game_name, participants)

        potential_payouts = self.player.calc_potential_payouts(['%s' % payment_condition(1)])
        
        self.player.payout = potential_payouts['%s' % payment_condition(1)]
        self.player.scheme = 'Tournament'
        self.participant.vars[game_name + '_scheme'] = self.player.scheme
        self.player.dump_vars(game_name, self.participant.vars)
        return {
            'data' : self.player.data()
        }



page_sequence = [Data]
