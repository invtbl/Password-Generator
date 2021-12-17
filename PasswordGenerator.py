# firstly, generate unique user id# that stores in database
import random
import sqlite3

conn = sqlite3.connect("user_id_storage.db")
c = conn.cursor()


# Create a table
def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS MyUsers(User ID int, Password Phrase str, Security Answer str)')


def data_entry():
    c.execute("INSERT INTO MyUsers VALUES(1234, ' Generator ', ' London ')")
    conn.commit()
    c.close()
    conn.close()


# create_table()
# data_entry()

# Generates a 4 digit user ID from a random number between 1000 and 9998
def id_gen():
    print("Please generate your unique User ID# below")
    generate = input("Enter Y to generate: ")
    user_id = str(random.randint(1000, 9999))

    # Kills the program if "quit" is entered
    if generate == "Y" or generate == "y":
        print("Your unique User ID# is: " + str(user_id))
        print("Store this unique User ID# for future use")
        id_gen.clear()
        id_gen()
    else:
        clear()
        id_gen()


id_gen()

# print user input text asking for user id# and phrase to be encrypted

# create dictionary to store encryption algorithm

# use algorithm to create encrypted password

# print encrypted algorithm

# if statement to print stored password after user id and "phrase" is entered
# create prompt asking whether or not to display encrypted passwords or just phrases

# security questions to authenticate in the event either the user id or "phrase" is forgotten
