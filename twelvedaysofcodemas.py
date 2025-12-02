import argparse

from days.Day1 import run as Day1
from days.Day2 import run as Day2
from days.Day3 import run as Day3
from days.Day4 import run as Day4
from days.Day5 import run as Day5
from days.Day6 import run as Day6
from days.Day7 import run as Day7
from days.Day8 import run as Day8
from days.Day9 import run as Day9
from days.Day10 import run as Day10
from days.Day11 import run as Day11
from days.Day12 import run as Day12

import utils


def getDayFunction(day_number):
    day_functions = {
        1: Day1,
        2: Day2,
        3: Day3,
        4: Day4,
        5: Day5,
        6: Day6,
        7: Day7,
        8: Day8,
        9: Day9,
        10: Day10,
        11: Day11,
        12: Day12
    }
    return day_functions.get(day_number, None)


def getDayLyrics(multiple_days, day_number, result1, result2):
    day_lyrics = {
        1: "first",
        2: "second",
        3: "third",
        4: "fourth",
        5: "fifth",
        6: "sixth",
        7: "seventh",
        8: "eighth",
        9: "ninth",
        10: "tenth",
        11: "eleventh",
        12: "twelfth",
    }

    day = day_lyrics.get(day_number, f"{day_number}th")
    day_lyric = f"On the {day} day of Advent, my code gave to me..."
    return day_lyric


def getResultLyrics(multiple_days, day_number, result1, result2):
    and_string = "and " if multiple_days else ""
    result_lyrics = {
        1: f"{and_string}{result1} partidges in {result2} pear trees.",
        2: f"{result2} turtle doves",
        3: f"{result2} french hens",
        4: f"{result2} calling birds",
        5: f"{result2} golden rings",
        6: f"{result2} geese a-laying",
        7: f"{result2} swans a-swimming",
        8: f"{result2} maids a-milking",
        9: f"{result2} ladies dancing",
        10: f"{result2} lords a-leaping",
        11: f"{result2} pipers piping",
        12: f"{result2} drummers drumming",
    }
    return result_lyrics.get(day_number, "")


def runNumberOfDays(number_of_days):
    current_day = number_of_days
    multiple_days = number_of_days > 1

    dayLyric = getDayLyrics(multiple_days, current_day, None, None)
    print("\t" + dayLyric)

    while current_day > 0:
        day_function = getDayFunction(current_day)

        if day_function is None:
            print(f"No implementation for Day {current_day}")
            current_day -= 1
            continue

        part1, part2 = day_function(
            f"./inputs/day{current_day}test.txt", f"./inputs/day{current_day}real.txt")
        resultLyrics = getResultLyrics(
            multiple_days, current_day, part1, part2)
        print("\t" + resultLyrics)
        current_day -= 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Run Advent of Code solutions.")
    parser.add_argument("--day", type=int, required=True,
                        help="Day number to run")
    args = parser.parse_args()

    utils.verbosity = 0

    print("\n")
    print("\t==== 12 Days of Codemas ====")
    print("\n")

    runNumberOfDays(number_of_days=max(0, min(12, args.day)))

    print("\n")
