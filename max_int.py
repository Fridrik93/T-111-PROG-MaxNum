# https://github.com/Fridrik93/T-111-PROG-MaxNum
num_int = 0
max_int = 0
while True:
    num_int = int(input("Input a number: "))    # Do not change this line
    if num_int < 0:
        break
    if (num_int > max_int):
        max_int = num_int
# Fill in the missing code
print("The maximum is", max_int)    # Do not change this line
