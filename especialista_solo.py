"""
AgriSmart - Sistema Multiagente para Agricultura Inteligente
Agente Especialista em Análise de Solo - Especializado em interpretação de análises e características do solo

Desenvolvido para a Imersão Lura (Alura + Google Gemini)
"""

import google.generativeai as genai

class EspecialistaSolo:
    """
    Agente Especialista em Análise de Solo do sistema AgriSmart.
    Especializado em interpretação de análises laboratoriais e características do solo.
    """
    
    def __init__(self, modelo_gemini):
        """Inicializa o Especialista em Análise de Solo com o modelo Gemini."""
        self.modelo = modelo_gemini
        self.definir_personalidade()
        
    def definir_personalidade(self):
        """Define a personalidade e conhecimentos do Especialista em Análise de Solo."""
        self.personalidade = """
        Você é o Especialista em Análise de Solo do AgriSmart, um sistema multiagente de consultoria agrícola.
        
        Sua especialidade inclui conhecimento profundo sobre:
        - Interpretação de análises laboratoriais de solo
        - Avaliação de textura, estrutura e composição do solo
        - Diagnóstico de deficiências e toxicidades de nutrientes
        - Recomendações para correção de pH e salinidade
        - Avaliação da capacidade de retenção de água e drenagem
        
        Você também possui conhecimentos sobre:
        - Classificação de solos e suas características
        - Técnicas de amostragem de solo para análise
        - Indicadores biológicos de qualidade do solo
        - Manejo de solos problemáticos (ácidos, salinos, compactados)
        - Interpretação de mapas de solo e variabilidade espacial
        
        Ao responder, você deve:
        1. Interpretar dados de análise de solo quando fornecidos
        2. Explicar as implicações das características do solo para o cultivo
        3. Identificar problemas potenciais baseados nas propriedades do solo
        4. Sugerir práticas de manejo para melhorar a qualidade do solo
        5. Reconhecer quando um problema requer a consulta a outros especialistas
        
        Mantenha um tom profissional, objetivo e prestativo.
        """
    
    def responder(self, mensagem, historico):
        """
        Gera uma resposta especializada sobre análise e características do solo.
        
        Args:
            mensagem: A pergunta ou solicitação do usuário
            historico: O histórico da conversa para contexto
            
        Returns:
            Uma resposta especializada sobre análise e características do solo
        """
        # Constrói o prompt com a personalidade, histórico e mensagem atual
        prompt = f"""
        {self.personalidade}
        
        Histórico da conversa:
        {self._formatar_historico(historico)}
        
        Pergunta do usuário: "{mensagem}"
        
        Forneça uma resposta detalhada e especializada sobre análise e características do solo,
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
