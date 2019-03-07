
classroom = [
  [None, "Pumpkin", None, None],
  ["Socks", None, "Mimi", None],
  ["Gismo", "Shadow", None, None],
  ["Smokey","Toast","Pacha","Mau"]
]

row_index = 0
seat_index = 0
for row_index, row in enumerate(classroom):
    for seat_index, seat in enumerate(row):
        if seat == None:
            print("Row {} seat {} is free. Do you want to sit there? (y/n)".format(row_index + 1, seat_index + 1))
            user_input = input()
            if user_input == 'y':
                print("What is your name?")
                user_name = input()
                classroom[row_index][seat_index] = user_name
                break
    seat_index += 1
row_index += 1

print(classroom)

# Row 1 seat 1 is free.
# Row 1 seat 3 is free.
# Row 1 seat 4 is free.
# Row 2 seat 2 is free.
# Row 3 seat 3 is free.
# Row 3 seat 4 is free.


# Row 1 seat 1 is free. Do you want to sit there? (y/n) # user says 'n'
# Row 1 seat 3 is free. Do you want to sit there? (y/n) # user says 'n'
# Row 1 seat 4 is free. Do you want to sit there? (y/n) # user says 'n'
# Row 2 seat 2 is free. Do you want to sit there? (y/n) # user says 'n'
# Row 3 seat 3 is free. Do you want to sit there? (y/n) # user says 'n'
# Row 3 seat 4 is free. Do you want to sit there? (y/n) # user says 'y'
# What is your name? # user says "Tama"
