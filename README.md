# Lexi AI 🤖
- **Status do Projeto:** (Protótipo Conceitual - Curso Potenc.IA | Criadoras do Futuro com IA)

- Um protótipo de assistente de IA focado em recomendações éticas e hiper-personalizadas, construído com Streamlit e a API do Google Gemini.

# 🎯 O Problema
Na era da informação, sofremos com o **"paradoxo da escolha"** (ou fadiga de decisão). Algoritmos de recomendação atuais são superficiais e falham em dois pontos principais:

1. **Ignoram Filtros Negativos:** Eles não entendem preferências de nicho ou restrições morais/éticas específicas (ex: "quero séries de romance, mas que não tenham cenas de violência gráfica").

2. **Geram Dependência:** Muitos sistemas de IA são projetados para maximizar o "engajamento", incentivando a dependência emocional e o uso excessivo, em vez de focar na eficiência.

# ✨ A Solução: A "Persona Virtual"
Lexi AI resolve isso através de um sistema de "Persona Virtual" de duas camadas:

1. **A "Persona-Mãe":** É o *SYSTEM_PROMPT* principal da IA. Ela contém os Guardrails Éticos (a regra de "não ser terapeuta"), a personalidade da IA (prestativa, mas não íntima) e a lógica de como ela deve construir a persona do usuário.

2. **A "Persona do Usuário":** É o perfil que o usuário constrói. Ele armazena não apenas gostos (*gosto de K-pop e cottage core*), mas principalmente seus filtros e limites (*odeio filmes de terror*, *amo séries sobre pés de galinha*).

O objetivo é ser uma ferramenta de eficiência: um "segundo cérebro" que economiza o tempo de pesquisa do usuário, para que ele possa usar seu tempo de descanso para descansar.

# 🚀 Funcionalidades Principais (do Protótipo)
- **Interface de Chat:** Uma interface limpa e reativa construída com Streamlit.

- **Gestão de Segredos:** O projeto usa o *secrets.toml* do Streamlit e o *.gitignore* para proteger a chave da API e o "Prompt-Mãe", permitindo que o código seja público sem expor dados sensíveis.

- **Guardrails Éticos:** A IA é instruída (via "Persona-Mãe") a identificar e redirecionar conversas que saem do escopo de recomendações (como pedidos de terapia), visando a saúde mental do usuário.

- **Chat Persistente:** O histórico da conversa é salvo na sessão (usando *st.session_state*).

# 🧠 Conceitos-Chave (Arquitetura Futura)
Este protótipo prova a "Fase 0", mas o design completo do projeto (discutido na concepção) prevê um sistema mais robusto:

- **O "Robô Invisível" (Backend):** Um processo assíncrono que faria a coleta de dados (Data Scraping) em mídias sociais (ex: "edits de fãs" no TikTok) e fóruns (ex: MyDramaList).

- **Descoberta de Tópicos (Topic Modeling):** Em vez de usar tags pré-definidas, o "Robô" usaria IA para descobrir tags relevantes (como "engraçado" ou "hot edit") analisando a frequência de palavras nas discussões de fãs, permitindo recomendações de nicho.

# 🛠️ Tecnologias Utilizadas
- **Python**

- **Streamlit** (Para a interface web)

- **Google Gemini API** (Para o cérebro da IA)

- **GitHub Codespaces** (Como ambiente de desenvolvimento na nuvem)

# 🏃‍♀️ Como Executar o Protótipo
Este projeto foi desenvolvido para rodar facilmente no GitHub Codespaces.

1. **Inicie o Codespace:** Abra este repositório em um novo Codespace.

2. **Crie seus Segredos:**

  - Crie uma nova pasta na raiz do projeto chamada *.streamlit*.
    
  - Dentro dela, crie um arquivo chamado *secrets.toml*.
    
  - Cole nesse arquivo sua API key e o "Prompt-Mãe".

3. **Instale as Dependências:**

  - Crie um arquivo *requirements.txt* e adicione *streamlit* e *google-generativeai*.
  
  - No terminal do Codespaces, rode: *pip install -r requirements.txt*

4. **Rode o App:**

  - No terminal, rode: *streamlit run app.py*
  
  - O Codespaces irá notificá-lo para abrir o aplicativo em uma nova aba do navegador.

# 🔮 Próximos Passos (Fases Futuras)
- **[Fase 1 - Mídia]:** Expandir o protótipo para se conectar a bancos de dados reais (como Common Sense Media) para validar os filtros.

- **[Fase 2 - Estilo e Compras]:** Implementar Visão Computacional (CV) para que a IA possa analisar fotos de roupas e recomendar looks com base em estilos (Cottage Core, Y2K).

- **[Fase 3 - O Robô]:** Construir o "Robô Invisível" (backend worker) para fazer a coleta de dados e a descoberta de tópicos em tempo real.
