"""
AgriSmart - Sistema Multiagente para Agricultura Inteligente
Agente Especialista em Irrigação - Especializado em otimização de recursos hídricos e sistemas de irrigação

Desenvolvido para a Imersão Lura (Alura + Google Gemini)
"""

import google.generativeai as genai

class EspecialistaIrrigacao:
    """
    Agente Especialista em Irrigação do sistema AgriSmart.
    Especializado em otimização de recursos hídricos e sistemas de irrigação.
    """
    
    def __init__(self, modelo_gemini):
        """Inicializa o Especialista em Irrigação com o modelo Gemini."""
        self.modelo = modelo_gemini
        self.definir_personalidade()
        
    def definir_personalidade(self):
        """Define a personalidade e conhecimentos do Especialista em Irrigação."""
        self.personalidade = """
        Você é o Especialista em Irrigação do AgriSmart, um sistema multiagente de consultoria agrícola.
        
        Sua especialidade inclui conhecimento profundo sobre:
        - Sistemas de irrigação (gotejamento, microaspersão, aspersão, superfície)
        - Gestão eficiente de recursos hídricos na agricultura
        - Cálculo de necessidades hídricas de diferentes culturas
        - Tecnologias de monitoramento de umidade do solo
        - Estratégias de irrigação em condições de escassez hídrica
        
        Você também possui conhecimentos sobre:
        - Qualidade da água para irrigação e tratamentos necessários
        - Captação e armazenamento de água para uso agrícola
        - Automação de sistemas de irrigação
        - Fertirrigação (aplicação de fertilizantes via irrigação)
        - Legislação e outorgas relacionadas ao uso da água na agricultura
        
        Ao responder, você deve:
        1. Recomendar sistemas e estratégias de irrigação adequados ao contexto específico
        2. Priorizar o uso eficiente da água e a sustentabilidade dos recursos hídricos
        3. Considerar fatores como tipo de solo, clima, cultura e disponibilidade de água
        4. Explicar os benefícios e limitações de diferentes abordagens
        5. Reconhecer quando um problema requer a consulta a outros especialistas
        
        Mantenha um tom profissional, objetivo e prestativo.
        """
    
    def responder(self, mensagem, historico):
        """
        Gera uma resposta especializada sobre irrigação e recursos hídricos.
        
        Args:
            mensagem: A pergunta ou solicitação do usuário
            historico: O histórico da conversa para contexto
            
        Returns:
            Uma resposta especializada sobre irrigação e gestão de recursos hídricos
        """
        # Constrói o prompt com a personalidade, histórico e mensagem atual
        prompt = f"""
        {self.personalidade}
        
        Histórico da conversa:
        {self._formatar_historico(historico)}
        
        Pergunta do usuário: "{mensagem}"
        
        Forneça uma resposta detalhada e especializada sobre irrigação e gestão de recursos hídricos,
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
