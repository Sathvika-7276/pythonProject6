Numbers = []
NUMBER_OF_INPUTS = 5
for i in range(NUMBER_OF_INPUTS):
    user_input = int(input("Number:"))
    Numbers += [user_input]
print(f"The first number is {Numbers[0]}")
print(f"The last number is {Numbers[-1]}")
print(f"The smallest number is {min(Numbers)}")
print(f"The largest number is {max(Numbers)}")
print(f"the average of the numbers is {sum(Numbers)/len(Numbers)}")