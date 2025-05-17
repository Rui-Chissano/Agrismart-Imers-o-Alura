"""
AgriSmart - Sistema Multiagente para Agricultura Inteligente
Agente Especialista em Fertilização e Nutrição de Plantas - Especializado em recomendações de adubação e nutrição vegetal

Desenvolvido para a Imersão Lura (Alura + Google Gemini)
"""

import google.generativeai as genai

class EspecialistaFertilizacao:
    """
    Agente Especialista em Fertilização e Nutrição de Plantas do sistema AgriSmart.
    Especializado em recomendações de adubação e nutrição vegetal baseadas em análises de solo.
    """
    
    def __init__(self, modelo_gemini):
        """Inicializa o Especialista em Fertilização e Nutrição de Plantas com o modelo Gemini."""
        self.modelo = modelo_gemini
        self.definir_personalidade()
        
    def definir_personalidade(self):
        """Define a personalidade e conhecimentos do Especialista em Fertilização e Nutrição de Plantas."""
        self.personalidade = """
        Você é o Especialista em Fertilização e Nutrição de Plantas do AgriSmart, um sistema multiagente de consultoria agrícola.
        
        Sua especialidade inclui conhecimento profundo sobre:
        - Recomendações precisas de fertilizantes baseadas na análise de solo
        - Planos de adubação específicos para diferentes culturas
        - Estratégias de nutrição foliar complementar
        - Manejo de matéria orgânica e compostagem
        - Técnicas de fertilização sustentável e de precisão
        
        Você também possui conhecimentos sobre:
        - Sintomas de deficiências e toxicidades nutricionais em plantas
        - Interações entre nutrientes no solo e na planta
        - Fertilizantes orgânicos e convencionais
        - Biofertilizantes e inoculantes microbianos
        - Fertirrigação e aplicação localizada de nutrientes
        
        Ao responder, você deve:
        1. Fornecer recomendações específicas de adubação quando solicitado
        2. Considerar as necessidades nutricionais da cultura em questão
        3. Levar em conta as características do solo (quando informadas)
        4. Explicar os benefícios esperados das recomendações
        5. Reconhecer quando um problema requer a consulta a outros especialistas
        
        Mantenha um tom profissional, objetivo e prestativo.
        """
    
    def responder(self, mensagem, historico):
        """
        Gera uma resposta especializada sobre fertilização e nutrição de plantas.
        
        Args:
            mensagem: A pergunta ou solicitação do usuário
            historico: O histórico da conversa para contexto
            
        Returns:
            Uma resposta especializada sobre fertilização e nutrição de plantas
        """
        # Constrói o prompt com a personalidade, histórico e mensagem atual
        prompt = f"""
        {self.personalidade}
        
        Histórico da conversa:
        {self._formatar_historico(historico)}
        
        Pergunta do usuário: "{mensagem}"
        
        Forneça uma resposta detalhada e especializada sobre fertilização e nutrição de plantas,
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
