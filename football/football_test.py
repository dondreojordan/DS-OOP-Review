import unittest
from players import Player, Defensive, Quarterback
impo
# from possible_values import team_names, location, week
# from game import Game
# from season import generate_rand_games
# from team import team_names

# TODO - some things you can add...

# [X] import the `season` file and make sure generate_random_games only
# [] makes games with appropriate team names 
# [?] (and never has a team playing itself)

# [] Complete the FootballGameTest


class FootballGameTest(unittest.TestCase):
    '''test the class'''
    def test_field_goal_made(self):
        field_goal = Player(field_goals=2)
        self.assertEqual(field_goal.field_goals, 2)

    # def test_get_winner(self):
    #    game = Game(details)
    #    -score points-
    #    winning_team = game.get_winning_team
       
    #    #Give points to team 
    #     self.assertEqual(winning_team, team_name)


class FootballPlayerTest(unittest.TestCase):
    '''Check the default values for Player and Quarterback
    yards=120, touchdowns=5, safety=1,
                 interceptions=0
    '''
    def test_default_player_yards(self):
        player = Player(name='Dude')
        self.assertEqual(player.yards, 120)

    def test_player_yards_set_to(self):
        player = Player(name='OtherDude', yards=150)
        self.assertEqual(player.yards, 150)

    def test_default_qb_interceptions(self):
        qb = Quarterback(name='FancyDude')
        self.assertEqual(qb.interceptions, 4)

    def test_default_qb_completed_passes(self):
        qb1 = Quarterback()
        self.assertEqual(qb1.completed_passes, 20)

    def test_passing_score(self):
        qb2 = Quarterback()
        self.assertEqual((20 - (2 * 4)), qb2.passing_score())


if __name__ == '__main__':
    unittest.main()
