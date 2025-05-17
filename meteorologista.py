"""
AgriSmart - Sistema Multiagente para Agricultura Inteligente
Agente Meteorologista - Especializado em análise e previsão climática para agricultura

Desenvolvido para a Imersão Lura (Alura + Google Gemini)
"""

import google.generativeai as genai

class Meteorologista:
    """
    Agente Meteorologista do sistema AgriSmart.
    Especializado em análise e previsão de condições climáticas para agricultura.
    """
    
    def __init__(self, modelo_gemini):
        """Inicializa o Meteorologista com o modelo Gemini."""
        self.modelo = modelo_gemini
        self.definir_personalidade()
        
    def definir_personalidade(self):
        """Define a personalidade e conhecimentos do Meteorologista."""
        self.personalidade = """
        Você é o Meteorologista do AgriSmart, um sistema multiagente de consultoria agrícola.
        
        Sua especialidade inclui conhecimento profundo sobre:
        - Interpretação de dados meteorológicos para aplicações agrícolas
        - Previsão de condições climáticas de curto e médio prazo
        - Análise de padrões sazonais e sua influência nas culturas
        - Identificação de riscos climáticos (secas, geadas, chuvas intensas)
        - Estratégias de adaptação às mudanças climáticas na agricultura
        
        Você também possui conhecimentos sobre:
        - Microclimas e sua influência na produção agrícola
        - Sistemas de monitoramento meteorológico
        - Relação entre clima e desenvolvimento de culturas
        - Calendários agroclimáticos para diferentes regiões
        - Interpretação de imagens de satélite e radar para agricultura
        
        Ao responder, você deve:
        1. Fornecer análises meteorológicas precisas e relevantes para o contexto agrícola
        2. Explicar como as condições climáticas afetam as culturas específicas
        3. Oferecer recomendações práticas para mitigar riscos climáticos
        4. Usar linguagem acessível, mas tecnicamente precisa
        5. Reconhecer quando um problema requer a consulta a outros especialistas
        
        Mantenha um tom profissional, objetivo e prestativo.
        """
    
    def responder(self, mensagem, historico):
        """
        Gera uma resposta especializada sobre meteorologia agrícola.
        
        Args:
            mensagem: A pergunta ou solicitação do usuário
            historico: O histórico da conversa para contexto
            
        Returns:
            Uma resposta especializada sobre meteorologia e clima para agricultura
        """
        # Constrói o prompt com a personalidade, histórico e mensagem atual
        prompt = f"""
        {self.personalidade}
        
        Histórico da conversa:
        {self._formatar_historico(historico)}
        
        Pergunta do usuário: "{mensagem}"
        
        Forneça uma resposta detalhada e especializada sobre meteorologia e clima para agricultura,
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
