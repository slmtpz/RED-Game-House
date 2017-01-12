class Bill:

    def __init__(self):
        self.games = []  # tuple (game_type, number_of_players, time_passed_in_sec, game_charge)
        self.consumptions = []
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
        charge_per_half_hour = game_type['charge'] / 2
        charge_per_man = charge_per_half_hour * (int(time_passed_in_sec / 3600) + 1)
        return self.total_charge + charge_per_man * number_of_players

    def add_consumption(self):
        pass

    def add_other(self):
        pass
