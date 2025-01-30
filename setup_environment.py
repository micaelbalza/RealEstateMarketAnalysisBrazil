import os
import subprocess
import sys

def run_command(command):
    """Função para executar comandos no terminal."""
    process = subprocess.run(command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if process.returncode != 0:
        print(f"Erro ao executar: {command}\n{process.stderr}")
        sys.exit(1)
    print(process.stdout)

def main():
    print("Configuração automática do ambiente virtual iniciada...")

    # Passo 1: Criar o ambiente virtual
    env_dir = "env"
    if not os.path.exists(env_dir):
        print("Criando o ambiente virtual...")
        run_command(f"python -m venv {env_dir}")
    else:
        print("Ambiente virtual já existe.")

    # Passo 2: Ativar o ambiente virtual e instalar as dependências
    activate_script = os.path.join(env_dir, "Scripts", "activate") if os.name == "nt" else f"source {env_dir}/bin/activate"
    pip_install = f"{activate_script} && pip install --upgrade pip && pip install -r requirements.txt"

    print("Instalando bibliotecas no ambiente virtual...")
    run_command(pip_install)

    # Passo 3: Adicionar o kernel do Jupyter Lab
    kernel_install = f"{activate_script} && python -m ipykernel install --user --name env --display-name 'Python-env'"
    print("Registrando o ambiente virtual no Jupyter Lab...")
    run_command(kernel_install)

    print("Configuração concluída com sucesso!")

if __name__ == "__main__":
    main()
