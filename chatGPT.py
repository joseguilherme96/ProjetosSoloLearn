import time,openai

openai.api_key = "TODO" # Cadastrar chave no site e inserir aqui para que o programa funcione ! https://platform.openai.com/account/api-keys

def mensagem(mensagem):

    respostaAPI = openai.ChatCompletion.create(

        model = "gpt-3.5-turbo",
        messages=[

            {
                'role':'system',
                'content':'Você vai conversar comigo sobre qualquer assunto'
            },
            {
                'role':'user',
                'content':mensagem
            }
        ]
    )

    return respostaAPI.choices[0].message.content

try:

    print('Para sair do chat digite "sair"')

    chat = True
    while chat:

        mensagem_user = input()

        if mensagem_user == 'sair':
            chat = False
        else:
            chatGPT = mensagem(mensagem_user)

            for letra in chatGPT:

                if letra == "\n":

                    print()

                else:

                    print(letra,end="")

                time.sleep(0.05)

            print()


except KeyboardInterrupt:

        print("Execução Finalizada !")
else:
        print("Execução Finalizada !")
