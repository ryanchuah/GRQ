import random
from datetime import datetime
import time

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

end_time = datetime(2023, 3, 7, 20, 0, 0)  # 8pm today

while datetime.now() < end_time:
    print(
        "\033[93m"
        "Random name generated: "
        + random.choice(names)
        + "\n"
        + str(end_time - datetime.now())[:-7]
        + " till result\n"
    )
    time.sleep(1)

print("Winner: " + random.choice(names))
