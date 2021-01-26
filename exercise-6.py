# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

class Season:
  def __init__(self, name, months, startDate, endDate):
    self.name = name
    self.months = months
    self.startDate = startDate
    self.endDate = endDate

winter = Season('winter', ['Dec', 'Jan', 'Feb', 'Mar'], 'Dec 21', 'Mar 19')
spring = Season('spring', ['Mar', 'Apr', 'May', 'Jun'], 'Mar 20', 'Jun 20')
summer = Season('summer', ['Jun', 'Jul', 'Aug', 'Sep'], 'Jun 21', 'Sep 21')
fall = Season('fall', ['Sep', 'Oct', 'Nov', 'Dec'], 'Sep 22', 'Dec 20')

seasons = [winter, spring, summer, fall]

def checkSeason():
  userMonth = input('Enter the month of the year (Jan - Dec): ')
  userDay = int(input('Enter the day of the month: '))
  if userMonth not in months:
    input('Please enter a valid month [enter...]')
    print('- - - - - -')
    checkSeason()
  
  if userDay == 0 or userDay > 31:
    input('Please enter a valid day [enter...]')
    checkSeason()

  currentSeason = ''

  for season in seasons:
    if userMonth in season.months:
      startMonth = season.startDate[0:3]
      startDay = int(season.startDate[4:6])

      endMonth = season.endDate[0:3]
      endDay = int(season.endDate[4:6])

      if userMonth == startMonth and userDay >= startDay:
        currentSeason = season.name
      elif userMonth == endMonth and userDay <= endDay:
        currentSeason = season.name
      elif season.months.index(userMonth) >= season.months.index(startMonth) and season.months.index(userMonth) <= season.months.index(endMonth):
          currentSeason = season.name

  print(f'{userMonth} {userDay} is in {currentSeason} ')
  print('- - - - - -')
  checkSeason()

checkSeason()