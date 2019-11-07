import tkinter as tk
from tkinter import filedialog
from Crypto.Hash import SHA256, SHA1, MD5
from collections import namedtuple
import os

class Questao01:

    MD5 = 0
    SHA_1 = 1
    SHA_256 = 2

    def __init__(self):
        self.texto = ''
        self.opcao = -1

    def selecionar_arquivo(self):
        root = tk.Tk()
        root.withdraw()
        caminho_arquivo = filedialog.askopenfilename()
        f = open(caminho_arquivo, mode="r", encoding="utf-8")
        self.texto = f.read()

    def escolher_algoritmo(self):
        while self.opcao < 0 or self.opcao > 2:
            self.opcao = int(
                input('Escolha um menu:\n\t0 - MD5\n\t1 - SHA-1\n\t2 - SHA-256\n'))

    def apresentar_informacoes(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Texto:', self.texto)
        retorno = self.cifrar()
        print(retorno.nome + ': ' + retorno.texto)

    def cifrar(self):
        Retorno = namedtuple('Retorno', ['nome', 'texto'])
        if self.opcao == self.MD5:
            return Retorno('MD5', self.cifrar_md5())
        elif self.opcao == self.SHA_1:
            return Retorno('SHA-1', self.cifrar_sha_1())
        else:
            return Retorno('SHA-256', self.cifrar_sha_256())

    def cifrar_md5(self):
        h = MD5.new()
        h.update(bytearray(self.texto, encoding="utf-8"))
        return h.hexdigest().upper()

    def cifrar_sha_1(self):
        h = SHA1.new()
        h.update(bytearray(self.texto, encoding="utf-8"))
        return h.hexdigest().upper()

    def cifrar_sha_256(self):
        h = SHA256.new()
        h.update(bytearray(self.texto, encoding="utf-8"))
        return h.hexdigest().upper()


if __name__ == "__main__":
    q = Questao01()
    q.selecionar_arquivo()
    q.escolher_algoritmo()
    q.apresentar_informacoes()
