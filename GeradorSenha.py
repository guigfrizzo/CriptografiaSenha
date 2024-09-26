print('\nEsse é um gerador de senhas que as gera a partir de criptografia pesada!\n')

def validar_tamanho_senha(chave):
    if len(chave) < 8:
        print('A senha deve ter pelo menos 8 caracteres.')
        return False
    return True

def gerar_senha(chave):
    senha = ""
    for letra in chave:
        if letra in "Aa": senha += "1"
        elif letra in "Bb": senha += "$"
        elif letra in "Cc": senha += "2"
        elif letra in "Dd": senha += "3"
        elif letra in "Ee": senha += "4"
        elif letra in "Ff": senha += "5"
        elif letra in "Gg": senha += "16"
        elif letra in "Hh": senha += "17"
        elif letra in "Ii": senha += "18"
        elif letra in "Jj": senha += "19"
        elif letra in "Kk": senha += "20"
        elif letra in "Rr": senha += "#"
        elif letra in "Ss": senha += "%"
        elif letra in "Mm": senha += "@"
        else:
            senha += letra
    return senha

def main():
    chave = input('Digite a base da sua senha: ')

    if not validar_tamanho_senha(chave):
        return

    senha_gerada = gerar_senha(chave)
    print(f'Senha gerada: {senha_gerada}')

    opcao = input('Deseja ver a chave da senha novamente?\nDigite 1 para sim | Digite 2 para não\n')
    
    if opcao == '1':
        print(f'Chave: {chave}')
    elif opcao == '2':
        print('Encerrando.')
    else:
        print('Opção inválida.')

if __name__ == "__main__":
    main()
