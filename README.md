# 🦊 Missão Nível S: Enxoval do Vicente 🍥

Bem-vindo ao repositório oficial da missão mais importante do Mundo Ninja: **A chegada do Vicente!** 

Este projeto é um aplicativo interativo feito em [Streamlit](https://streamlit.io/), desenvolvido para ajudar o casal a gerenciar e acompanhar a lista do enxoval e o chá de bebê, garantindo que nenhum pergaminho (ou pacote de fralda) fique para trás! *Dattebayo!*

## 📜 Jutsus e Funcionalidades

- **Controle Ninja de Compras:** Tabela interativa para marcar os itens que já foram garantidos e acompanhar o progresso.
- **Rastreador de Ofertas (Byakugan de Promoções):** Links de busca automatizada e direcionada para encontrar as melhores ofertas e promoções nas principais lojas da internet.
- **Invocação de Novos Itens:** Formulário dinâmico para adicionar novos itens à lista. O robô automaticamente gera um link inteligente focado em achar descontos para aquele item no Google Shopping!
- **Visual Shinobi:** Estilização exclusiva e customizada com as cores clássicas e a garra do universo Naruto.

## 🛠️ Ferramentas Ninja (Tecnologias Usadas)

- **Python** (O Chakra principal)
- **Streamlit** (Para a Interface Web)
- **Pandas** (Para manipular os pergaminhos de dados do Excel/CSV)

## 🚀 Como executar sua missão localmente

1. Faça o clone deste repositório na sua máquina:
```bash
git clone https://github.com/LucasTavaresRibeiro/chaVicente.git
```
2. Instale as dependências necessárias:
```bash
pip install -r requirements.txt
```
3. Libere seu chakra e execute a aplicação:
```bash
streamlit run app.py
```

## ☁️ Implantação (Aldeia da Nuvem)

Este aplicativo está otimizado para ser hospedado gratuitamente no **Streamlit Community Cloud**. 
> **Aviso de Persistência:** Atualmente, os dados são salvos em um arquivo local `enxoval.csv`. Para implantações na nuvem (onde o armazenamento é efêmero), é recomendado o uso do módulo `st.connection` integrado ao **Google Sheets** para que os dados persistam mesmo quando o servidor "dormir".

---
**"Eu não vou voltar atrás na minha palavra! Esse é o meu jeito ninja!"** 👊
