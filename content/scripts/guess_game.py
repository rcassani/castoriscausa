import random
from pyscript import document

game_message_txt = document.querySelector("#game-message-txt")
new_guess_txt = document.querySelector("#new-guess-txt")

def new_game(e):
    'Print instructions and set secret number'
    global x_target
    game_message_txt.innerText = 'Guess the secret number between 0 and 42'
    x_target = random.randint(0, 42)

new_game(None)

def new_guess(e):
    # ignore empty input
    if not new_guess_txt.value:
        return None
    x_str = new_guess_txt.value
    # must be a number
    if not x_str.isnumeric():
        game_message_txt.innerText = 'Come on, it needs to be a number'
        return None
    else:
        try:
            # check it's an integer
            x = int(x_str)
        except ValueError as ve:
            game_message_txt.innerText = 'It needs to be an integer'
    # check it's in range
    if x < 0 or x > 42:
        game_message_txt.innerText = 'It needs to be in the range 0 to 42'
        return None
    # game logic
    if x > x_target:
        game_message_txt.innerText = 'Go lower than {0}'.format(x)
    elif x < x_target:
        game_message_txt.innerText = 'Go higher than {0}'.format(x)
    elif x == x_target:
        game_message_txt.innerText = 'Success!!!'

def new_guess_event(e):
    if e.key == "Enter":
        new_guess(e)
