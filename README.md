# AgriSmart - Sistema Multiagente para Agricultura Inteligente

## Visão Geral

AgriSmart é um sistema multiagente desenvolvido para a Imersão Lura (Alura + Google Gemini), que utiliza inteligência artificial para fornecer consultoria agrícola especializada. O sistema é composto por um Agente Gerente central que coordena nove Agentes Especialistas, cada um com conhecimentos específicos em diferentes áreas da agricultura.

## Arquitetura do Sistema

O sistema AgriSmart utiliza a API Gemini para criar um ecossistema de agentes inteligentes que trabalham em conjunto:

1. **Agente Gerente**: Recebe as solicitações do usuário, analisa a intenção e direciona para o especialista mais adequado ou coordena a colaboração entre múltiplos especialistas.

2. **Agentes Especialistas** (10 especialistas):
   - **Especialista em Culturas**: Conhecimento sobre culturas como milho, mandioca, café e banana
   - **Meteorologista**: Análise e previsão de condições climáticas para agricultura
   - **Especialista em Pragas e Doenças**: Identificação e gestão de pragas e doenças agrícolas
   - **Especialista em Irrigação**: Otimização de recursos hídricos e sistemas de irrigação
   - **Especialista Financeiro**: Análise de custos, rendimentos e projeções econômicas
   - **Especialista em Design e Visualização**: Criação de representações visuais e layouts de plantações
   - **Especialista em Análise de Solo**: Interpretação de análises e características do solo
   - **Especialista em Fertilização**: Recomendações de adubação e nutrição vegetal
   - **Especialista em Sustentabilidade**: Práticas sustentáveis e certificações agrícolas

## Funcionalidades

- Análise e recomendações personalizadas para diferentes culturas
- Previsões meteorológicas aplicadas à agricultura
- Identificação e tratamento de pragas e doenças em plantações
- Estratégias de otimização de irrigação e uso de recursos hídricos
- Análise financeira e projeções econômicas para empreendimentos agrícolas
- Visualizações e representações gráficas de plantações e dados agrícolas
- Interpretação de análises de solo e recomendações de manejo
- Planos de adubação e nutrição vegetal personalizados
- Orientações sobre práticas sustentáveis e certificações
- Coordenação inteligente entre diferentes áreas de especialização

## Tecnologias Utilizadas

- Google Gemini API
- Python
- Google Colab
- Técnicas avançadas de engenharia de prompt
- Sistema de embeddings para processamento de documentos agrícolas

## Diferenciais

- Abordagem multiagente que simula uma equipe completa de especialistas trabalhando em conjunto
- Capacidade de contextualização e personalização para diferentes regiões e culturas
- Sistema de coordenação inteligente que integra conhecimentos de diferentes áreas
- Interface intuitiva que simplifica o acesso a conhecimentos agrícolas especializados
- Análise financeira integrada para tomada de decisões baseada em dados econômicos
- Capacidade de visualização para planejamento e apresentação de projetos agrícolas
- Recomendações de manejo de solo e fertilização baseadas em dados científicos
- Orientações sobre práticas sustentáveis e acesso a mercados premium

## Como Utilizar

Para utilizar o AgriSmart no Google Colab:

1. Obtenha uma API Key do Google Gemini em https://aistudio.google.com/
2. Faça upload dos arquivos do AgriSmart para o Google Colab
3. Execute o arquivo `agrismart_colab.py`
4. Insira sua API Key quando solicitado
5. Interaja com o sistema através do método `gerente.processar_mensagem()`

Exemplos de perguntas que você pode fazer:

- "Qual a melhor época para plantar mandioca?"
- "Minhas plantas de café estão com manchas amarelas nas folhas. O que pode ser?"
- "Qual o melhor sistema de irrigação para banana em região com escassez de água?"
- "Qual o custo estimado e retorno esperado para 1 hectare de café arábica?"
- "Gostaria de visualizar como ficaria uma área de 5 hectares com plantação de café."
- "Meu solo tem pH 5.2 e textura argilosa. O que isso significa para o cultivo de milho?"
- "Quais fertilizantes devo usar para uma plantação de café com deficiência de nitrogênio?"
- "Quais certificações orgânicas são mais valorizadas para exportação de café?"

## Sobre o Projeto

Este projeto foi desenvolvido como parte da Imersão Lura (Alura + Google Gemini), aplicando os conhecimentos adquiridos nas aulas 4 e 5 sobre criação de chatbots com a API Gemini e construção de agentes autônomos.
