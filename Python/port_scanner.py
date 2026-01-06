import socket

alvo = "127.0.0.1"


def scan(alvo_para_testar, porta_para_testar):
    """
        alvo_para_testar: hostname ou IP alvo (str)
        porta_para_testar: número da porta (int)

    Retorna 1 se a porta estiver aberta, 0 caso contrário.
    s: É a nossa variável, o nosso "telefone".

socket.socket(): Estamos pedindo um "telefone" novo.
socket.AF_INET: Dizendo que vamos ligar para um endereço de Internet (um IP).
socket.SOCK_STREAM: Dizendo que vamos usar o protocolo TCP (uma "ligação" confiável, que avisa se o outro lado atendeu).s: É a nossa variável, o nosso "telefone".
socket.socket(): Estamos pedindo um "telefone" novo.
socket.AF_INET: Dizendo que vamos ligar para um endereço de Internet (um IP).
socket.SOCK_STREAM: Dizendo que vamos usar o protocolo TCP (uma "ligação" confiável, que avisa se o outro lado atendeu).
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        s.connect((alvo_para_testar, porta_para_testar))
        s.close()
        return 1

    except socket.error:
        return 0

print(f"Testando {alvo} na porta {range(1,101)}...")

for i in range(1, 101):

    porta_esta_aberta = scan(alvo, i)

    if (porta_esta_aberta):
        print(f"A porta {i} esta aberta")
        resultado = str(i)
        with open("portas_abertas.txt", "a") as f:
            f.write(resultado + "\n")
    else:
        print(f"A porta {i} esta fechada")
        
    