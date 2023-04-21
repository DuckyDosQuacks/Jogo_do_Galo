# Importar Bibliotecas
from tkinter import *
from tkinter import messagebox as mb

# Criar Janela
root = Tk()

# Propriedades da Janela
root.title('Jogo do Galo')
root.resizable(False, False)

# Inicializar Variáveis
turn = True
winner = False
move_cont = 0

# Criar Menu da Janela
window_menu = Menu(master=root)
root.configure(menu=window_menu)

# Funções do Jogo
def ButtonPressed(button):
    global turn
    global move_cont

    if button['text'] == '':
        if turn:
            button['text'] = 'X'

            move_cont += 1

            CheckForWinner()
            CheckForTie()

            turn = False
        else:
            button['text'] = 'O'

            move_cont += 1

            CheckForWinner()
            CheckForTie()

            turn = True
    else:
        mb.showerror('Jogo do Galo', 'Essa posição já está em uso!')

def CheckForWinner():
    global winner

    ################
    ## HORIZONTAL ##
    ################
    if button1['text'] == button2['text'] == button3['text'] and button1['text'] != '':

        button1['bg'] = 'red'
        button2['bg'] = 'red'
        button3['bg'] = 'red'

        if button1['text'] == 'X':
            EndGame()
            mb.showinfo('Jogo do Galo', 'O jogador X ganhou!')
            winner = True
        elif button1['text'] == 'O':
            EndGame()
            mb.showinfo('Jogo do Galo', 'O jogador O ganhou!')
            winner = True

    elif button4['text'] == button5['text'] == button6['text'] and button4['text'] != '':

        button4['bg'] = 'red'
        button5['bg'] = 'red'
        button6['bg'] = 'red'

        if button4['text'] == 'X':
            EndGame()
            mb.showinfo('Jogo do Galo', 'O jogador X ganhou!')
            winner = True
        elif button4['text'] == 'O':
            EndGame()
            mb.showinfo('Jogo do Galo', 'O jogador O ganhou!')
            winner = True
    
    elif button7['text'] == button8['text'] == button9['text'] and button7['text'] != '':

        button7['bg'] = 'red'
        button8['bg'] = 'red'
        button9['bg'] = 'red'

        if button7['text'] == 'X':
            EndGame()
            mb.showinfo('Jogo do Galo', 'O jogador X ganhou!')
            winner = True
        elif button7['text'] == 'O':
            EndGame()
            mb.showinfo('Jogo do Galo', 'O jogador O ganhou!')
            winner = True

    ##############
    ## VERTICAL ##
    ##############
    if button1['text'] == button4['text'] == button7['text'] and button1['text'] != '':

        button1['bg'] = 'red'
        button4['bg'] = 'red'
        button7['bg'] = 'red'

        if button1['text'] == 'X':
            EndGame()
            mb.showinfo('Jogo do Galo', 'O jogador X ganhou!')
            winner = True
        elif button1['text'] == 'O':
            EndGame()
            mb.showinfo('Jogo do Galo', 'O jogador O ganhou!')
            winner = True

    elif button2['text'] == button5['text'] == button8['text'] and button2['text'] != '':

        button2['bg'] = 'red'
        button5['bg'] = 'red'
        button8['bg'] = 'red'

        if button2['text'] == 'X':
            EndGame()
            mb.showinfo('Jogo do Galo', 'O jogador X ganhou!')
            winner = True
        elif button2['text'] == 'O':
            EndGame()
            mb.showinfo('Jogo do Galo', 'O jogador O ganhou!')
            winner = True
    
    elif button3['text'] == button6['text'] == button9['text'] and button3['text'] != '':

        button3['bg'] = 'red'
        button6['bg'] = 'red'
        button9['bg'] = 'red'

        if button3['text'] == 'X':
            EndGame()
            mb.showinfo('Jogo do Galo', 'O jogador X ganhou!')
            winner = True
        elif button3['text'] == 'O':
            EndGame()
            mb.showinfo('Jogo do Galo', 'O jogador O ganhou!')
            winner = True

    ##############
    ## DIAGONAL ##
    ##############
    if button1['text'] == button5['text'] == button9['text'] and button1['text'] != '':

        button1['bg'] = 'red'
        button5['bg'] = 'red'
        button9['bg'] = 'red'

        if button1['text'] == 'X':
            EndGame()
            mb.showinfo('Jogo do Galo', 'O jogador X ganhou!')
            winner = True
        elif button1['text'] == 'O':
            EndGame()
            mb.showinfo('Jogo do Galo', 'O jogador O ganhou!')
            winner = True

    elif button3['text'] == button5['text'] == button7['text'] and button3['text'] != '':

        button3['bg'] = 'red'
        button5['bg'] = 'red'
        button7['bg'] = 'red'

        if button3['text'] == 'X':
            EndGame()
            mb.showinfo('Jogo do Galo', 'O jogador X ganhou!')
            winner = True
        elif button3['text'] == 'O':
            EndGame()
            mb.showinfo('Jogo do Galo', 'O jogador O ganhou!')
            winner = True

def CheckForTie():
    global move_cont

    if move_cont == 9 and winner == False:
        EndGame()
        mb.showinfo('Jogo do Galo', 'Empate!')

def EndGame():
    button1['state'] = 'disabled'
    button2['state'] = 'disabled'
    button3['state'] = 'disabled'
    button4['state'] = 'disabled'
    button5['state'] = 'disabled'
    button6['state'] = 'disabled'
    button7['state'] = 'disabled'
    button8['state'] = 'disabled'
    button9['state'] = 'disabled'

def RestartGame():
    # Reeniciar Estado do Botão
    button1['state'] = 'normal'
    button2['state'] = 'normal'
    button3['state'] = 'normal'
    button4['state'] = 'normal'
    button5['state'] = 'normal'
    button6['state'] = 'normal'
    button7['state'] = 'normal'
    button8['state'] = 'normal'
    button9['state'] = 'normal'

    # Reeniciar Cor do Botão
    button1['bg'] = 'SystemButtonFace'
    button2['bg'] = 'SystemButtonFace'
    button3['bg'] = 'SystemButtonFace'
    button4['bg'] = 'SystemButtonFace'
    button5['bg'] = 'SystemButtonFace'
    button6['bg'] = 'SystemButtonFace'
    button7['bg'] = 'SystemButtonFace'
    button8['bg'] = 'SystemButtonFace'
    button9['bg'] = 'SystemButtonFace'

    # Limpar Texto do Botão
    button1['text'] = ''
    button2['text'] = ''
    button3['text'] = ''
    button4['text'] = ''
    button5['text'] = ''
    button6['text'] = ''
    button7['text'] = ''
    button8['text'] = ''
    button9['text'] = ''

    # Reeniciar Vencedor
    global winner
    winner = False

    # Reeniciar Contador de Jogadas
    global move_cont
    move_cont = 0

# Criar Botões
button1 = Button(master=root, text='', font=('Monserrat', 14), width=8, height=4, command=lambda: ButtonPressed(button1))
button2 = Button(master=root, text='', font=('Monserrat', 14), width=8, height=4, command=lambda: ButtonPressed(button2))
button3 = Button(master=root, text='', font=('Monserrat', 14), width=8, height=4, command=lambda: ButtonPressed(button3))

button4 = Button(master=root, text='', font=('Monserrat', 14), width=8, height=4, command=lambda: ButtonPressed(button4))
button5 = Button(master=root, text='', font=('Monserrat', 14), width=8, height=4, command=lambda: ButtonPressed(button5))
button6 = Button(master=root, text='', font=('Monserrat', 14), width=8, height=4, command=lambda: ButtonPressed(button6))

button7 = Button(master=root, text='', font=('Monserrat', 14), width=8, height=4, command=lambda: ButtonPressed(button7))
button8 = Button(master=root, text='', font=('Monserrat', 14), width=8, height=4, command=lambda: ButtonPressed(button8))
button9 = Button(master=root, text='', font=('Monserrat', 14), width=8, height=4, command=lambda: ButtonPressed(button9))

# Posicionar Botões
button1.grid(column=0, row=0)
button2.grid(column=1, row=0)
button3.grid(column=2, row=0)

button4.grid(column=0, row=1)
button5.grid(column=1, row=1)
button6.grid(column=2, row=1)

button7.grid(column=0, row=2)
button8.grid(column=1, row=2)
button9.grid(column=2, row=2)

# Criar Menu de Opções
options_menu = Menu(master=window_menu, tearoff=False)
window_menu.add_cascade(label='Jogo', menu=options_menu)
options_menu.add_command(label='Recomeçar', command=RestartGame)
options_menu.add_command(label='Sair', command=exit)

# Main Loop
root.mainloop()
