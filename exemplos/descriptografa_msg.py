from cryptography.fernet import Fernet

#carrega nossa chave marota na variavel chave
with open('chave.key', 'rb') as filekey:
    chave = filekey.read()
   
#Carrega o Fernet com a nossa chave 
fernet = Fernet(chave)

#Vai carregar a nossa mensagem criptografada
with open('mensagem.txt','rb') as arquivo_criptografado:
    criptografado = arquivo_criptografado.read()
    
#Descriptografar
descriptografa = fernet.decrypt(criptografado)

#reescrevemos a mensagem decriptografada pelo descriptografa e add no arquivo mensagem.txt
with open('mensagem.txt', 'wb') as arquivo_descriptografado:
    arquivo_descriptografado.write(descriptografa)

    