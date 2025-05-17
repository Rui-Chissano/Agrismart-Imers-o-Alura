"""
AgriSmart - Sistema Multiagente para Agricultura Inteligente
Arquivo principal atualizado para integração e execução do sistema com todos os especialistas

Desenvolvido para a Imersão Lura (Alura + Google Gemini)
"""

import os
import google.generativeai as genai
from IPython.display import display, Markdown

# Importação dos módulos dos agentes
from agente_gerente import AgenteGerente
from especialista_culturas import EspecialistaCulturas
from meteorologista import Meteorologista
from especialista_pragas import EspecialistaPragas
from especialista_irrigacao import EspecialistaIrrigacao
from especialista_financeiro import EspecialistaFinanceiro
from especialista_visualizacao import EspecialistaVisualizacao
from especialista_solo import EspecialistaSolo
from especialista_fertilizacao import EspecialistaFertilizacao
from especialista_sustentabilidade import EspecialistaSustentabilidade

def iniciar_agrismart(api_key):
    """
    Inicializa o sistema AgriSmart com todos os agentes.
    
    Args:
        api_key: Chave da API Gemini fornecida pelo usuário
        
    Returns:
        O agente gerente inicializado com todos os especialistas registrados
    """
    # Inicializa o agente gerente
    gerente = AgenteGerente(api_key)
    
    # Configura o modelo Gemini para os especialistas
    modelo = genai.GenerativeModel('gemini-pro')
    
    # Inicializa e registra os especialistas
    especialista_culturas = EspecialistaCulturas(modelo)
    meteorologista = Meteorologista(modelo)
    especialista_pragas = EspecialistaPragas(modelo)
    especialista_irrigacao = EspecialistaIrrigacao(modelo)
    especialista_financeiro = EspecialistaFinanceiro(modelo)
    especialista_visualizacao = EspecialistaVisualizacao(modelo)
    especialista_solo = EspecialistaSolo(modelo)
    especialista_fertilizacao = EspecialistaFertilizacao(modelo)
    especialista_sustentabilidade = EspecialistaSustentabilidade(modelo)
    
    # Registra os especialistas no gerente
    gerente.registrar_especialista("Especialista em Culturas", especialista_culturas)
    gerente.registrar_especialista("Meteorologista", meteorologista)
    gerente.registrar_especialista("Especialista em Pragas e Doenças", especialista_pragas)
    gerente.registrar_especialista("Especialista em Irrigação", especialista_irrigacao)
    gerente.registrar_especialista("Especialista Financeiro", especialista_financeiro)
    gerente.registrar_especialista("Especialista em Design e Visualização", especialista_visualizacao)
    gerente.registrar_especialista("Especialista em Análise de Solo", especialista_solo)
    gerente.registrar_especialista("Especialista em Fertilização", especialista_fertilizacao)
    gerente.registrar_especialista("Especialista em Sustentabilidade", especialista_sustentabilidade)
    
    print("Sistema AgriSmart inicializado com sucesso!")
    print("Agentes registrados:")
    print("- Agente Gerente")
    print("- Especialista em Culturas")
    print("- Meteorologista")
    print("- Especialista em Pragas e Doenças")
    print("- Especialista em Irrigação")
    print("- Especialista Financeiro")
    print("- Especialista em Design e Visualização")
    print("- Especialista em Análise de Solo")
    print("- Especialista em Fertilização")
    print("- Especialista em Sustentabilidade")
    
    return gerente

# Exemplo de uso no Google Colab
def exemplo_uso():
    """
    Exemplo de como utilizar o sistema AgriSmart no Google Colab.
    """
    markdown_exemplo = """
    # AgriSmart - Sistema Multiagente para Agricultura Inteligente
    
    ## Configuração Inicial
    
    Primeiro, você precisa obter uma API Key do Google Gemini:
    1. Acesse [Google AI Studio](https://aistudio.google.com/)
    2. Crie ou faça login na sua conta Google
    3. Vá para a seção "API Keys"
    4. Crie uma nova API Key
    
    ```python
    # Importe as bibliotecas necessárias
    import os
    import google.generativeai as genai
    from IPython.display import display, Markdown
    
    # Importe o sistema AgriSmart
    from agrismart import iniciar_agrismart
    
    # Configure sua API Key (substitua pelo seu valor)
    API_KEY = "SUA_API_KEY_AQUI"  # Nunca compartilhe sua API Key publicamente!
    
    # Inicialize o sistema AgriSmart
    gerente = iniciar_agrismart(API_KEY)
    ```
    
    ## Interagindo com o Sistema
    
    Agora você pode interagir com o sistema AgriSmart:
    
    ```python
    # Primeira interação - o sistema se apresentará
    resposta = gerente.processar_mensagem("Olá, preciso de ajuda com minha plantação de milho.")
    display(Markdown(resposta))
    
    # Pergunte sobre culturas específicas
    resposta = gerente.processar_mensagem("Qual a melhor época para plantar mandioca?")
    display(Markdown(resposta))
    
    # Pergunte sobre problemas com pragas
    resposta = gerente.processar_mensagem("Minhas plantas de café estão com manchas amarelas nas folhas. O que pode ser?")
    display(Markdown(resposta))
    
    # Pergunte sobre irrigação
    resposta = gerente.processar_mensagem("Qual o melhor sistema de irrigação para banana em região com escassez de água?")
    display(Markdown(resposta))
    
    # Pergunte sobre clima
    resposta = gerente.processar_mensagem("Como a previsão de seca prolongada pode afetar minha plantação de café?")
    display(Markdown(resposta))
    
    # Pergunte sobre análise financeira
    resposta = gerente.processar_mensagem("Qual o custo estimado e retorno esperado para 1 hectare de café arábica?")
    display(Markdown(resposta))
    
    # Pergunte sobre visualização
    resposta = gerente.processar_mensagem("Gostaria de visualizar como ficaria uma área de 5 hectares com plantação de café e sistema de irrigação por gotejamento.")
    display(Markdown(resposta))
    
    # Pergunte sobre análise de solo
    resposta = gerente.processar_mensagem("Meu solo tem pH 5.2 e textura argilosa. O que isso significa para o cultivo de milho?")
    display(Markdown(resposta))
    
    # Pergunte sobre fertilização
    resposta = gerente.processar_mensagem("Quais fertilizantes devo usar para uma plantação de café com deficiência de nitrogênio?")
    display(Markdown(resposta))
    
    # Pergunte sobre sustentabilidade
    resposta = gerente.processar_mensagem("Quais certificações orgânicas são mais valorizadas para exportação de café?")
    display(Markdown(resposta))
    
    # Faça uma pergunta que envolve múltiplos especialistas
    resposta = gerente.processar_mensagem("Estou planejando iniciar uma plantação de café em 10 hectares. Preciso de orientações completas sobre variedades, clima, solo, pragas, irrigação, fertilização, custos, certificações e como visualizar o layout.")
    display(Markdown(resposta))
    ```
    
    ## Personalização
    
    Você pode personalizar os agentes especialistas modificando seus arquivos de definição:
    - `especialista_culturas.py`
    - `meteorologista.py`
    - `especialista_pragas.py`
    - `especialista_irrigacao.py`
    - `especialista_financeiro.py`
    - `especialista_visualizacao.py`
    - `especialista_solo.py`
    - `especialista_fertilizacao.py`
    - `especialista_sustentabilidade.py`
    
    Para adicionar novos especialistas, crie um novo arquivo seguindo o mesmo padrão e registre-o no `agente_gerente`.
    """
    
    return markdown_exemplo
