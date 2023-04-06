import datetime
from collections import defaultdict

names = [
    "Kai Sean",
    "Lib Kai",
    "Kar Lid",
    "Michael",
    "Alvin",
    "Yi Luk",
    "Steve",
    "Ryan",
    "Brandon",
]

name_to_count_mapping = defaultdict(int)


END_DATETIME = datetime.datetime(2023, 4, 7, 20, 0, 0)


def has_lottery_ended() -> bool:
    return datetime.datetime.now() >= END_DATETIME


def time_until_lottery_ends() -> str:
    return str(END_DATETIME - datetime.datetime.now())[:-7]
