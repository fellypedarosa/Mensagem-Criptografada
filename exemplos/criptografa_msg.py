from cryptography.fernet import Fernet

# Aqui ele vai pegar o coneudo do arquivo de chave (a chave) e colocar na variavel chave

with open('chave.key', 'rb') as filekey:
    chave = filekey.read()
    
# Inicia o Fernet usando a chave
fernet = Fernet(chave)

#Vai carregar o nosso arquivo de mensagem
with open('mensagem.txt', 'rb') as arquivo:
    conteudo_mensagem = arquivo.read()
    
#Aqui criptografamos a mensagem, azar
criptografa = fernet.encrypt(conteudo_mensagem)

with open('mensagem.txt', 'wb') as mensagem_criptografada:
    mensagem_criptografada.write(criptografa)
    
    