import ctypes

#salvar em hexadecimal o arquivo
atributo_ocultar = 0x02

pasta = input("Digite o caminho da pasta")

retorno = ctypes.windll.kernel32.SetFileAttributesW(pasta, atributo_ocultar)

if retorno:
    print("Arquivo foi ocultado")
else:
    print("Arquivo não foi ocultado")