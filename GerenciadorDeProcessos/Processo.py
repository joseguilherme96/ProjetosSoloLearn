import time
from datetime import datetime

class Processo:

    numero_processo = 0
    data_hora_inicio_processo = 0
    data_hora_fim_processo = 0
    processo_configurado = False
    status_processo = "Não Iniciado"
    executando_processo = False
    codigo_processo = 0

    processos = {

        1: {'nome_processo': "Fabricação da Roda Carro GOl", 'tempo_fabricacao': 30},
        2: {'nome_processo': "Fabricação da Porta Dianteira", 'tempo_fabricacao': 30}

    }

    def __init__(self):

        self.status_processo = 'Não iniciado'

    # Fução responsável por configurar processo que irá ser executado
    def configurar_processo(self, codigo_processo):

        try:

            self.numero_processo = codigo_processo;

            self.processo_configurado = True

            self.codigo_processo = self.processos[codigo_processo]

        except KeyError:

            self.processo_configurado = False;

            return False

    # Função responsável por iniciar processo
    def executar_processo(self):

        if self.processo_configurado:

            time.sleep(5)
            self.data_hora_inicio_processo = datetime.today()
            self.status_processo = "Em execução..."
            self.executando_processo = True

            return True

        else:
            print("O processo precisa ser configurado !")

            return False

    def pausar_processo(self):

        self.status_processo = "Pausado"
        self.executando_processo = False

    def parar_processo(self):

        self.status_processo = "Interrompido"

    def retomar_processo(self):

        self.status_processo = "Retomado"

        return True

