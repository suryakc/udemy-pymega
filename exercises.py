""" Test """

import datetime
import os

def celsius_to_fahrenheit(celsius):
    """A function to convert celsius to fahrenheit"""
    print("Converting {0} to fahrenheit...".format(celsius))
    try:
        return celsius * 9 / 5 + 32
    except ZeroDivisionError:
        print("An error occurred.")
        print("\n")


def celsius_to_fahrenheit_2(celsius):
    """A function to convert celsius to fahrenheit"""
    if celsius < -273.15:
        print("The lowest possible temperature that physical matter can reach is -273.15 °C."
              "\nPlease enter a valid temperature.")
        return

    print("Converting {0} to fahrenheit...".format(celsius))
    try:
        return celsius * 9 / 5 + 32
    except ZeroDivisionError:
        print("An error occurred.")


def exercise_one():
    """Exercise 1: Convert celsius to fahrenheit"""
    print("Exercise 1: Convert celsius to fahrenheit")
    print(celsius_to_fahrenheit(40))
    print("\n")


def exercise_two():
    """Exercise 2: Using a dictionary"""
    print("Exercise 2: Using a dictionary")
    money = {"saving_account" : 200, "checking_account" : 100, "under_bed" : [500, 10, 100]}
    print(money["under_bed"][1])
    print("\n")


def exercise_three():
    """Exercise 3: Using conditionals"""
    print("Exercise 3: Using conditionals")
    print(celsius_to_fahrenheit_2(-274.15))
    print("\n")


def exercise_four():
    """Exercise 4: Iterate"""
    print("Exercise 4: Iterate")
    temperatures = [10, -20, -289, 100]
    for temperature in temperatures:
        print(celsius_to_fahrenheit_2(temperature))
        print("\n")


def exercise_five():
    """Exercise 5: Integrates functions, loops, conditionals and file handling"""
    print("Exercise 5: Integrates functions, loops, conditionals and file handling")
    temperatures = [10, -20, -289, 100]
    with open("exercise-5-output.txt", "w") as output_file:
        for temperature in temperatures:
            fahrenheit = celsius_to_fahrenheit_2(temperature)
            if fahrenheit is not None:
                output_file.write(str(fahrenheit))
                output_file.write("\n")


def exercise_six():
    """Exercise 6: Merging Text Files"""
    print("Exercise 6: Merging Text Files")
    input_file_dir = os.path.join(os.getcwd(), "exercise-6")
    input_files = [f for f in os.listdir(input_file_dir) \
                   if os.path.isfile(os.path.join(input_file_dir, f))]
    output_file_name = os.path.join(input_file_dir, \
                       datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt")
    with open(output_file_name, "w") as output_file:
        for input_file_path in input_files:
            input_file_path = os.path.join(input_file_dir, input_file_path)
            with open(input_file_path, "r") as input_file:
                content = input_file.read()
            output_file.write(content + "\n")


def run_all_exercises():
    """Runs all the exercise functions"""
    print("------------------------------")
    exercise_one()
    print("------------------------------")
    print("------------------------------")
    exercise_two()
    print("------------------------------")
    print("------------------------------")
    exercise_three()
    print("------------------------------")
    print("------------------------------")
    exercise_four()
    print("------------------------------")
    print("------------------------------")
    exercise_five()
    print("------------------------------")
    print("------------------------------")
    exercise_six()
    print("------------------------------")
    print("------------------------------")


if __name__ == "__main__":
    run_all_exercises()
