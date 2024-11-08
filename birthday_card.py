from datetime import datetime
from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Prompt

def birthday_message(dipali, age):
    """Generates a birthday message for Dipali with a cute, aesthetic, and viral feel."""
    message = f"""
Happy {age}th Birthday, {dipali}! 

May this special day be filled with happiness, laughter, and everything your heart desires! 
You are an incredible soul, and the world is lucky to have you! 
Wishing you endless joy, success, and love in the year ahead.

May all your dreams come true as you step into this exciting new chapter.

Keep shining bright, and never forget how truly amazing you are. 

Love, 
Your Friend 

P.S. You're {age} today! Let's make this year unforgettable!
"""
    return message

# Get today's date
today = datetime.now()

# Set Dipali's birthdate (November 9, 2024)
birthdate = today.replace(month=11, day=9, year=2024, hour=0, minute=0, second=0, microsecond=0)

# If her birthday this year has already passed, set next year's birthday
if today > birthdate:
    birthdate = birthdate.replace(year=today.year + 1)

# Calculate the number of days left until Dipali's birthday
days_left = (birthdate - today).days

# Ask for Dipali's name (in case the name is dynamic)
dipali = "Dipali"  # You can replace this with Prompt.ask() if you want user input

# Ask for Dipali's age (or set it directly)
age = 16  # You can also ask for the age dynamically with Prompt.ask()

# Create the birthday card with rich text and panel
card_title = Text(f"🎉 **Happy Birthday, {dipali}!** 🎉", style="bold yellow underline")
card_message = Text(birthday_message(dipali, age))
card_content = Panel(card_message, title=card_title, style="bold magenta", expand=False)

# Display the card
print(card_content)

# Simulating the "Open a Gift!" Button
button_action = Prompt.ask("Press Enter to 'Open a Gift!'")

# Trigger the gift function when Enter is pressed
def open_gift():
    print(" A Virtual HUG and lots of love! ")

if button_action == "":
    open_gift()

# Final reminder of the days left
print(f"\n {days_left} days left until Dipali's big day! ")

 
