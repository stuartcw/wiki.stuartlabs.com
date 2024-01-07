I always want to make an adventure game. This seems like a good library.

```
#!/usr/local/bin/python3

from adventurelib import *
from dataclasses import dataclass, field
import sys

@dataclass
class Room:
    description: str = "An empty room"
    items: list[int]=field(default_factory=list)

currentRoom=Room()
inventory=["an old sausage","a golden key"]

@when("exit")
def exit():
    sys.exit()

@when("look")
def look():
    say(f"You see {currentRoom.description}.")

@when("scream")
def scream():
    print("You unleash a piercing shriek that reverberates around you.")

@when("brush teeth")
def brush_teeth():
    print("You brush your teeth. They feel clean.")

@when("take THING")
def take(thing):
    print(f"You take the {thing}.")
    inventory.append(thing)

@when("drop THING")
def drop(thing):
    say(f"You drop the {thing}.")
    inventory.remove(thing)

@when("inventory")
def show_inventory():
    say("You are carrying "+(", ".join(inventory[:-1]))+f" and {inventory[-1]}.")

@when('enter mirror')
def enter_mirror():
    if get_context() == 'wonderland':
        say('There is no mirror here.')
    else:
        set_context('wonderland')
        say('You step into the silvery surface, which feels wet and cool.')
        say('You realise that clicking your heels will let you return.')


@when('click heels', context='wonderland')
def click_heels():
    set_context(None)
    say('The moment your heels touch the world rearranges around you.')

start()
```
