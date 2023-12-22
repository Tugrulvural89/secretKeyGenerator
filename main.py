# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import random
import string


def generate_secret_key(length=50):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


new_secret_key = generate_secret_key()
print(new_secret_key)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    generate_secret_key()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
