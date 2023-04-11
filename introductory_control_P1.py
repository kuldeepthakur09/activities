Provide Feedback to the User (Console level Feedback)
Test (Paper Calculation)
Validate (Paper Calculation = Code  Result)
'''
'''

total_runs_scored = int(input("Enter the total runs scored by the team: "))
total_overs_faced = int(input("Enter the total overs faced by the team: "))
total_runs_conceded = int(input("Enter the total runs conceded by the team's opponents: "))
total_overs_bowled = int(input("Enter the total overs bowled by the team's opponents: "))

team_run_rate = (total_runs_scored / total_overs_faced)
opponent_run_rate = (total_runs_conceded / total_overs_bowled)
net_run_rate = (team_run_rate - opponent_run_rate) * 100

print("The team's net run rate is:", net_run_rate)

other_team_net_run_rate = 5.0 
if net_run_rate > other_team_net_run_rate:
    print("The team is ahead in net run rate and tops the points table.")
elif net_run_rate < other_team_net_run_rate:
    print("The team is behind in net run rate and does not top the points table.")
else:
    print("The teams have the same net run rate. The tie-breaker will depend on other factors.")