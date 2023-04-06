import secrets
import datetime
import time
import requests
from dotenv import load_dotenv

load_dotenv()
import os

END_DATETIME = datetime.datetime(2023, 4, 6, 23, 26, 0)

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

name_to_count_mapping = {name: 0 for name in names}


def has_lottery_ended() -> bool:
    return datetime.datetime.now() >= END_DATETIME


def time_until_lottery_ends() -> str:
    return str(END_DATETIME - datetime.datetime.now())[:-7]


def most_frequent_names():
    global name_to_count_mapping
    highest_frequency = max(name_to_count_mapping.values())
    return [
        name
        for name, count in name_to_count_mapping.items()
        if count == highest_frequency
    ]


def send_request_to_update_leaderboard():
    global name_to_count_mapping
    requests.post(
        "http://127.0.0.1:5000/update_leaderboard",
        json={
            "name_to_count_mapping": {
                name: count
                for name, count in sorted(
                    name_to_count_mapping.items(),
                    key=lambda item: item[1],
                    reverse=True,
                )
            },
        },
        headers={"API_KEY": os.getenv("API_KEY")},
    )


def send_request_to_end_lottery(winner):
    requests.post(
        "http://127.0.0.1:5000/end_lottery",
        json={"winner": winner},
        headers={"API_KEY": os.getenv("API_KEY")},
    )


while not has_lottery_ended():
    random_name = secrets.choice(names)
    name_to_count_mapping[random_name] += 1
    send_request_to_update_leaderboard()
    print(
        "\033[96m"
        f"Current list order: {str(names)}\n"
        f"Random name generated: {random_name}. "
        f"He has been picked {name_to_count_mapping[random_name]} times so far\n"
        f"Current Leader: {' and '.join(most_frequent_names())} - been picked {name_to_count_mapping[most_frequent_names()[0]]} times\n"
        f"{time_until_lottery_ends()} till result\n"
    )
    time.sleep(1)

winner = secrets.choice(most_frequent_names())
print("Winner: " + winner)

send_request_to_end_lottery(winner)