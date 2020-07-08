import random as rnd
import sqlite3
import getpass as gpass

VAULT_PASS = "GrandioseGoPro"

word = gpass.getpass()

while word != VAULT_PASS:
    if word == "q":
        break
    word = input("What is your password?\n")
    

conn = sqlite3.connect('NotVault.db')
c = conn.cursor()

if word == VAULT_PASS:   
    
    while True:
        print()
        print("**************************")
        print( "Options:" )
        print( "g: Get a Password")
        print( "r: Retrieve a Password" )
        print( "d: Delete a Password")
        print( "q: Quit" )
        print("**************************")

        try:
            c.execute("CREATE TABLE IF NOT EXISTS pass (Website TEXT, Password TEXT)")
            conn.commit()
            print("Your Vault has been created!")
        except:
            print("You already have a Vault!")
            continue

        opt=input( "Enter the option:" )
        print()

        
        if opt == "g":
            website = input("Enter the Website's name \n")
            website = website.capitalize()
            password_length = 15
            chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890@#$%*()_-+="
            x = ''
            for i in range(0,15):
                a = rnd.choice(chars)
                x += a
            print(x)
            
            c.execute('INSERT INTO pass VALUES(?,?)',[website,x])
            conn.commit()

        if opt == "r":
            website = input("Enter the Website's name \n")
            website = website.capitalize()
            c.execute("SELECT password FROM pass WHERE Website = ?",(website,))
            try:
                pwd = c.fetchone()
                pwd = list(pwd)
                print()
                print("Password for",website,'is:',(pwd))
            except:
                print("NO PASSWORD FOR:",website)
                continue

        if opt == "d":
            website = input("Enter the Website's name \n")
            website = website.capitalize()
            c.execute("DELETE FROM pass WHERE website=(?)",[website,])
            conn.commit()    
        
        if opt == "q":
            break
