'''Player class to record stats for individual players
'''


class Player:
    '''
    [X] Dosctring TODO
    A Player's stats with the number of yards, touchdowns, saftey
    interceptions and field goals.
    '''
    def __init__(self, name=None, yards=120, touchdowns=5, safety=1,
                 interceptions=0, field_goals=3):
        self.name = name
        self.yards = yards
        self.touchdowns = touchdowns
        self.safety = safety
        self.interceptions = interceptions
        self.field_goals = field_goals

    def get_points(self):
        '''Gets points scored by the player from stats
        '''
        td_points = 6 * self.touchdowns
        safety_points = 2 * self.safety
        total_points = td_points + safety_points
        return total_points
        
class Defensive(Player):
    """
    [X] Override certain parameters of the default Player class and add some
    functionality unique to defensive player
    """
    def __init(self, name=None, yards=85, touchdowns=3,
               safety=1, interceptions=3, tackles=5, sacks=2):
        super().__init__(name=name, yards=yards, touchdowns=touchdowns,
                         safety=safety, interceptions=interceptions)
        self.tackles = tackles
        self.sacks = sacks


class Quarterback(Player):
    '''Override certain parameters of the default Player class and add some
    functionality unique to quarterbacks
    '''
    def __init__(self, name=None, yards=130, touchdowns=5, completed_passes=20,
                 interceptions=4, safety=None, field_goals=None):
        super().__init__(name=name, yards=yards, touchdowns=touchdowns,
                         safety=safety, interceptions=interceptions)
        self.completed_passes = completed_passes

    def passing_score(self):
        '''This is a random formula... FYI
        '''
        score = self.completed_passes - (2 * self.interceptions)
        return score

# TODO - refine the default player stats and/or make a defensive player default
# with number of tackles, sacks, interceptions etc.
