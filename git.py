# Python program to explain os.system() method
	
# importing os module
import os

# Using readlines()
file1 = open('commands.txt', 'r')
every_lines = file1.readlines()

# Strips the newline character
for each_line in every_lines:
    os.system(f"{each_line.strip()}")
    # print(f"{each_line.strip()}")
