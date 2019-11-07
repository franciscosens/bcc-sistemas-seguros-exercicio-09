import tkinter as tk
from tkinter import filedialog

class Questao01:

    MD5 = 0
    SHA_1 = 1
    SHA_256 = 2

    def __init__(self):
        self.texto = ''
        self.selecionar_arquivo()
        self.escolher_algoritmo()

    def selecionar_arquivo(self):
        root = tk.Tk()
        root.withdraw()
        caminho_arquivo = filedialog.askopenfilename()
        f = open(caminho_arquivo, mode="r", encoding="utf-8")
        self.texto = f.read()

    def escolher_algoritmo(self):
        opcao = -1
        while opcao < 0 or opcao > 2:
            opcao = int(input('Escolha um menu:\n\t0 - MD5\n\t1 - SHA-1\n\t2 - SHA-256\n'))

        if opcao == self.MD5:
            print("MD5:", self.cifrar_md5())
        elif opcao == self.SHA_1:
            print("SHA-1:", self.cifrar_sha_1())
        elif opcao == self.SHA_256:
            print("SHA-256:", self.cifrar_sha_256)

    def cifrar_md5(self):
        return ''

    def cifrar_sha_1(self):
        return ''

    def cifrar_sha_256(self):
        return ''

if __name__ == "__main__":
    q = Questao01()