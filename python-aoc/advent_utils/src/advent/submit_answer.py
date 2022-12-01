from advent.config import ROOT_DIR
from advent.console import console
import requests
import os


def submit(year, day, part, answer):
    """Submit the answer to the puzzle."""
    print(f"Submitting answer to {year}/{day} part {part}...")

    if not os.path.exists(ROOT_DIR + "/input"):
        os.mkdir(ROOT_DIR + "/input")

    cookie_path = ROOT_DIR + "/input/.cookie"
    if not os.path.exists(cookie_path):
        session_cookie = console.input(
            "Session cookie missing, please input adventofcode.com session cookie: "
        )
        with open(cookie_path, "w", encoding="utf-8") as file:
            file.write(session_cookie)

    

    cookie = open(cookie_path, "r", encoding="utf-8").read().split("\n")[0]
    headers = {"session": cookie}
    session = requests.Session()
    validate = console.input(f"Answer: {answer}\n Submit? y/n:")
    if validate == "y" or validate == "Y":
        response = session.post(
            f"https://adventofcode.com/{year}/day/{day}/answer",
            data={"level": part, "answer": answer},
            cookies=headers,
        )
        #console.print(response.text)
        if response.status_code == 200:
            print("Success!")
        else:
            print("Failed!")
            print(response.text)