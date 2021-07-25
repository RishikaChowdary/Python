#program 6
teams=input('enter the teams:').split(' ')
team1_count=0
team2_count=0
for team_name in teams:
    if(team_name=='team1'):
        team1_count+=1
    elif(team_name=='team2'):
        team2_count+=1
if(team1_count>team2_count):
    print('Winner of the day is:team1')
elif(team1_count<team2_count):
    print('Winner of the day is:team2')
elif(team1_count==team2_count):
    print('Match tie')
