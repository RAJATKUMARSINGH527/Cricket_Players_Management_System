import random
import matplotlib.pyplot as plt
import pandas as pd
# Base Player Class
class Player:
    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role
        self.matches = 0
        self.runs = 0
        self.wickets = 0
    def profile(self):
        return f"{self.name} ({self.role}), Age: {self.age}, Matches: {self.matches}"
# Derived Classes for Different Player Roles
class Batsman(Player):
    def __init__(self, name, age):
        super().__init__(name, age, role="Batsman")
        self.strike_rate = 0.0
        self.batting_average = 0.0
    def update_performance(self, runs, balls_faced):
        self.runs += runs
        self.matches += 1
        self.strike_rate = self.runs / balls_faced * 100
        self.batting_average = self.runs / self.matches
    def profile(self):
        return f"{super().profile()}, Runs: {self.runs}, Strike Rate: {self.strike_rate:.2f}, Average: {self.batting_average:.2f}"
class Bowler(Player):
    def __init__(self, name, age):
        super().__init__(name, age, role="Bowler")
        self.economy_rate = 0.0
        self.bowling_average = 0.0
    def update_performance(self, runs_conceded, overs_bowled, wickets_taken):
        self.wickets += wickets_taken
        self.matches += 1
        self.economy_rate = runs_conceded / overs_bowled
        self.bowling_average = runs_conceded / self.wickets if self.wickets > 0 else 0
    def profile(self):
        return f"{super().profile()}, Wickets: {self.wickets}, Economy Rate: {self.economy_rate:.2f}, Bowling Average: {self.bowling_average:.2f}"
class AllRounder(Player):
    def __init__(self, name, age):
        super().__init__(name, age, role="All-Rounder")
        # Initialize attributes specific to both batting and bowling
        self.strike_rate = 0.0
        self.batting_average = 0.0
        self.economy_rate = 0.0
        self.bowling_average = 0.0
    def update_batting_performance(self, runs, balls_faced):
        self.runs += runs
        self.matches += 1
        self.strike_rate = self.runs / balls_faced * 100
        self.batting_average = self.runs / self.matches
    def update_bowling_performance(self, runs_conceded, overs_bowled, wickets_taken):
        self.wickets += wickets_taken
        self.economy_rate = runs_conceded / overs_bowled
        self.bowling_average = runs_conceded / self.wickets if self.wickets > 0 else 0
    def profile(self):
        return f"{super().profile()}, Runs: {self.runs}, Strike Rate: {self.strike_rate:.2f}, Batting Average: {self.batting_average:.2f}, Wickets: {self.wickets}, Economy Rate: {self.economy_rate:.2f}, Bowling Average: {self.bowling_average:.2f}"
class WicketKeeper(Player):
    def __init__(self, name, age):
        super().__init__(name, age, role="Wicket-Keeper")
        self.catches = 0
        self.stumpings = 0
    def update_performance(self, catches, stumpings):
        self.catches += catches
        self.stumpings += stumpings
        self.matches += 1
    def profile(self):
        return f"{super().profile()}, Catches: {self.catches}, Stumpings: {self.stumpings}"
# Team Creation
class Team:
    def __init__(self, name):
        self.name = name
        self.players = []
    def add_player(self, player):
        self.players.append(player)
    def team_profile(self):
        print(f"Team {self.name}")
        for player in self.players:
            print(player.profile())
# Match Simulation
class MatchSimulator:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
    def simulate_match(self):
        print(f"Match: {self.team1.name} vs {self.team2.name}")
        team1_score = self.simulate_innings(self.team1)
        team2_score = self.simulate_innings(self.team2)
        if team1_score > team2_score:
            print(f"{self.team1.name} wins by {team1_score - team2_score} runs")
        else:
            print(f"{self.team2.name} wins by {team2_score - team1_score} runs")
    def simulate_innings(self, team):
        score = 0
        for player in team.players:
            if isinstance(player, Batsman):
                runs = random.randint(0, 100)
                balls_faced = random.randint(10, 60)
                player.update_performance(runs, balls_faced)
                score += runs
            elif isinstance(player, Bowler):
                runs_conceded = random.randint(20, 60)
                overs_bowled = random.randint(2, 10)
                wickets_taken = random.randint(0, 5)
                player.update_performance(runs_conceded, overs_bowled, wickets_taken)
        print(f"{team.name} scored {score} runs")
        return score
# Player Comparison
def compare_players(player1, player2):
    data = {
        "Player": [player1.name, player2.name],
        "Role": [player1.role, player2.role],
        "Matches": [player1.matches, player2.matches],
        "Runs": [player1.runs, player2.runs],
        "Wickets": [player1.wickets, player2.wickets],
    }
    df = pd.DataFrame(data)
    print(df)
    # Visualization
    df.set_index("Player")[["Runs", "Wickets"]].plot(kind="bar")
    plt.title("Player Comparison")
    plt.show()
# Example Usage
if __name__ == "__main__":
    # Creating players
    player1 = Batsman("Player A", 28)
    player2 = Bowler("Player B", 30)
    player3 = AllRounder("Player C", 25)
    player4 = WicketKeeper("Player D", 27)
    # Creating teams
    team1 = Team("Warriors")
    team2 = Team("Titans")
    team1.add_player(player1)
    team1.add_player(player3)
    team2.add_player(player2)
    team2.add_player(player4)
    # Display team profiles
    team1.team_profile()
    team2.team_profile()
    # Simulating a match
    match = MatchSimulator(team1, team2)
    match.simulate_match()
    # Comparing two players
    compare_players(player1, player2)
# team -- name,players[] + method(player add)
# player(name,...) - batsman(att + method)    bowler  wickletkeepr allrounder
#match --import random
import matplotlib.pyplot as plt
import pandas as pd
# Base Player Class
class Player:
    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role
        self.matches = 0
        self.runs = 0
        self.wickets = 0
    def profile(self):
        return f"{self.name} ({self.role}), Age: {self.age}, Matches: {self.matches}"
# Derived Classes for Different Player Roles
class Batsman(Player):
    def __init__(self, name, age):
        super().__init__(name, age, role="Batsman")
        self.strike_rate = 0.0
        self.batting_average = 0.0
    def update_performance(self, runs, balls_faced):
        self.runs += runs
        self.matches += 1
        self.strike_rate = self.runs / balls_faced * 100
        self.batting_average = self.runs / self.matches
    def profile(self):
        return f"{super().profile()}, Runs: {self.runs}, Strike Rate: {self.strike_rate:.2f}, Average: {self.batting_average:.2f}"
class Bowler(Player):
    def __init__(self, name, age):
        super().__init__(name, age, role="Bowler")
        self.economy_rate = 0.0
        self.bowling_average = 0.0
    def update_performance(self, runs_conceded, overs_bowled, wickets_taken):
        self.wickets += wickets_taken
        self.matches += 1
        self.economy_rate = runs_conceded / overs_bowled
        self.bowling_average = runs_conceded / self.wickets if self.wickets > 0 else 0
    def profile(self):
        return f"{super().profile()}, Wickets: {self.wickets}, Economy Rate: {self.economy_rate:.2f}, Bowling Average: {self.bowling_average:.2f}"
class AllRounder(Player):
    def __init__(self, name, age):
        super().__init__(name, age, role="All-Rounder")
        # Initialize attributes specific to both batting and bowling
        self.strike_rate = 0.0
        self.batting_average = 0.0
        self.economy_rate = 0.0
        self.bowling_average = 0.0
    def update_batting_performance(self, runs, balls_faced):
        self.runs += runs
        self.matches += 1
        self.strike_rate = self.runs / balls_faced * 100
        self.batting_average = self.runs / self.matches
    def update_bowling_performance(self, runs_conceded, overs_bowled, wickets_taken):
        self.wickets += wickets_taken
        self.economy_rate = runs_conceded / overs_bowled
        self.bowling_average = runs_conceded / self.wickets if self.wickets > 0 else 0
    def profile(self):
        return f"{super().profile()}, Runs: {self.runs}, Strike Rate: {self.strike_rate:.2f}, Batting Average: {self.batting_average:.2f}, Wickets: {self.wickets}, Economy Rate: {self.economy_rate:.2f}, Bowling Average: {self.bowling_average:.2f}"
class WicketKeeper(Player):
    def __init__(self, name, age):
        super().__init__(name, age, role="Wicket-Keeper")
        self.catches = 0
        self.stumpings = 0
    def update_performance(self, catches, stumpings):
        self.catches += catches
        self.stumpings += stumpings
        self.matches += 1
    def profile(self):
        return f"{super().profile()}, Catches: {self.catches}, Stumpings: {self.stumpings}"
# Team Creation
class Team:
    def __init__(self, name):
        self.name = name
        self.players = []
    def add_player(self, player):
        self.players.append(player)
    def team_profile(self):
        print(f"Team {self.name}")
        for player in self.players:
            print(player.profile())
# Match Simulation
class MatchSimulator:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
    def simulate_match(self):
        print(f"Match: {self.team1.name} vs {self.team2.name}")
        team1_score = self.simulate_innings(self.team1)
        team2_score = self.simulate_innings(self.team2)
        if team1_score > team2_score:
            print(f"{self.team1.name} wins by {team1_score - team2_score} runs")
        else:
            print(f"{self.team2.name} wins by {team2_score - team1_score} runs")
    def simulate_innings(self, team):
        score = 0
        for player in team.players:
            if isinstance(player, Batsman):
                runs = random.randint(0, 100)
                balls_faced = random.randint(10, 60)
                player.update_performance(runs, balls_faced)
                score += runs
            elif isinstance(player, Bowler):
                runs_conceded = random.randint(20, 60)
                overs_bowled = random.randint(2, 10)
                wickets_taken = random.randint(0, 5)
                player.update_performance(runs_conceded, overs_bowled, wickets_taken)
        print(f"{team.name} scored {score} runs")
        return score
# Player Comparison
def compare_players(player1, player2):
    data = {
        "Player": [player1.name, player2.name],
        "Role": [player1.role, player2.role],
        "Matches": [player1.matches, player2.matches],
        "Runs": [player1.runs, player2.runs],
        "Wickets": [player1.wickets, player2.wickets],
    }
    df = pd.DataFrame(data)
    print(df)
    # Visualization
    df.set_index("Player")[["Runs", "Wickets"]].plot(kind="bar")
    plt.title("Player Comparison")
    plt.show()
# Example Usage
if __name__ == "__main__":
    # Creating players
    player1 = Batsman("Player A", 28)
    player2 = Bowler("Player B", 30)
    player3 = AllRounder("Player C", 25)
    player4 = WicketKeeper("Player D", 27)
    # Creating teams
    team1 = Team("Warriors")
    team2 = Team("Titans")
    team1.add_player(player1)
    team1.add_player(player3)
    team2.add_player(player2)
    team2.add_player(player4)
    # Display team profiles
    team1.team_profile()
    team2.team_profile()
    # Simulating a match
    match = MatchSimulator(team1, team2)
    match.simulate_match()
    # Comparing two players
    compare_players(player1, player2)