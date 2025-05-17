"""
AgriSmart - Sistema Multiagente para Agricultura Inteligente
Agente Especialista em Culturas - Especializado em culturas como milho, mandioca, café e banana

Desenvolvido para a Imersão Lura (Alura + Google Gemini)
"""

import google.generativeai as genai

class EspecialistaCulturas:
    """
    Agente Especialista em Culturas do sistema AgriSmart.
    Possui conhecimento especializado sobre culturas como milho, mandioca, café e banana.
    """
    
    def __init__(self, modelo_gemini):
        """Inicializa o Especialista em Culturas com o modelo Gemini."""
        self.modelo = modelo_gemini
        self.definir_personalidade()
        
    def definir_personalidade(self):
        """Define a personalidade e conhecimentos do Especialista em Culturas."""
        self.personalidade = """
        Você é o Especialista em Culturas do AgriSmart, um sistema multiagente de consultoria agrícola.
        
        Sua especialidade inclui conhecimento profundo sobre:
        - Cultivo de milho: variedades, ciclo de crescimento, necessidades nutricionais, técnicas de plantio
        - Cultivo de mandioca: variedades, métodos de propagação, processamento, resistência a secas
        - Cultivo de café: variedades (arábica, robusta), sistemas de produção, processamento pós-colheita
        - Cultivo de banana: variedades, manejo do bananal, controle de maturação, colheita
        
        Você também possui conhecimentos sobre:
        - Rotação de culturas e consórcios
        - Calendários agrícolas para diferentes regiões
        - Seleção de variedades adaptadas a diferentes climas
        - Técnicas de plantio e colheita
        - Armazenamento e processamento básico de produtos agrícolas
        
        Ao responder, você deve:
        1. Fornecer informações precisas e atualizadas sobre as culturas
        2. Adaptar suas recomendações ao contexto específico (clima, solo, escala de produção)
        3. Considerar práticas sustentáveis e economicamente viáveis
        4. Usar linguagem acessível, mas precisa tecnicamente
        5. Reconhecer quando um problema pode se beneficiar da consulta a outros especialistas
        
        Mantenha um tom profissional, objetivo e prestativo.
        """
    
    def responder(self, mensagem, historico):
        """
        Gera uma resposta especializada sobre culturas agrícolas.
        
        Args:
            mensagem: A pergunta ou solicitação do usuário
            historico: O histórico da conversa para contexto
            
        Returns:
            Uma resposta especializada sobre culturas agrícolas
        """
        # Constrói o prompt com a personalidade, histórico e mensagem atual
        prompt = f"""
        {self.personalidade}
        
        Histórico da conversa:
        {self._formatar_historico(historico)}
        
        Pergunta do usuário: "{mensagem}"
        
        Forneça uma resposta detalhada e especializada sobre as culturas agrícolas mencionadas,
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
