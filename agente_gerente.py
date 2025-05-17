"""
AgriSmart - Sistema Multiagente para Agricultura Inteligente
Agente Gerente - Responsável por coordenar os agentes especialistas

Desenvolvido para a Imersão Lura (Alura + Google Gemini)
"""

import os
import google.generativeai as genai
from IPython.display import display, Markdown

# Configuração da API Gemini (a chave será fornecida pelo usuário)
def configurar_gemini(api_key):
    """Configura a API Gemini com a chave fornecida."""
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-pro')

class AgenteGerente:
    """
    Agente Gerente do sistema AgriSmart.
    Responsável por receber as solicitações do usuário, analisar a intenção
    e direcionar para o especialista mais adequado.
    """
    
    def __init__(self, api_key):
        """Inicializa o Agente Gerente com a chave da API Gemini."""
        self.modelo = configurar_gemini(api_key)
        self.especialistas = {}
        self.historico = []
        self.definir_personalidade()
        
    def definir_personalidade(self):
        """Define a personalidade e comportamento do Agente Gerente."""
        self.personalidade = """
        Você é o Gerente do AgriSmart, um sistema multiagente de consultoria agrícola.
        
        Seu papel é:
        1. Receber as solicitações dos usuários
        2. Analisar a intenção e o contexto da solicitação
        3. Identificar qual especialista ou combinação de especialistas é mais adequado para responder
        4. Coordenar a comunicação entre os especialistas quando necessário
        5. Apresentar as respostas de forma clara e profissional
        
        Você tem acesso a quatro especialistas:
        - Especialista em Culturas: conhecimento sobre culturas como milho, mandioca, café e banana
        - Meteorologista: análise e previsão de condições climáticas para agricultura
        - Especialista em Pragas e Doenças: identificação e gestão de pragas e doenças agrícolas
        - Especialista em Irrigação: otimização de recursos hídricos e sistemas de irrigação
        
        Mantenha um tom profissional, cordial e prestativo. Sempre apresente-se como Gerente do AgriSmart
        no início da conversa e explique brevemente como pode ajudar.
        """
    
    def registrar_especialista(self, nome, especialista):
        """Registra um agente especialista no sistema."""
        self.especialistas[nome] = especialista
        print(f"Especialista '{nome}' registrado com sucesso.")
    
    def analisar_intencao(self, mensagem):
        """
        Analisa a intenção do usuário para determinar qual especialista deve responder.
        Retorna o nome do especialista mais adequado ou uma lista de especialistas.
        """
        prompt = f"""
        {self.personalidade}
        
        Analise a seguinte solicitação de um usuário e determine qual especialista ou especialistas 
        devem responder. Retorne apenas o nome do especialista ou uma lista de nomes separados por vírgula.
        
        Especialistas disponíveis:
        - Especialista em Culturas
        - Meteorologista
        - Especialista em Pragas e Doenças
        - Especialista em Irrigação
        
        Solicitação do usuário: "{mensagem}"
        
        Especialista(s) mais adequado(s):
        """
        
        resposta = self.modelo.generate_content(prompt)
        especialistas_indicados = resposta.text.strip()
        
        # Processa a resposta para extrair os nomes dos especialistas
        if ',' in especialistas_indicados:
            return [esp.strip() for esp in especialistas_indicados.split(',')]
        else:
            return [especialistas_indicados]
    
    def processar_mensagem(self, mensagem):
        """
        Processa a mensagem do usuário, identifica os especialistas adequados
        e coordena a resposta.
        """
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
        
        # Analisa a intenção e identifica os especialistas adequados
        especialistas_indicados = self.analisar_intencao(mensagem)
        
        # Verifica se os especialistas existem no sistema
        especialistas_disponiveis = [esp for esp in especialistas_indicados if esp in self.especialistas]
        
        if not especialistas_disponiveis:
            resposta = """
            Peço desculpas, mas não consegui identificar claramente qual especialista poderia melhor
            responder à sua solicitação. Poderia fornecer mais detalhes sobre sua questão agrícola?
            """
            self.historico.append({"papel": "sistema", "conteúdo": resposta})
            return resposta
        
        # Caso seja apenas um especialista
        if len(especialistas_disponiveis) == 1:
            especialista = self.especialistas[especialistas_disponiveis[0]]
            resposta = especialista.responder(mensagem, self.historico)
            self.historico.append({"papel": "especialista", "nome": especialistas_disponiveis[0], "conteúdo": resposta})
            return f"[Consultando {especialistas_disponiveis[0]}]\n\n{resposta}"
        
        # Caso sejam múltiplos especialistas
        respostas = []
        for nome_esp in especialistas_disponiveis:
            especialista = self.especialistas[nome_esp]
            resp = especialista.responder(mensagem, self.historico)
            respostas.append(f"[{nome_esp}]:\n{resp}")
            self.historico.append({"papel": "especialista", "nome": nome_esp, "conteúdo": resp})
        
        # Integra as respostas dos especialistas
        resposta_integrada = self.integrar_respostas(mensagem, especialistas_disponiveis, respostas)
        self.historico.append({"papel": "sistema", "conteúdo": resposta_integrada})
        
        return resposta_integrada
    
    def integrar_respostas(self, mensagem, especialistas, respostas):
        """
        Integra as respostas de múltiplos especialistas em uma resposta coerente.
        """
        prompt = f"""
        {self.personalidade}
        
        Você recebeu respostas de múltiplos especialistas para a seguinte solicitação do usuário:
        "{mensagem}"
        
        Respostas dos especialistas:
        {"".join(respostas)}
        
        Integre essas respostas em uma única resposta coerente e abrangente.
        Mantenha as informações técnicas importantes de cada especialista, mas evite repetições.
        Organize a resposta de forma lógica e fluida, como se fosse uma única análise completa.
        """
        
        resposta = self.modelo.generate_content(prompt)
        return f"Com base na análise de nossos especialistas ({', '.join(especialistas)}), posso informar que:\n\n{resposta.text}"
    
    def exibir_resposta(self, resposta):
        """Exibe a resposta formatada no notebook."""
        display(Markdown(resposta))
