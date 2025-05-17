"""
AgriSmart - Sistema Multiagente para Agricultura Inteligente
Agente Especialista em Pragas e Doenças - Especializado em identificação e gestão de pragas e doenças agrícolas

Desenvolvido para a Imersão Lura (Alura + Google Gemini)
"""

import google.generativeai as genai

class EspecialistaPragas:
    """
    Agente Especialista em Pragas e Doenças do sistema AgriSmart.
    Especializado em identificação e gestão de pragas e doenças agrícolas.
    """
    
    def __init__(self, modelo_gemini):
        """Inicializa o Especialista em Pragas e Doenças com o modelo Gemini."""
        self.modelo = modelo_gemini
        self.definir_personalidade()
        
    def definir_personalidade(self):
        """Define a personalidade e conhecimentos do Especialista em Pragas e Doenças."""
        self.personalidade = """
        Você é o Especialista em Pragas e Doenças do AgriSmart, um sistema multiagente de consultoria agrícola.
        
        Sua especialidade inclui conhecimento profundo sobre:
        - Identificação de pragas comuns em culturas tropicais e subtropicais
        - Diagnóstico de doenças fúngicas, bacterianas e virais em plantas
        - Estratégias de manejo integrado de pragas (MIP)
        - Métodos de controle biológico, cultural e químico
        - Resistência de pragas e patógenos a defensivos agrícolas
        
        Você também possui conhecimentos sobre:
        - Ciclos de vida de insetos-praga e patógenos
        - Monitoramento e amostragem de pragas no campo
        - Uso seguro e eficiente de defensivos agrícolas
        - Práticas preventivas para redução de infestações
        - Legislação e certificações relacionadas ao controle de pragas
        
        Ao responder, você deve:
        1. Ajudar na identificação precisa de pragas e doenças com base nos sintomas descritos
        2. Recomendar estratégias de manejo integrado, priorizando métodos menos agressivos
        3. Explicar os riscos associados a diferentes métodos de controle
        4. Considerar o contexto específico (cultura, clima, escala de produção)
        5. Reconhecer quando um problema requer a consulta a outros especialistas
        
        Mantenha um tom profissional, objetivo e prestativo.
        """
    
    def responder(self, mensagem, historico):
        """
        Gera uma resposta especializada sobre pragas e doenças agrícolas.
        
        Args:
            mensagem: A pergunta ou solicitação do usuário
            historico: O histórico da conversa para contexto
            
        Returns:
            Uma resposta especializada sobre identificação e gestão de pragas e doenças
        """
        # Constrói o prompt com a personalidade, histórico e mensagem atual
        prompt = f"""
        {self.personalidade}
        
        Histórico da conversa:
        {self._formatar_historico(historico)}
        
        Pergunta do usuário: "{mensagem}"
        
        Forneça uma resposta detalhada e especializada sobre identificação e gestão de pragas e doenças agrícolas,
        considerando o contexto da conversa. Se a pergunta não estiver relacionada às suas
        especialidades, indique quais outros especialistas poderiam ajudar melhor.
        """
        
        # Gera a resposta usando o modelo Gemini
        resposta = self.modelo.generate_content(prompt)
        return resposta.text
    
    def _formatar_historico(self, historico):
        """Formata o histórico da conversa para incluir no prompt."""
        historico_formatado = ""
        for item in historico:
            if item["papel"] == "usuário":
                historico_formatado += f"Usuário: {item['conteúdo']}\n"
            elif item["papel"] == "sistema":
                historico_formatado += f"Sistema: {item['conteúdo']}\n"
            elif item["papel"] == "especialista":
                historico_formatado += f"{item['nome']}: {item['conteúdo']}\n"
        return historico_formatado
