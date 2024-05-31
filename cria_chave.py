from cryptography.fernet import Fernet


chave = Fernet.generate_key()

#Aqui cria a chave e add no aruivo de chave
with open ('chave.key', 'wb') as filekey:
    filekey.write(chave)
    
