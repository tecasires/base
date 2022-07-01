import modules.ask as ask


def pro_name():

    al_up_chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    al_lo_chars = []
    al_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    al_signs = ['-', '_']

    for char in al_up_chars:
        al_lo_chars.append((char.lower()))

    al_chars = al_up_chars + al_lo_chars + al_num + al_signs

    opt = False

    while opt is False:

        name = input('\nIntroduzca el nombre del proyecto a crear: ')
        proj_name = []
        
        for cha in name:

            if cha not in al_chars:
                print('\nCarácter', cha, 'no permitido.')

            else:
                proj_name.append(cha.lower())

        val_proj_name = "".join(proj_name)
        print('\nEl nombre del proyecto será: ', val_proj_name)

        print('\nLe sirve el nombre? ')
        sel = ask.value_dec()

        if sel == True:
            
            opt = True

        else:
            opt == False
            
    
    return  val_proj_name
