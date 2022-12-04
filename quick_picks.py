import random

MINIMUM_RANGE = 0
MAXIMUM_RANGE = 45
MINIMUM_NUMBER = 1
NUMBER_PER_LINE = 6

quick_picks = int(input("How many quick picks do you wish to generate?(1-45):"))

while quick_picks < MINIMUM_RANGE or quick_picks > MAXIMUM_RANGE:
    print("Input not in range")
    quick_picks = int(input("How many quick picks do you wish to generate?(1-45):"))

for quick_pick in range(quick_picks):
    random_list = []
    for i in range(NUMBER_PER_LINE):
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_RANGE)
        while number in random_list:
            number = random.randint(MINIMUM_NUMBER, MAXIMUM_RANGE)
        random_list.append(number)
    random_list.sort()
    print(" ".join(f"{number:2}" for number in random_list))
