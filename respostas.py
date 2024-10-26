from random import choice, randint

piadas = [
            'Qual é o contrário de volátil? Vem cá sobrinho!',
            'Por que a vaca foi para o espaço? Para encontrar o vácuo!',
            'Por que o livro de matemática ficou triste? Porque ele tinha muitos problemas!',
            'O que o pato disse para a pata? Vem quá!',
            'Por que o computador foi preso? Porque ele executou um programa!',
        ]

desculpas = [
                'Desculpe, não entendi isso.',
                'Você poderia reformular?',
                'Não tenho certeza do que você quis dizer com isso.'
            ]

def obter_resposta(entrada_usuario: str):
    mensagem = entrada_usuario.lower()
    
    if mensagem == '':
        return 'Ué? Você tá aí?'
    elif 'olá' in mensagem or 'oi' or 'opa' in mensagem:
        return 'Olá! Como você está?'
    elif 'Tudo bem?' in mensagem:
        return 'Estou bem, obrigado por perguntar!'
    elif 'bem' in mensagem or 'ótimo' or 'tudo bem' in mensagem:
        return 'Que bom saber!'
    elif 'mal' in mensagem or 'terrível' in mensagem:
        return 'Sinto muito ouvir isso. Como posso ajudar?'
    elif 'jogar dado' in mensagem:
        return 'Você rolou um ' + str(randint(1, 6)) + '!'
    elif 'cara ou coroa' in mensagem:
        return 'Você tirou ' + choice(['cara', 'coroa']) + '!'
    elif 'piada' in mensagem:
        return choice(piadas)
    else:
        return choice(desculpas)