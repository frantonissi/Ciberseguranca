import hashlib
def verificar_login(nome_digitado, senha_digitada):
    
    hash_Francisco = "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4"
    hash_Maria = "dbff5341acad5e2a58db4efd5e72e2d9a0a843a28e02b1183c68162d0a3a3de6"


# 2. O "liquidificador" (SHA-256)
#    - .encode() transforma a string em bytes
#    - hashlib.sha256() processa esses bytes
#    - .hexdigest() nos dá a "vitamina" (o hash) em texto
    hash_gerado = hashlib.sha256(senha_digitada.encode('utf-8')).hexdigest()

#print(f"A senha vira este hash:")
#print(hash_gerado)

    nivel_acesso = ""

    if(nome_digitado == "Francisco" and hash_gerado == hash_Francisco):
        return "admin"
    
    elif(nome_digitado == "Maria" and hash_gerado == hash_Maria ):
        return "user"
    
    else:
        return ""
#                           ///////////FIM DA FUNCAO////////////// 

def deletar_usuarios():
    print("---------------------------------")
    print("!! ALERTA ADMIN !!")
    print("...DELETANDO TODOS OS USUÁRIOS...")
    print("---------------------------------")

def ver_perfil():
    print("---------------------------------")
    print(">> PERFIL DO USUÁRIO <<")
    print("Nome: Maria")
    print("Email: maria@email.com")
    print("---------------------------------")

nome = input("Qual é o seu nome? ")
senha = input("Digite a senha: ")
nivel_acesso = verificar_login(nome, senha)
    
if (nivel_acesso == "admin"):
    
    deletar_usuarios()
    
elif(nivel_acesso == "user"):
    
    ver_perfil()
    
else:
        print("ACESSO NEGADO (Usuário ou senha incorretos)")
    
    