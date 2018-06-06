import time
import random

tekme = ["Brinje : Arne Tabor", "Zagorje : Ivancna Gorica", "Sencur : Komenda", "Kranj : Kolpa", "Kocevje : Rudar Trbovlje"]
#
tvoj_vnos = []
for i in (tekme):
      # this works fine, but since you dont need elements from tekme but only how many times to ask, this line would be appropriate:
      # for i in range(len(tekme)):
      print(i)
      rezultat_tekme = (tvoj_vnos.append(input(str("Vnesi rezultat:"))))
      # rezultat tekme is never used, you can totally omit it
      # input returns string anyway so the line below does the same, but is much simpler
#       tvoj_vnos.append(input("Vnesi rezultat:"))
#     since max 5 goals can be scored by a team, user should know that so input more than  would be rejected or re-asked.

#time.sleep(10)

def generate_random_number():
    return (random.randint(0,5))
# since you actually need string, you could do the string() casting here, so when you use it, you hide complexity.
#   return str(random.randint(0,5))

izidi = []
import re

denar=0


for i in range(len(tekme)):
    izidi.append(str(generate_random_number())+"-"+str(generate_random_number()))
    # since you use generated result in the same loop, there is no need for izidi array.
    # you could just save the generated result to variable and use this variable below.
    print("Actual game: " + tekme[i] +" "+ izidi[i])
    print("Your bet: " + tvoj_vnos[i])
    if (izidi[i][0] == tvoj_vnos[i][0]) and (izidi[i][2] == tvoj_vnos[i][2]):
        denar +=10
        print("\n!!!!!!!!Winner winner chicken dinner. +10€€€€€!!!!!!!!!\n")
    else:
        denar -=1
        print("You lose -1€\n")


print("Your wallet= " + str(denar)+"€")


