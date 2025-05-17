"""
AgriSmart - Sistema Multiagente para Agricultura Inteligente
Agente Especialista em Sustentabilidade e Certificação Agrícola - Especializado em práticas sustentáveis e certificações

Desenvolvido para a Imersão Lura (Alura + Google Gemini)
"""

import google.generativeai as genai

class EspecialistaSustentabilidade:
    """
    Agente Especialista em Sustentabilidade e Certificação Agrícola do sistema AgriSmart.
    Especializado em práticas agrícolas sustentáveis e processos de certificação.
    """
    
    def __init__(self, modelo_gemini):
        """Inicializa o Especialista em Sustentabilidade e Certificação Agrícola com o modelo Gemini."""
        self.modelo = modelo_gemini
        self.definir_personalidade()
        
    def definir_personalidade(self):
        """Define a personalidade e conhecimentos do Especialista em Sustentabilidade e Certificação Agrícola."""
        self.personalidade = """
        Você é o Especialista em Sustentabilidade e Certificação Agrícola do AgriSmart, um sistema multiagente de consultoria agrícola.
        
        Sua especialidade inclui conhecimento profundo sobre:
        - Práticas agrícolas sustentáveis e regenerativas
        - Certificações orgânicas e sustentáveis (GlobalG.A.P., Rainforest Alliance, etc.)
        - Requisitos para exportação de produtos agrícolas
        - Redução da pegada de carbono na agricultura
        - Preservação da biodiversidade em áreas agrícolas
        
        Você também possui conhecimentos sobre:
        - Processos de auditoria e documentação para certificações
        - Mercados premium para produtos certificados
        - Legislação ambiental aplicada à agricultura
        - Manejo integrado de recursos naturais
        - Tendências em consumo consciente e sustentável
        
        Ao responder, você deve:
        1. Recomendar práticas sustentáveis adequadas ao contexto específico
        2. Explicar os processos e requisitos para obtenção de certificações
        3. Orientar sobre estratégias para acesso a mercados de produtos certificados
        4. Sugerir abordagens para agregar valor através da sustentabilidade
        5. Reconhecer quando um problema requer a consulta a outros especialistas
        
        Mantenha um tom profissional, objetivo e prestativo.
        """
    
    def responder(self, mensagem, historico):
        """
        Gera uma resposta especializada sobre sustentabilidade e certificação agrícola.
        
        Args:
            mensagem: A pergunta ou solicitação do usuário
            historico: O histórico da conversa para contexto
            
        Returns:
            Uma resposta especializada sobre sustentabilidade e certificação agrícola
        """
        # Constrói o prompt com a personalidade, histórico e mensagem atual
        prompt = f"""
        {self.personalidade}
        
        Histórico da conversa:
        {self._formatar_historico(historico)}
        
        Pergunta do usuário: "{mensagem}"
        
        Forneça uma resposta detalhada e especializada sobre sustentabilidade e certificação agrícola,
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
