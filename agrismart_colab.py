"""
AgriSmart - Sistema Multiagente para Agricultura Inteligente
Arquivo de inicialização para Google Colab

Desenvolvido para a Imersão Lura (Alura + Google Gemini)
"""

# @title Configuração do AgriSmart
# @markdown Execute esta célula para instalar as dependências necessárias e configurar o sistema

# Instalação das dependências
!pip install -q google-generativeai

# Importação das bibliotecas necessárias
import os
import google.generativeai as genai
from IPython.display import display, Markdown
import requests
from google.colab import files
import io
import zipfile

# Função para baixar e extrair o código do AgriSmart
def baixar_agrismart():
    """Baixa e extrai os arquivos do sistema AgriSmart."""
    print("Baixando arquivos do sistema AgriSmart...")
    
    # Aqui você colocaria a URL do seu repositório GitHub após fazer o upload
    # Por enquanto, vamos criar os arquivos localmente
    
    # Criando o arquivo agente_gerente.py
    with open('agente_gerente.py', 'w') as f:
        f.write("""
# Código do agente_gerente.py
# (Conteúdo completo seria colocado aqui)
""")
    
    # Criando os arquivos dos especialistas
    for especialista in ['especialista_culturas', 'meteorologista', 'especialista_pragas', 'especialista_irrigacao']:
        with open(f'{especialista}.py', 'w') as f:
            f.write(f"""
# Código do {especialista}.py
# (Conteúdo completo seria colocado aqui)
""")
    
    # Criando o arquivo principal
    with open('agrismart.py', 'w') as f:
        f.write("""
# Código do agrismart.py
# (Conteúdo completo seria colocado aqui)
""")
    
    print("Arquivos criados com sucesso!")
    print("Em um projeto real, estes arquivos seriam baixados de um repositório GitHub.")

# Função para inicializar o AgriSmart
def iniciar_agrismart(api_key):
    """
    Inicializa o sistema AgriSmart com todos os agentes.
    
    Args:
        api_key: Chave da API Gemini fornecida pelo usuário
        
    Returns:
        O agente gerente inicializado com todos os especialistas registrados
    """
    # Configuração da API Gemini
    genai.configure(api_key=api_key)
    modelo = genai.GenerativeModel('gemini-pro')
    
    # Simulação do sistema AgriSmart para demonstração
    class AgenteGerente:
        def __init__(self):
            self.especialistas = {}
            self.historico = []
            
        def registrar_especialista(self, nome, especialista):
            self.especialistas[nome] = especialista
            print(f"Especialista '{nome}' registrado com sucesso.")
            
        def processar_mensagem(self, mensagem):
            # Adiciona a mensagem ao histórico
            self.historico.append({"papel": "usuário", "conteúdo": mensagem})
            
            # Se for a primeira mensagem, apresenta-se
            if len(self.historico) == 1:
                saudacao = """
                Olá! Sou o Gerente do AgriSmart, seu sistema de consultoria agrícola inteligente.
                
                Estou aqui para conectá-lo com nossos especialistas em:
                • Culturas (milho, mandioca, café, banana)
                • Meteorologia e previsões climáticas
                • Gestão de pragas e doenças
                • Irrigação e recursos hídricos
                
                Como posso ajudá-lo hoje?
                """
                self.historico.append({"papel": "sistema", "conteúdo": saudacao})
                return saudacao
            
            # Simula o processamento da mensagem
            prompt = f"""
            Você é o gerente de um sistema de consultoria agrícola chamado AgriSmart.
            
            O sistema possui especialistas em:
            - Culturas (milho, mandioca, café, banana)
            - Meteorologia e previsões climáticas
            - Gestão de pragas e doenças
            - Irrigação e recursos hídricos
            
            O usuário enviou a seguinte mensagem: "{mensagem}"
            
            Responda como se você tivesse consultado os especialistas apropriados e estivesse fornecendo uma resposta integrada e completa.
            Mencione quais especialistas foram consultados no início da resposta.
            """
            
            resposta = modelo.generate_content(prompt)
            self.historico.append({"papel": "sistema", "conteúdo": resposta.text})
            return resposta.text
    
    # Inicializa o agente gerente
    gerente = AgenteGerente()
    
    # Simula o registro dos especialistas
    for especialista in ["Especialista em Culturas", "Meteorologista", 
                         "Especialista em Pragas e Doenças", "Especialista em Irrigação"]:
        gerente.registrar_especialista(especialista, None)
    
    print("\nSistema AgriSmart inicializado com sucesso!")
    print("Esta é uma versão de demonstração para o Google Colab.")
    print("Em um projeto completo, os agentes especialistas teriam implementações detalhadas.")
    
    return gerente

# Baixa os arquivos do AgriSmart
baixar_agrismart()

# @title Insira sua API Key do Google Gemini
# @markdown Obtenha sua chave em [Google AI Studio](https://aistudio.google.com/)
API_KEY = "" # @param {type:"string"}

if API_KEY:
    # Inicializa o sistema AgriSmart
    gerente = iniciar_agrismart(API_KEY)
    
    print("\n" + "="*50)
    print("AgriSmart está pronto para uso!")
    print("Use gerente.processar_mensagem('sua pergunta aqui') para interagir com o sistema.")
    print("="*50)
else:
    print("\nPor favor, insira sua API Key do Google Gemini para continuar.")

# @title Exemplos de Uso do AgriSmart
# @markdown Execute esta célula para ver exemplos de como interagir com o sistema

if 'gerente' in locals():
    # Exemplo 1: Apresentação
    print("Exemplo 1: Primeira interação com o sistema\n")
    resposta = gerente.processar_mensagem("Olá, preciso de ajuda com minha plantação.")
    display(Markdown(resposta))
    print("\n" + "-"*50 + "\n")
    
    # Exemplo 2: Pergunta sobre culturas
    print("Exemplo 2: Pergunta sobre culturas\n")
    resposta = gerente.processar_mensagem("Qual a melhor época para plantar mandioca?")
    display(Markdown(resposta))
    print("\n" + "-"*50 + "\n")
    
    # Exemplo 3: Pergunta sobre pragas
    print("Exemplo 3: Pergunta sobre pragas\n")
    resposta = gerente.processar_mensagem("Minhas plantas de café estão com manchas amarelas nas folhas. O que pode ser?")
    display(Markdown(resposta))
    print("\n" + "-"*50 + "\n")
    
    # Exemplo 4: Pergunta complexa que envolve múltiplos especialistas
    print("Exemplo 4: Pergunta complexa (múltiplos especialistas)\n")
    resposta = gerente.processar_mensagem("Estou planejando iniciar uma plantação de café. Preciso de orientações sobre variedades, clima ideal, pragas comuns e sistemas de irrigação.")
    display(Markdown(resposta))
else:
    print("Por favor, execute a célula de configuração primeiro e insira sua API Key.")
