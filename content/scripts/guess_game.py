import random

game_message_txt = Element("game-message-txt")
new_guess_txt = Element("new-guess-txt")

def new_game():
    'Print instructions and set secret number'
    global x_target
    game_message_txt.write('Guess the secret number between 0 and 42')
    x_target = random.randint(0, 42)

new_game()

def new_guess(*args, **kws):
    # ignore empty input
    if not new_guess_txt.element.value:
        return None
    x_str = new_guess_txt.element.value
    # must be a number
    if not x_str.isnumeric():
        game_message_txt.write('Come on, it needs to be a number')
        return None
    else:
        try:
            # check it's an integer
            x = int(x_str)
        except ValueError as ve:
            game_message_txt.write('It needs to be an integer')
    # check it's in range
    if x < 0 or x > 42:
        game_message_txt.write('It needs to be in the range 0 to 42')
        return None
    # game logic
    if x > x_target:
        game_message_txt.write('Go lower than {0}'.format(x))
    elif x < x_target:
        game_message_txt.write('Go higher than {0}'.format(x))
    elif x == x_target:
        game_message_txt.write('Success!!!')

def new_guess_event(e):
    if e.key == "Enter":
        new_guess()

new_guess_txt.element.onkeypress = new_guess_event
