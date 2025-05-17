"""
AgriSmart - Sistema Multiagente para Agricultura Inteligente
Agente Especialista Financeiro - Especializado em análise financeira e econômica para agricultura

Desenvolvido para a Imersão Lura (Alura + Google Gemini)
"""

import google.generativeai as genai

class EspecialistaFinanceiro:
    """
    Agente Especialista Financeiro do sistema AgriSmart.
    Especializado em análise financeira, custos, rendimentos e projeções econômicas para agricultura.
    """
    
    def __init__(self, modelo_gemini):
        """Inicializa o Especialista Financeiro com o modelo Gemini."""
        self.modelo = modelo_gemini
        self.definir_personalidade()
        
    def definir_personalidade(self):
        """Define a personalidade e conhecimentos do Especialista Financeiro."""
        self.personalidade = """
        Você é o Especialista Financeiro do AgriSmart, um sistema multiagente de consultoria agrícola.
        
        Sua especialidade inclui conhecimento profundo sobre:
        - Análise de custos e rendimentos de produção agrícola
        - Projeções financeiras para diferentes culturas
        - Análise de viabilidade econômica de projetos agrícolas
        - Gestão financeira de propriedades rurais
        - Financiamentos e linhas de crédito para agricultura
        
        Você também possui conhecimentos sobre:
        - Precificação de produtos agrícolas
        - Análise de mercado e tendências de preços
        - Estratégias de comercialização
        - Gestão de riscos financeiros na agricultura
        - Tributação e aspectos legais financeiros do agronegócio
        
        Ao responder, você deve:
        1. Fornecer análises financeiras precisas e realistas
        2. Apresentar projeções de custos e rendimentos quando solicitado
        3. Considerar fatores específicos como escala de produção, região e tipo de cultura
        4. Explicar conceitos financeiros de forma acessível
        5. Sugerir estratégias para otimização de resultados financeiros
        
        Quando solicitado, você deve fornecer dados em formato tabular ou sugerir a criação de gráficos
        para visualização de informações financeiras.
        
        Mantenha um tom profissional, objetivo e prestativo.
        """
    
    def responder(self, mensagem, historico):
        """
        Gera uma resposta especializada sobre finanças e economia agrícola.
        
        Args:
            mensagem: A pergunta ou solicitação do usuário
            historico: O histórico da conversa para contexto
            
        Returns:
            Uma resposta especializada sobre análise financeira e econômica para agricultura
        """
        # Constrói o prompt com a personalidade, histórico e mensagem atual
        prompt = f"""
        {self.personalidade}
        
        Histórico da conversa:
        {self._formatar_historico(historico)}
        
        Pergunta do usuário: "{mensagem}"
        
        Forneça uma resposta detalhada e especializada sobre análise financeira e econômica para agricultura,
        considerando o contexto da conversa. Se a pergunta não estiver relacionada às suas
        especialidades, indique quais outros especialistas poderiam ajudar melhor.
        
        Se for solicitada uma análise de custos, rendimentos ou projeções financeiras, apresente os dados
        em formato tabular quando apropriado. Se for solicitada a criação de gráficos, descreva como seria
        o gráfico ideal para representar os dados solicitados.
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
