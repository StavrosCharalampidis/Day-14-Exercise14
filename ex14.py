# import from sys the argv module
from sys import argv

# Those args is input from the terminal
Script, First, Second = argv

# The Variable prompt store a string
prompt = '> '

# Print the terminal inputs
print(f'Hello {First} {Second}, Im the {Script}!!!')

# I ask the user some quest to answer.
print(f'What is yor age {First} {Second}?', end='\n')

# The Variable age is for answering the question.
age = input(prompt)

# I ask the user some quest to answer.
print(f'Where do you live {First} {Second}?', end='\n')

# The Variable live is for answering the question.
live = input(prompt)

# I ask the user some quest to answer.
print(f'What is your favorite Number {First} {Second}?', end='\n')

# The Variable favoriteNumber is for answering the question.
favoriteNumber = input(prompt)

# I ask the user some quest to answer.
print(f'when do you have birthday {First} {Second}?', end='\n')

# The Variable userBirthday is for answering the question.
userBirthday = input(prompt)

# Print The Results of your answers, Using the format-string
print("""
    Yor age {} is {}.
    You live {} in {}.
    Your favoriteNumber {} is {}.
    And your B-Day {} is {}
""".format(First, age,
           First, live,
           First, favoriteNumber,
           First, userBirthday))