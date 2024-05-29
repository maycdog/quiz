from tkinter import *
janela = Tk()
texto_creditos = Label(janela, text="https://github.com/maycdog")
texto_creditos.grid(column=0, row=0)
janela.mainloop()

Loop_Recomeço = 0
while Loop_Recomeço == 0:
    # COMEÇANDO
    print("Seja muito bem-vindo ao quiz do Maycon!")
    answer_user = input("Quer começar? (S/N) ")

    if answer_user != "S" and answer_user != "s":
        quit()

    print("Começando... \n")

    score = 0

    # PERGUNTA 1 (FORMA INVERSA)
    r1 = input("Qual não é o meu nome? \n")
    if r1 == "Maycon" or r1 == "MAYCON":
        print("Perdeu de primeira, pelo amor viu")
        print("PONTUAÇÃO FINAL: ", score)
        quit()

    print("BOA!!! a partir de agora será com alternativas! ex.: (A),(B),(C)... \n")
    print("... \n")
    score = score + 1

    # PERGUNTA 2
    print("Quem foi o primeiro presidente negro dos Estados Unidos? \n (A) Dao Thi Uyen \n (B) Barack Obama \n (C) Biden \n (D) Kevin Durant \n ")
    r2 = input("R: ")
    if r2 == "B" or r2 == "b":
        print("CORRETO! \n")
        score = score + 1
    else:
        print("INCORRETO! \n")
        print("PONTUAÇÃO: ", score)
        quit()

    # PERGUNTA 3
    print("Quem foi o campeão da bola de ouro em 2004? \n (A) Cristiano Ronaldo \n (B) Pavel Nedved \n (C) Luis Fabiano \n (D) Andriy Shevchenko \n ")
    r3 = input("R: ")
    if r3 == "D" or r3 == "d":
        print("CORRETO! \n")
        score = score + 1
    else:
        print("INCORRETO! \n")
        print("PONTUAÇÃO: ", score)
        quit()

    # PERGUNTA 4
    print("Qual nome verdadeiro do MC POZE? \n (A) Marlon Brandon Coelho Couto Silva \n (B) Angelo Costa Coelho \n (C) Fernando de Noronha \n (D) Riquelmy da Silva Santos \n ")
    r4 = input("R: ")
    if r4 == "A" or r4 == "a":
        print("CORRETO! \n")
        score = score + 1
    else:
        print("INCORRETO! \n")
        print("PONTUAÇÃO: ", score)
        quit()

    # PERGUNTA 5
    print("Quem é a desenvolvedora do jogo God Of War? \n (A) Santa Monica Studio \n (B) Xbox 360 \n (C) Sony \n (D) Electronic Arts \n ")
    r5 = input("R: ")
    if r5 == "A" or r5 == "a":
        print("CORRETO! \n")
        score = score + 1
    else:
        print("INCORRETO! \n")
        print("PONTUAÇÃO: ", score)
        quit()

    # PERGUNTA 6
    print("Qual clube foi campeão da Copa Roblox 2023? \n (A) Botafogo \n (B) Corinthians \n (C) São Paulo \n (D) River Plate \n ")
    r6 = input("R: ")
    if r6 == "A" or r6 == "a":
        print("CORRETO! \n")
        score = score + 1
    else:
        print("INCORRETO! \n")
        print("PONTUAÇÃO: ", score)
        quit()

    # FIM
    print(
        f"┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\n PARABÉNS! FIM DO QUIZ!   ...  PONTUAÇÃO TOTAL: {score} \n┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\n")
    print("RECOMEÇANDO...")
