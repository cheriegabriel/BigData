import sqlite3
import csv
import os
from sqlite3 import Error
import re


#cipher code
decrypt = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] + [str(num) for num in list(range(0,10))] + ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
encrypt = ['t','i','m','e','o','d','a','n','s','f','r','b','c','g','h','j','k','l','p','q','u','v','w','x','y','z'] + [str(num) for num in list(range(9,-1,-1))] + ['T','I','M','E','O','D','A','N','S','F','R','B','C','G','H','J','K','L','P','Q','U','V','W','X','Y','Z']

# connect to database USER
conn = sqlite3.connect('USER.db')
cursor = conn.cursor()  #used to make the connection for executing SQL queries

# create table if not exists
cursor.execute("""CREATE TABLE IF NOT EXISTS TB_USER (USER_ID TEXT PRIMARY KEY, CRYPTOGRAPHIC_PASSWORD TEXT, EMAIL, Access_Count INTEGER DEFAULT 0);""")

cursor.close()
conn.close()


def select():
    # the statement below will loop until the user quit the application
    error_choice = True
    while error_choice:
        try:
            print("===========================================")
            print("| New User? [1]-Yes    [2]-No     [3]Quit |")
            print("===========================================")
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid entry. Select option [1-3].. Please try again.")
            continue
        else:
            error_choice = False
    if choice == 1:
        new_user()

    elif choice == 2:
        existing_user()

    elif choice == 3:
        quit();

# this function will not accept symbol for the password input
def spell_check(str):
    sym = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    assert sym.search(str) == None

# this function will return the value of encoder from decoder
def encrypting(str):
    try:
        # with open('CypherCode.csv', 'r') as cyphercode:
        #     csvreader = csv.reader(cyphercode, delimiter=',')
        #     encrypt = ''
        #     for i in str:
        #         encrypt = list(i[0] for i )
        #     return encrypt
        Ncrypt = ''
        for i in str:
            Ncrypt = Ncrypt + encrypt[decrypt.index(i)]
        return Ncrypt
    except ValueError:
        print("Invalid input.")

# this function will return the value of decoder from encoder
def decrypting(str):
    try:
        # with open('CypherCode.csv', 'r') as cyphercode:
        #     csvreader = csv.reader(cyphercode, delimiter=',')
        #     decrypt = ''
        #     for i in str:
        #         decrypt = r2[r1]
        #     return decrypt
        Dcrypt = ''
        #the for loop is to eget
        for i in str:
            Dcrypt = Dcrypt + decrypt[encrypt.index(i)]
        return Dcrypt
    except ValueError:
        print("Invalid input.")

# this function will read and return the column USER_ID from TABLE TB_USER
def userlist():
    conn = sqlite3.connect('USER.db')
    cursor = conn.cursor()

    cursor.execute('SELECT USER_ID FROM TB_USER;')
    users = [row[0] for row in cursor.fetchall()]

    cursor.close()
    conn.close()

    return users

# this function are for users that already existed in table TB_USER
def existing_user():
    print("Returning user, type '1' if first time user to go back to the main menu and select '1'.")
    while True:
        try:
            username = input("Enter username: ")
            if username == '1':
                break
            assert username in userlist()
        except:
            print("Invalid username.")
            select()
        else:
            while True:
                try:
                    password = input("Enter password: ")
                    pword = password.upper()
                    pword = encrypting(pword)

                    conn = sqlite3.connect('USER.db')
                    cursor = conn.cursor()

                    cursor.execute('SELECT CRYPTOGRAPHIC_PASSWORD FROM TB_USER WHERE USER_ID = ?;', (username,))
                    save_pword = cursor.fetchall()[0][0] #return all rows of query result

                    assert pword == save_pword

                except:
                    print("Invalid password.")
                    cursor.close()
                    conn.close()

                    continue
                else:
                    print("Login successful.")
                    # the execution below will count the number on how many times the user logged in, default is zero and add 1 everytime the user log in
                    cursor.execute('UPDATE TB_USER SET Access_Count = Access_Count + 1 WHERE USER_ID = ?;', (username,))
                    conn.commit()
                    # the back up function will update the access count in usersdb-backup.csv
                    backup()
                    
                    cursor.execute('SELECT USER_ID, Access_Count FROM TB_USER WHERE USER_ID = ? AND CRYPTOGRAPHIC_PASSWORD = ?;',
                                   (username, pword))
                    values = cursor.fetchall()

                    cursor.close()
                    conn.close()

                    print("USER: {}  Access_Count: {} ".format(values[0][0], values[0][1]))
                    
                    break
            break

    select()

def new_user():
    print("Create user account.")
    while True:
        try:
            new_username = input("Enter username: ")

            if new_username =='no':
                break
            assert new_username not in userlist()
            email = input("Enter email address: ")
        except:
            print("User already exists. ")
            continue
        else:
            print("Create password. Type '1' if you wish to go back to the main menu.")
            while True:
                try:
                    crypt_pw = input("Enter password: ").upper()
                    if crypt_pw.upper() == '1':
                        break
                    spell_check(crypt_pw)
                except:
                    print("Invalid password. Do not use any symbol please. Try again.\n")
                    continue
                else:
                    crypt_pw = encrypting(crypt_pw)

                    conn = sqlite3.connect('USER.db')
                    cursor = conn.cursor()

                    cursor.execute('INSERT INTO TB_USER(USER_ID, CRYPTOGRAPHIC_PASSWORD, EMAIL) VALUES(?, ?, ?);', (new_username, crypt_pw, email))
                    conn.commit()

                    backup()
                    cursor.close()
                    conn.close()
                    print("Successfully registered.")
                    break
            break
    select()



def backup():
    try:
        # Connect to database
        conn = sqlite3.connect("USER.db")

        # Exporting data into CSV
        cursor = conn.cursor()
        cursor.execute("select * from TB_USER")
        with open("usersdb-backup.csv", "w") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter="\t")
            csv_writer.writerow([i[0] for i in cursor.description])
            csv_writer.writerows(cursor)

        dirpath = os.getcwd() + "/usersdb-backup.csv"
        print("Data exported Successfully into {}".format(dirpath))


    except Error as e:
        print(e)

    # Close database connection
    finally:
        conn.close()


def backup():
    try:
        # Connect to database
        conn = sqlite3.connect("USER.db")

        # Exporting data into CSV
        cursor = conn.cursor()
        cursor.execute("select * from TB_USER")

        with open("usersdb-backup.csv", "w") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter="\t")
            csv_writer.writerow([i[0] for i in cursor.description])
            csv_writer.writerows(cursor)

        dirpath = os.getcwd() + "/usersdb-backup.csv"
        print("Data exported Successfully into {}".format(dirpath))

    except Error as e:
        print(e)

    # Close database connection
    finally:
        conn.close()




if __name__ == "__main__":
    select()
