#!/usr/bin/python3

morale_score_counter = 0
help_method = ["Your mental status is BLACK,
               "You should look for help immediately, call 1-800-273-8255 for help.",
               "Your mental status is RED, You might need to seek help from medical professional",
               "Your mental status is ORANGE, I would recommend you watch some YouTube videos",
               "Your mental status is YELLOW, keep it up.",
               "Your mental status is GREEN, you are living in your dream"]
name = input("Write down your name: ")
Questions = ["Question 1, True or False, I don’t like my everyday activities.",
             "People are bugging me about my ethnicity",
             "I feel like my friends are letting me down",
             " I’m a social reject",
             "I don’t get credit for my hard work",
             " I can’t get any peace and quiet",
             " I feel like I don’t explain myself well",
             " I feel isolated",
             "For the past six months, I had suicidal thoughts",
             "For the past six months, I had homicidal thoughts"]

if ('a' <= name <= 'z') or ('A' <= name <= 'Z'):
    for test in Questions:
        print(test)
        while True:
            try:
                score = int(input("Type in your score from 0 - 5, program will be terminated if "
                                  "the input is : "))
                break
            except ValueError:
                print("Oops!  That was no valid number.  Try again...")

        while 0 <= score <= 5:
            morale_score_counter += score
            print("--------------------------------------------------------------")
            break
        else:
            score = int(input("Type in your score from 0 - 5 again, the number you input was invalid: "))
    print(f"Hey, {name} you scored {morale_score_counter} in the test.\n")

    if morale_score_counter <= 10:
        print(help_method[0])
    if 20 >= morale_score_counter > 10:
        print(help_method[1])
    if 30 >= morale_score_counter > 20:
        print(help_method[2])
    if 40 >= morale_score_counter > 30:
        print(help_method[3])
    if 50 >= morale_score_counter > 40:
        print(help_method[4])

else:
    print("Invalid name. ")
