# The birthday paradox

import datetime, random

def getBirthdays(numberOfBirthdays):
    '''Returns a list of number random date objects for birthdays.'''
    birthdays = []
    for i in range(numberOfBirthdays):
        # all the birthdays in same year
        startOfYear = datetime.date(2001, 1, 1)
        # Get a random day into the year
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

 def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None # All birthdays are unique, so return None
    # Compare each birthday to every other birthday
    for a, birthdayA in enumerate(birthdays):
         for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA # Return the matching birthday


# Set up a tuple of month names in order:
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:
    print('How many birthdays shall I generate? (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break
print()

# Generate and display the birthdays
print('Here are', numBDays, 'birthdays:')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(', ', end='')
    monthName = MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText, end='')

print()
print()






