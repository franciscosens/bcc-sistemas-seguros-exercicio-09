from questao01 import Questao01
import os

class Questao02:
    def __init__(self):
        questao01 = Questao01()
        questao01.selecionar_arquivo()
        questao01.escolher_algoritmo()
        retorno = questao01.cifrar()
        texto_cifrado = retorno.texto

        texto_cifrado_original = input('Digite o hash para ser validado: ')

        os.system('cls' if os.name == 'nt' else 'clear')
        print('Texto: ',  questao01.texto)
        print('Hash cifrado:\t', texto_cifrado)
        print('Hash original:\t', texto_cifrado_original)

        if texto_cifrado == texto_cifrado_original:
            print('Arquivo integro')
        else:
            print('Quebra da integridade do arquivo')


if __name__ == "__main__":
    q = Questao02()