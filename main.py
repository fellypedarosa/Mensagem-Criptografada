from cryptography.fernet import Fernet

# Função para criptografar mensagem
def criptografa_msg(mensagem, chave):
    fernet = Fernet(chave)
    return fernet.encrypt(mensagem.encode())

# Função para descriptografar mensagem
def descriptografa_msg(mensagem_criptografada, chave):
    fernet = Fernet(chave)
    return fernet.decrypt(mensagem_criptografada).decode()

# Função para enviar mensagem
def enviar_mensagem(mensagem, chave):
    mensagem_criptografada = criptografa_msg(mensagem, chave)
    with open("mensagem.txt", "ab") as file:
        file.write(mensagem_criptografada + b"\n")
    print("Mensagem enviada!")

# Função para ler mensagem
def ler_mensagem(chave):
    try:
        with open("mensagem.txt", "rb") as file:
            conteudo = file.readlines()
            if conteudo:
                print("Mensagens:")
                for mensagem_criptografada in conteudo:
                    mensagem = descriptografa_msg(mensagem_criptografada.strip(), chave)
                    print(mensagem)
            else:
                print("O arquivo está vazio.")
    except FileNotFoundError:
        print("O arquivo mensagem.txt não foi encontrado. Envie uma mensagem primeiro.")

# Função principal
def main():
    # Carrega a chave
    with open('chave.key', 'rb') as filekey:
        chave = filekey.read()

    while True:
        opcao = input("Você quer enviar, ler, limpar o histórico ou sair? (digite enviar, ler, limpar ou sair): ").strip().lower()
        
        if opcao == 'enviar':
            mensagem = input("Digite sua mensagem: ").strip()
            enviar_mensagem(mensagem, chave)
        
        elif opcao == 'ler':
            ler_mensagem(chave)
        
        elif opcao == 'limpar':
            confirmacao = input("Tem certeza que deseja limpar o histórico? (sim/não): ").strip().lower()
            if confirmacao == 'sim':
                with open("mensagem.txt", "wb") as file:
                    file.truncate(0)
                print("Histórico limpo com sucesso.")
            else:
                print("Operação de limpeza cancelada.")
        
        elif opcao == 'sair':
            print("Saindo do programa.")
            break
        
        else:
            print("Escolha inválida. Por favor, digite enviar, ler, limpar ou sair.")


if __name__ == "__main__":
    main()
