import datetime

class Bill:

    def __init__(self):
        self.startingTime = ''
        self.endingTime = ''
        self.games = []  # tuple (game_type, number_of_players, time_passed_in_sec, game_charge)
        self.extras = []
        self.others = []
        self.charges = []
        self.total_charge = 0.0
        self.is_active = False

    def add_game(self, game_type, number_of_players, time_passed_in_sec):
        new_total_charge = self.get_total_charge(game_type, number_of_players, time_passed_in_sec)
        game_charge = new_total_charge - self.total_charge
        self.total_charge = new_total_charge
        self.games.append((game_type, number_of_players, time_passed_in_sec, game_charge))

    def get_total_charge(self, game_type, number_of_players, time_passed_in_sec):
        n = max(0, number_of_players - 2)
        c = game_type['charge']

        if time_passed_in_sec <= 1800:
            game_charge = c / 2 + n
        else:
            game_charge = (c / 4 + n / 2) * (int(time_passed_in_sec / 900) + 1)

        return self.total_charge + game_charge

    def add_extra(self, extra):
        self.total_charge += extra['charge']
        self.extras.append(extra)

    def add_other(self, name, charge):
        self.total_charge += charge
        self.others.append((name, charge))
