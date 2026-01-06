import hashlib

senha_digitada = "1234"

hash_roubado = hashlib.sha256(senha_digitada.encode('utf-8')).hexdigest()

# O hash que "roubámos" do sistema (sabemos que é "1234")
hash_roubado = "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4"

# "r" significa 'read' (ler)
with open("senhas.txt", "r") as f: 
        for linha in f:    #for <variavel_temporaria> in <sequencia>:
            if(hashlib.sha256(linha.strip().encode('utf-8')).hexdigest() == hash_roubado): #strip serve para limpar o restante da linha no txt
                print (linha.strip())
                break
            