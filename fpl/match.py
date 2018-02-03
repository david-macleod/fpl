import json

class Match(object):
    def __init__(self, match):
        self.goals_a = match[0]["goals_scored"]["a"]
        self.goals_h = match[0]["goals_scored"]["h"]
        self.assists_a = match[1]["assists"]["a"]
        self.assists_h = match[1]["assists"]["h"]
        self.own_goals_a = match[2]["own_goals"]["a"]
        self.own_goals_h = match[2]["own_goals"]["h"]
        self.penalties_saved_a = match[3]["penalties_saved"]["a"]
        self.penalties_saved_h = match[3]["penalties_saved"]["h"]
        self.penalties_missed_a = match[4]["penalties_missed"]["a"]
        self.penalties_missed_h = match[4]["penalties_missed"]["h"]
        self.yellow_cards_a = match[5]["yellow_cards"]["a"]
        self.yellow_cards_h = match[5]["yellow_cards"]["h"]
        self.red_cards_a = match[6]["red_cards"]["a"]
        self.red_cards_h = match[6]["red_cards"]["h"]
        self.saves_a = match[7]["saves"]["a"]
        self.saves_h = match[7]["saves"]["h"]
        self.bonus_a = match[8]["bonus"]["a"]
        self.bonus_h = match[8]["bonus"]["h"]
        self.bps_a = match[9]["bps"]["a"]
        self.bps_h = match[9]["bps"]["h"]