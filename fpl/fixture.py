def team_converter(team_id):
    """
    Converts a team's ID to their actual name.
    """
    if team_id == 1:
        return "Arsenal"
    elif team_id == 2:
        return "Bournemouth"
    elif team_id == 3:
        return "Brighton"
    elif team_id == 4:
        return "Burnley"
    elif team_id == 5:
        return "Chelsea"
    elif team_id == 6:
        return "Crystal Palace"
    elif team_id == 7:
        return "Everton"
    elif team_id == 8:
        return "Huddersfield"
    elif team_id == 9:
        return "Leicester"
    elif team_id == 10:
        return "Liverpool"
    elif team_id == 11:
        return "Man City"
    elif team_id == 12:
        return "Man Utd"
    elif team_id == 13:
        return "Newcastle"
    elif team_id == 14:
        return "Southampton"
    elif team_id == 15:
        return "Stoke"
    elif team_id == 16:
        return "Swansea"
    elif team_id == 17:
        return "Spurs"
    elif team_id == 18:
        return "Watford"
    else:
        return "West Brom"

class Fixture(object):
    def __init__(self, fixture):
        self.team_h_score = fixture["team_h_score"]
        self.team_a_score = fixture["team_a_score"]
        self.kickoff_time_formatted = fixture["kickoff_time_formatted"]
        self.kickoff_time = fixture["kickoff_time"]
        self.team_a_id = fixture["team_a"]
        self.team_h_id = fixture["team_h"]
        self.team_a_name = team_converter(fixture["team_a"])
        self.team_h_name = team_converter(fixture["team_h"])
        self.gameweek = fixture["event"]
        self.gameweek_name = self._gameweek_name(fixture)
        self.stats = self._stats(fixture)
        
    def _gameweek_name(self, fixture):
        if not fixture.get("event_name"):
            return ""
        return fixture["event_name"]

    def _stats(self, fixture):
        if not fixture.get("stats"):
            return []
        return fixture["stats"]

    def __str__(self):
        return "{} {}-{} {} - Gameweek {} - {}".format(self.team_h_name,
            self.team_h_score, self.team_a_score, self.team_a_name,
            self.gameweek, self.kickoff_time)