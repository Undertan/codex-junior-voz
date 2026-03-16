# 🎤 Codex Junior - Assistente de Voz para Iniciantes em Programação

**Projeto 100% offline e gratuito** desenvolvido para o desafio da DIO.

## O que o projeto faz?
- Entende sua voz em português brasileiro
- Responde perguntas sobre programação Python de forma simples e paciente
- Fala a resposta em voz alta
- Funciona sem internet depois da instalação inicial

## Por que não usei a API do ChatGPT?
Utilizei **Ollama (llama3.2:1b)** no lugar da API paga da OpenAI, pois não tenho acesso a chaves pagas.  
Mantive toda a funcionalidade do desafio original, mas de forma gratuita e local.

## Tecnologias utilizadas
- Ollama + llama3.2:1b (LLM local)
- faster-whisper tiny (transcrição de voz)
- sounddevice + numpy (captura de áudio)
- pyttsx3 (síntese de voz offline)

## Requisitos testados
- Notebook Intel i5 6300U
- 8 GB RAM
- Windows 10 Pro

## Como rodar (passo a passo)

1. Baixe e instale o Ollama → https://ollama.com
2. No terminal:
ollama pull llama3.2:1b
text3. Crie o ambiente virtual:
python -m venv venv
venv\Scripts\activate
text4. Instale as dependências:
pip install -r requirements.txt
text5. Execute o assistente:
python main.py
textDiga “sair” ou “tchau” para encerrar.

## Demonstração
(Você vai colocar o link do vídeo aqui depois de gravar)

**Desenvolvido por Leandro da Silva**  
Parauapebas/PA – Março 2026