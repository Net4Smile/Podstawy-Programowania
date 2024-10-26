# Yes-no question are often used in surveys to gauge people's attitudes with regard to specific ideas or beliefs. Write a program that prints a survey consisting of three questions. Save the answers to logical type variables. Then view the survey result. Sample result:

# SURVEY Are you interested in computer science? (y/n): y
# Do you like playing computer games? (y/n): n
# Do you have an Instagram account? (y/n): y

# SURVEY RESULTS Interested in computer science: Yes
# Playing computer games: No
# Has an Instagram account: Yes

interestedInCS = input('SURVEY Are you interested in computer science? (y/n): ')
likesPlayingGames = input('Do you like playing computer games? (y/n): ')
hasInstagramAccount = input('Do you have an Instagram account? (y/n): ')

answers = [interestedInCS, likesPlayingGames, hasInstagramAccount]

for i in range(len(answers)):
  if answers[i] == 'y':
    answers[i] = 'Yes'
  else:
    answers[i] = 'No'

print(f'SURVEY RESULTS Interested in computer science: {answers[0]}')
print(f'Playing computer games: {answers[1]}')
print(f'Has an Instagram account: {answers[2]}')
