# CP1404/CP5632 - Practical
# File reading and writing tasks following strict instructions

# 1. Ask the user for their name and write it to 'name.txt' using open and close
name = input("Enter your name: ")
file_out = open('name.txt', 'w')
file_out.write(name)
file_out.close()

# 2. Read the name from 'name.txt' and greet the user, using open and close
file_in = open('name.txt', 'r')
name_from_file = file_in.read().strip()
file_in.close()
print(f"Hi {name_from_file}!")

# 3. Read first two numbers from 'numbers.txt', add them and print the result using with and readlines
with open('numbers.txt', 'r') as numbers_file:
    lines = numbers_file.readlines()
    total = int(lines[0]) + int(lines[1])
    print(total)  # Should print 59

# 4. Read all numbers from 'numbers.txt', sum them and print the total using with and for loop
with open('numbers.txt', 'r') as numbers_file:
    total_all = 0
    for line in numbers_file:
        total_all += int(line.strip())
    print(total_all)
