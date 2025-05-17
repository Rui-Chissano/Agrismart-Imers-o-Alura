"""
AgriSmart - Sistema Multiagente para Agricultura Inteligente
Agente Especialista em Design e Visualização - Especializado em criação de visualizações e representações gráficas para agricultura

Desenvolvido para a Imersão Lura (Alura + Google Gemini)
"""

import google.generativeai as genai

class EspecialistaVisualizacao:
    """
    Agente Especialista em Design e Visualização do sistema AgriSmart.
    Especializado em criar visualizações, mapas e representações gráficas para agricultura.
    """
    
    def __init__(self, modelo_gemini):
        """Inicializa o Especialista em Design e Visualização com o modelo Gemini."""
        self.modelo = modelo_gemini
        self.definir_personalidade()
        
    def definir_personalidade(self):
        """Define a personalidade e conhecimentos do Especialista em Design e Visualização."""
        self.personalidade = """
        Você é o Especialista em Design e Visualização do AgriSmart, um sistema multiagente de consultoria agrícola.
        
        Sua especialidade inclui conhecimento profundo sobre:
        - Criação de visualizações de plantações baseadas em dados fornecidos
        - Geração de mapas de distribuição de culturas
        - Visualização de sistemas de irrigação
        - Representações gráficas de dados agrícolas
        - Simulações visuais de crescimento de culturas
        
        Você também possui conhecimentos sobre:
        - Princípios de design e comunicação visual
        - Interpretação de dados espaciais agrícolas
        - Ferramentas de visualização e design para agricultura
        - Mapeamento de propriedades rurais
        - Representação visual de dados meteorológicos e ambientais
        
        Ao responder, você deve:
        1. Descrever detalhadamente como seria a visualização ideal para o cenário solicitado
        2. Explicar os elementos visuais que comporiam a representação
        3. Sugerir cores, layouts e formatos apropriados para o contexto agrícola
        4. Considerar a finalidade da visualização (planejamento, monitoramento, apresentação)
        5. Indicar quais dados seriam necessários para criar a visualização completa
        
        Quando solicitado a criar uma imagem, descreva detalhadamente como seria essa imagem,
        incluindo todos os elementos visuais, cores, perspectivas e detalhes que a comporiam.
        
        Mantenha um tom profissional, criativo e prestativo.
        """
    
    def responder(self, mensagem, historico):
        """
        Gera uma resposta especializada sobre design e visualização para agricultura.
        
        Args:
            mensagem: A pergunta ou solicitação do usuário
            historico: O histórico da conversa para contexto
            
        Returns:
            Uma resposta especializada sobre visualizações e representações gráficas para agricultura
        """
        # Constrói o prompt com a personalidade, histórico e mensagem atual
        prompt = f"""
        {self.personalidade}
        
        Histórico da conversa:
        {self._formatar_historico(historico)}
        
        Pergunta do usuário: "{mensagem}"
        
        Forneça uma resposta detalhada e especializada sobre design e visualização para agricultura,
        considerando o contexto da conversa. Se a pergunta não estiver relacionada às suas
        especialidades, indique quais outros especialistas poderiam ajudar melhor.
        
        Se for solicitada a criação de uma visualização ou representação gráfica, descreva detalhadamente
        como seria essa visualização, incluindo todos os elementos visuais, cores, perspectivas e detalhes
        que a comporiam. Explique também quais dados seriam necessários para criar a visualização completa.
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
