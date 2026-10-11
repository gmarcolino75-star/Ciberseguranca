# Projeto educacional de Cibersegurança
# Simulação de Ransomware em ambiente controlado
# ⚠️ Uso apenas para fins de estudo. Não utilizar em sistemas de terceiros sem autorização.

from pathlib import Path
from cryptography.fernet import Fernet, InvalidToken

# Localiza as pastas independentemente do terminal usado
PASTA_TESTES = Path(__file__).resolve().parent
ARQUIVO_CHAVE = PASTA_TESTES.parent / "chave.key"


def carregar_chave():
    if not ARQUIVO_CHAVE.is_file():
        raise FileNotFoundError(
            f"Chave não encontrada: {ARQUIVO_CHAVE}"
        )

    chave = ARQUIVO_CHAVE.read_bytes().strip()

    # Valida a chave antes de utilizá-la
    Fernet(chave)
    return chave


def descriptografar_arquivo(caminho, f):
    try:
        dados = caminho.read_bytes()

        # Tenta descriptografar sem alterar o arquivo original
        dados_originais = f.decrypt(dados)

        # Salva o conteúdo recuperado somente após sucesso
        caminho.write_bytes(dados_originais)

        print(f"[OK] Arquivo restaurado: {caminho.name}")

    except InvalidToken:
        print(
            f"[ERRO] {caminho.name}: token inválido. "
            "Verifique a chave ou se o arquivo já foi restaurado."
        )

    except OSError as erro:
        print(f"[ERRO] {caminho.name}: {erro}")


def main():
    try:
        chave = carregar_chave()
        f = Fernet(chave)

        print(f"Chave localizada: {ARQUIVO_CHAVE}")
        print(f"Pasta de testes: {PASTA_TESTES}")

        # Lista os arquivos diretamente na pasta de testes
        arquivos = [
            arquivo for arquivo in PASTA_TESTES.iterdir()
            if arquivo.is_file()
            and arquivo.name != Path(__file__).name
            and arquivo.suffix != ".key"
        ]

        if not arquivos:
            print("Nenhum arquivo de teste encontrado.")
            return

        for arquivo in arquivos:
            descriptografar_arquivo(arquivo, f)

    except (FileNotFoundError, ValueError) as erro:
        print(f"[ERRO] Não foi possível carregar a chave: {erro}")


if __name__ == "__main__":
    main()
