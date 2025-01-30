userInput = input("Insert your score here // Inserisci qui il tuo punteggio: ")
def give_grade():
    num = float(userInput)
    if num >= 90:
        print("A 90-100")
    elif num >= 80:
        print("b 80-90")
    elif num >= 70:
        print("C 70-80")
    elif num >= 60:
        print("D 60-70")
    else:
        print("F")


try:
  give_grade()
except:
    print("You must insert a number between 0 and 100. Use a period to separate decimals. // Inserire un numero compreso tra 0 e 100. Usa il punto per separare i decimali.")
    
