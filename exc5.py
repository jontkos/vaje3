# Instructions
import time
import random
# Create a program that represents a football bet.
# The program needs to have a list of football matches, where for every match user should input
# the end result. There needs to be at least 5 matches. Example of input:
# (programs output) Liverpool : CSKA ?
# (user's input) 1-0
# (programs output) Bate Borisov : Partizan  ?
#  ....
tekme = ["Brinje : Arne Tabor", "Zagorje : Ivancna Gorica", "Sencur : Komenda", "Kranj : Kolpa", "Kocevje : Rudar Trbovlje"]
#
tvoj_vnos = []
for i in (tekme):
      print(i)
      rezultat_tekme = (tvoj_vnos.append(input(str("Vnesi rezultat:"))))

#time.sleep(10)

def generate_random_number():
    return (random.randint(0,5))

izidi = []
import re

denar=0


for i in range(len(tekme)):
    izidi.append(str(generate_random_number())+"-"+str(generate_random_number()))
    print("Actual game: " + tekme[i] +" "+ izidi[i])
    print("Your bet: " + tvoj_vnos[i])
    if (izidi[i][0] == tvoj_vnos[i][0]) and (izidi[i][2] == tvoj_vnos[i][2]):
        denar +=10
        print("\n!!!!!!!!Winner winner chicken dinner. +10€€€€€!!!!!!!!!\n")
    else:
        denar -=1
        print("You lose -1€\n")
print("Your wallet= " + str(denar)+"€")
# After user inputs all the results, program waits for 10 seconds and prints the result of matches.
# Results are totally random, you can say that max. goals by one team is 5.
# After results are displayed, program should output, how well were the bets.
# For every correctly guessed match, user gets 10€, for every incorrect user loses 1€
# Example of output:
# Actual game: Liverpool : CSKA 3-0.
# Your bet: 1-0
# You lose 1€
# ....
# --------------
# You earned -5€.
