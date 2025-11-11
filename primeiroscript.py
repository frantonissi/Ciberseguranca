import hashlib

hash_Francisco = "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4"
hash_Maria = "dbff5341acad5e2a58db4efd5e72e2d9a0a843a28e02b1183c68162d0a3a3de6"

nome = input("Qual é o seu nome? ")
senha = input("Digite a senha: ")

# 2. O "liquidificador" (SHA-256)
#    - .encode() transforma a string em bytes
#    - hashlib.sha256() processa esses bytes
#    - .hexdigest() nos dá a "vitamina" (o hash) em texto
hash_gerado = hashlib.sha256(senha.encode('utf-8')).hexdigest()

print(f"A senha vira este hash:")
print(hash_gerado)

if(nome == "Francisco" and hash_gerado == hash_Francisco):
    print("senha correta, acesso permitido")
elif(nome == "Maria" and hash_gerado == hash_Maria ):
    print("senha correta, acesso permitido")
else:
    print("acesso negado")