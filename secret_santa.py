# file SecretSantaConstraintSolver/secret_santa.py
"""
Secret Santa name maker
"""
from __future__ import division

import argparse
import logging
import os
import random

__modname__ = "secret_santa.py"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__modname__)

def main():
    """
    main function
    """
    parser = argparse.ArgumentParser(description="Couples Secret Santa Maker")
    parser.add_argument("-c", "--couples-file", help="Path to couples tsv file", required=True)
    parser.add_argument("-e", "--emails-file", help="Path to emails tsv file", required=True)
    args = parser.parse_args()


    couples = make_couples_list(args.couples_file)
    all_people = list(sum(couples, ()))

    person_to_email = make_email_mapping(args.emails_file)

    # ensure we have an email for everyone
    if not all([person in person_to_email.keys() for person in all_people]):
        logger.error("Emails file does not have an email for everyone from couples")
        raise SystemExit("Emails file missing people -- Exiting")

    santa_to_santee = {}


    solved = False
    while not solved:

        curr_santa_to_santee = {}
        for couple_list in couples:

            # get the possible pairing tuples and shuffle
            possibilities = list(set(couples) - set([couple_list]))
            random.shuffle(possibilities)

            # flatten them out and shuffle again
            possibilities = [person for couple in possibilities for person in couple]
            random.shuffle(possibilities)

            couple_solved = False
            for person in couple_list:

                # get the list of current santas and santees so we dont reuse
                possible_santas = filter(lambda possible: possible not in curr_santa_to_santee.keys(), possibilities)
                if len(possible_santas) == 0:
                    break

                santa_pick = random.choice(possible_santas)
                curr_santa_to_santee[santa_pick] = person

        # validate the solution
        all_are_santa = all([person in curr_santa_to_santee.keys()])
        all_are_santee = all([person in curr_santa_to_santee.values()])
        solved = all_are_santa and all_are_santee

    # its been solved
    santa_to_santee = curr_santa_to_santee
    logger.info("Secret Santa Solution Found!")

    for santa in santa_to_santee:
        santee = santa_to_santee[santa]
        print "Santa: {}\tSantee: {}".format(santa, santee)


def make_couples_list(couples_file):
    """
    Generate a list of tuples representing the couples
    that should not get paired together.
    """
    couples_file = os.path.abspath(couples_file)
    if not os.path.isfile(couples_file):
        logger.error("{} couples file does not exisit".format(couples_file))
        raise SystemExit("File not found -- Exiting")

    couples = []
    with open(couples_file, "r") as fh:
        for line in fh:
            couples.append(tuple(line.rstrip().split("\t")))

    logger.info("Found {} couples in couples file: {}".format(str(len(couples)), couples_file))
    return couples


def make_email_mapping(email_file):
    """
    Load the emails tsv file, should be
    <name>\t<email> with an email for every one
    in couples.
    """
    email_file = os.path.abspath(email_file)
    if not os.path.isfile(email_file):
        logger.error("{} email file does not exisit".format(email_file))
        raise SystemExit("Invalid Email File -- Exiting")

    email_mapping = {}
    with open(email_file, "r") as fh:
        for line in fh:
            line_split = line.rstrip().split("\t")
            if len(line_split) != 2:
                logger.error("Email line: {} is invalid".format(line))
                raise SystemExit("Invalid Email File -- Exiting")

            email_mapping[line_split[0]] = line_split[1]

    return email_mapping


if __name__ == "__main__":
    main()
