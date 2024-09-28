import colorama
from colorama import Fore, Style

# Initialize colorama
colorama.init(autoreset=True)

# Long greeting message
greeting_message = (
    "Hello, World!\n"
    "Welcome to the Colorful Python Program!\n"
    "This program demonstrates how to use the colorama library\n"
    "to print text in different colors in the terminal.\n"
    "You can customize the output by choosing your favorite colors.\n"
    "Let's get started on this colorful journey together!\n"
    "Enjoy coding with Python!\n"
)

# Printing the greeting message with different colors
print(Fore.RED + greeting_message[:15])    # Red for "Hello, World!"
print(Fore.GREEN + greeting_message[15:66])  # Green for the welcome message
print(Fore.YELLOW + greeting_message[66:120]) # Yellow for description
print(Fore.CYAN + greeting_message[120:])    # Cyan for encouragement

# Final message
print(Style.BRIGHT + Fore.MAGENTA + "Keep learning and exploring the world of programming!")
