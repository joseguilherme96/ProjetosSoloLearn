#  Classe responsável por receber opções do usuário e acionar processos
import time # Classe de tempo
import Processo as processo # Classe responsável por gerenciar processos
import threading # Classe responsável por executar em segundo plano

class Menu:

    Processo = processo.Processo()
    processo_configurado = False
    opcao = None

    def __init__(self):

        # Função responsável por capturar os dados que o usuário digita
        self.menu()

        # Mostra opções menu para o usuário
        self.mostrar_opcoes_menu()

    # Função responsável por acionar processos de acordo com o o que o usuário digita
    def controlar_processos(self):

        # Executa se o usuário tiver digitado algo
        if self.opcao is not None:

            # Start Processo
            if self.opcao == 1:

                # Verifica se o processo foi configurado
                if self.processo_configurado:

                    if self.Processo.executar_processo():
                        print("Processo configurado !")
                        print("Digite 1 para começar o processo..")

                    else:

                        print("Processo Inexistente")

                    print("Processo sendo iniciado...")
                    print("Inicio Processo :", self.Processo.data_hora_inicio_processo)

                else:
                    print("O processo ainda não pode ser iniciado...ainda precisa ser configurado digite 5 para configurar agora")

            elif self.opcao == 2:

                self.Processo.pausar_processo()

            elif self.opcao == 4:

                if self.Processo.retomar_processo():

                    print("O processo foi retomado !")

            elif self.opcao == 3:

                self.Processo.parar_processo()

            # opção que configura processo que vai ser iniciado posteriormente
            elif self.opcao == 5:

                print("Digite o numero do processo que deseja fazer !")

                for numero_processo, nome_processo in self.Processo.processos.items():
                    print(numero_processo, nome_processo)

                self.opcao = None;

                entrada_usuario = False

                while self.opcao is None:
                    time.sleep(1)
                else:

                    while entrada_usuario == False:

                        if self.opcao is not None:

                            if self.Processo.configurar_processo(self.opcao) == False:

                                print("Processo Inválido !")
                                entrada_usuario = False
                                self.opcao = None

                            else:

                                entrada_usuario = True

                        else:

                            entrada_usuario = False

                self.processo_configurado = True

            else:

                print("Opção inválida, digite novamente start, pause ou stop")

        self.opcao = None

    def mostrar_opcoes_menu(self):

        print("Status Processo :", self.Processo.status_processo)
        print("""Digite 1 - start , 2 - pause, 3 - stop, 4 - retomar processo, 5 - configurar processo """)

    def opcao_usuario(self):

        while True:
            self.opcao = int(input())

            if self.opcao is not None:

                self.controlar_processos()


    # Função que inicia Threading para ficar capturando entradas do usuário
    def menu(self):

        self.opcao_usuario = threading.Thread(target=self.opcao_usuario)
        self.opcao_usuario.start()
