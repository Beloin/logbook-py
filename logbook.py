#!python

import argparse
import os.path as path
import datetime as dt
from functools import reduce

LOGBOOK_CSV = './data/logbook.csv'
LOGBOOK_MD = './logbook.md'
LOGBOOK_CSV_PATTERN = 'name, date, content, description'


parser = argparse.ArgumentParser(
    prog='Logbook',
    description='Logbook for our job'
)
parser.add_argument('--date', help='Date to pick Logbook. ' +
                    'Respect %DD/%MM/%YY format', dest='date')
parser.add_argument('--yesterday', '-y', help="See yesterday's log")

args = parser.parse_args()

with open(LOGBOOK_MD, 'r') as reader:
    content = reader.readlines()
    content = reduce(lambda a, b: a + b, content)
    content = f"'{content}'"

    # path.isfile(LOGBOOK_CSV)
    csv = open(LOGBOOK_CSV, 'a')
    data = f"Beloin,{dt.datetime.now().strftime('%d-%M-%y')},{content},Any Description Here"

    csv.write('\n')
    csv.write(data)
    csv.close()
