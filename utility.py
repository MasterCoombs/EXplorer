import re

def start_game() -> bool:
    """
    Checks if the user would like to start a game.
    """
    response = input("Would you like to start a game Yes/No?")
    yes_pattern = re.compile(r"y(es)?", re.IGNORECASE)

    return True if re.search(yes_pattern, response) else False