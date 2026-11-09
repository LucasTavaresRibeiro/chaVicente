import streamlit as st
import pandas as pd
import os
import base64

# Configuração da página
st.set_page_config(page_title="Enxoval do Vicente - Dattebayo!", page_icon="🦊", layout="wide")

# Função para converter a imagem em base64
@st.cache_data
def get_base64_of_bin_file(bin_file):
    if os.path.exists(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    return ""

bg_image = get_base64_of_bin_file("background.jpg")

css_bg = f"""
<style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{bg_image}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* Overlay semi-transparente para as letras ficarem visíveis */
    .block-container {{
        background-color: rgba(18, 18, 18, 0.88); /* Fundo escuro com 88% de opacidade */
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.6);
    }}

    h1, h2, h3, h4, h5, h6, p, label, span {{
        color: #ffffff !important;
    }}

    h1, h2, h3 {{
        color: #ff7b00 !important; /* Laranja Naruto */
        font-family: 'Arial Black', sans-serif;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
    }}
    
    .stButton>button {{
        background-color: #004b87; /* Azul Escuro */
        color: white !important;
        border-radius: 8px;
        border: 2px solid #ff7b00;
        font-weight: bold;
    }}
    .stButton>button:hover {{
        background-color: #ff7b00;
        color: white !important;
        border: 2px solid #004b87;
    }}
</style>
"""
st.markdown(css_bg, unsafe_allow_html=True)

st.title("🦊 Enxoval do Vicente - Missão Nível S 🍥")
st.markdown("Bem-vindos ao painel de controle do enxoval e chá de bebê do **Vicente** e da **Mamãe Bruna**! *Dattebayo!*")

DATA_FILE = "enxoval.csv"
LOJAS_FILE = "lojas.csv"
SHEIN_FILE = "shein.csv"

# ==============================================================================
# DADOS INICIAIS COMPLETOS DO ENXOVAL (TODOS OS PRINTS ORGANIZADOS POR PRIORIDADE)
# ==============================================================================
INITIAL_DATA = [
    # -------------------------------------------------------------------------
    # CATEGORIA: QUARTO
    # -------------------------------------------------------------------------
    # Prioridade Alta (3 pontos)
    {"Item": "Berço", "Categoria": "Quarto", "Qtd": 1, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 550,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=berco+bebe",
     "Busca 2 (Específica)": "https://www.magazineluiza.com.br/busca/berco+bebe/",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=berco+bebe"},
    
    {"Item": "Colchão para berço", "Categoria": "Quarto", "Qtd": 1, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 150,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=colchao+para+berco+americano",
     "Busca 2 (Específica)": "https://www.magazineluiza.com.br/busca/colchao+para+berco/",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=colchao+para+berco"},

    {"Item": "Lençol para berço", "Categoria": "Quarto", "Qtd": 4, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 40,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=lencol+para+berco+elastico",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=lencol+berco+elastico",
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/lencol-berco"},

    {"Item": "Manta", "Categoria": "Quarto", "Qtd": 3, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 45,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=manta+bebe+microfibra",
     "Busca 2 (Específica)": "https://www.renner.com.br/b?q=manta+bebe",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=manta+bebe"},

    {"Item": "Fralda de boca", "Categoria": "Quarto", "Qtd": 10, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 35,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=fralda+de+boca+bebe+pano",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=fralda+de+boca+bebe",
     "Busca 3 (Alternativa)": "https://www.drogasil.com.br/search?w=fralda+de+boca"},

    # Prioridade Média (2 pontos)
    {"Item": "Cômoda infantil", "Categoria": "Quarto", "Qtd": 1, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 350,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=comoda+infantil+bebe",
     "Busca 2 (Específica)": "https://www.magazineluiza.com.br/busca/comoda+infantil/",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=comoda+infantil"},

    {"Item": "Poltrona amamentação", "Categoria": "Quarto", "Qtd": 1, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 600,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=poltrona+amamentacao",
     "Busca 2 (Específica)": "https://www.magazineluiza.com.br/busca/poltrona+amamentacao/",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=poltrona+amamentacao"},

    {"Item": "Kit de berço", "Categoria": "Quarto", "Qtd": 1, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 150,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=kit+de+berco+algodao",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=kit+de+berco",
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/kit-berco"},

    {"Item": "Babá eletrônica", "Categoria": "Quarto", "Qtd": 1, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 300,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=baba+eletronica+com+camera",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=baba+eletronica+camera",
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/baba-eletronica-camera"},

    {"Item": "Trocador", "Categoria": "Quarto", "Qtd": 1, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 70,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=trocador+bebe+comoda",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=trocador+bebe",
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/trocador-bebe"},

    {"Item": "Protetor de colchão", "Categoria": "Quarto", "Qtd": 2, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 45,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=protetor+colchao+berco+impermeavel",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=protetor+colchao+berco+impermeavel",
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/protetor-colchao-berco"},

    {"Item": "Cobertor / edredom", "Categoria": "Quarto", "Qtd": 2, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Entre 0 e 3 meses", "Comprado": False, "Preço Médio": "R$ 60,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=cobertor+edredom+bebe",
     "Busca 2 (Específica)": "https://www.renner.com.br/b?q=cobertor+bebe",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=cobertor+bebe"},

    {"Item": "Cueiro", "Categoria": "Quarto", "Qtd": 2, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 35,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=cueiro+flanelado+bebe",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=cueiro+bebe",
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/cueiro-bebe"},

    {"Item": "Mosquiteiro para berço", "Categoria": "Quarto", "Qtd": 1, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 40,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=mosquiteiro+para+berco",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=mosquiteiro+berco",
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/mosquiteiro-berco"},

    {"Item": "Posicionador para dormir", "Categoria": "Quarto", "Qtd": 1, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 55,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=posicionador+para+dormir+bebe",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=posicionador+bebe+dormir",
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/posicionador-bebe"},

    {"Item": "Cabide infantil", "Categoria": "Quarto", "Qtd": 20, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 40,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=kit+cabide+infantil+veludo",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=kit+cabide+infantil",
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/cabide-infantil"},

    # Prioridade Baixa (1 ponto)
    {"Item": "Travesseiro", "Categoria": "Quarto", "Qtd": 1, "Prioridade": "⭐ Baixa", "Quando Comprar": "Entre 6 e 12 meses", "Comprado": False, "Preço Médio": "R$ 30,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=travesseiro+antissufocante+bebe",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=travesseiro+bebe",
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/travesseiro-bebe"},

    {"Item": "Fronha avulsa", "Categoria": "Quarto", "Qtd": 3, "Prioridade": "⭐ Baixa", "Quando Comprar": "Entre 6 e 12 meses", "Comprado": False, "Preço Médio": "R$ 20,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=fronha+avulsa+berco+bebe",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=fronha+bebe",
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/fronha-bebe"},

    {"Item": "Naninha", "Categoria": "Quarto", "Qtd": 1, "Prioridade": "⭐ Baixa", "Quando Comprar": "Entre 0 e 3 meses", "Comprado": False, "Preço Médio": "R$ 35,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=naninha+bebe+pelucia",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=naninha+bebe",
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/naninha-bebe"},

    {"Item": "Ninho", "Categoria": "Quarto", "Qtd": 1, "Prioridade": "⭐ Baixa", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 120,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=ninho+redutor+de+berco",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=ninho+redutor+berco",
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/ninho-redutor-berco"},

    {"Item": "Móbile para berço", "Categoria": "Quarto", "Qtd": 1, "Prioridade": "⭐ Baixa", "Quando Comprar": "Entre 0 e 3 meses", "Comprado": False, "Preço Médio": "R$ 80,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=mobile+para+berco+musical",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=mobile+berco",
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/mobile-berco"},

    {"Item": "Livro diário do bebê", "Categoria": "Quarto", "Qtd": 1, "Prioridade": "⭐ Baixa", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 45,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=livro+diario+do+bebe+recordacoes",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=livro+diario+do+bebe",
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/livro-diario-do-bebe"},

    # -------------------------------------------------------------------------
    # CATEGORIA: BANHO
    # -------------------------------------------------------------------------
    # Prioridade Alta (3 pontos)
    {"Item": "Banheira", "Categoria": "Banho", "Qtd": 1, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 160,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=banheira+bebe+com+suporte",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=banheira+bebe+suporte",
     "Busca 3 (Alternativa)": "https://www.magazineluiza.com.br/busca/banheira+bebe/"},

    {"Item": "Toalha", "Categoria": "Banho", "Qtd": 3, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 50,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=toalha+de+banho+bebe+com+capuz",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=toalha+capuz+bebe",
     "Busca 3 (Alternativa)": "https://www.renner.com.br/b?q=toalha+bebe"},

    # Prioridade Média (2 pontos)
    {"Item": "Termômetro para banho", "Categoria": "Banho", "Qtd": 1, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 25,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=termometro+para+banho+bebe",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=termometro+banho+bebe",
     "Busca 3 (Alternativa)": "https://www.drogasil.com.br/search?w=termometro+banho"},

    # Prioridade Baixa (1 ponto)
    {"Item": "Almofada para banho", "Categoria": "Banho", "Qtd": 1, "Prioridade": "⭐ Baixa", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 70,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=almofada+para+banho+bebe",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=almofada+banho+bebe",
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/almofada-banho-bebe"},

    {"Item": "Caneca para banho", "Categoria": "Banho", "Qtd": 1, "Prioridade": "⭐ Baixa", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 25,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=caneca+chuveiro+banho+bebe",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=caneca+banho+bebe",
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/caneca-banho-bebe"},

    {"Item": "Brinquedos para banho", "Categoria": "Banho", "Qtd": 3, "Prioridade": "⭐ Baixa", "Quando Comprar": "Entre 3 e 6 meses", "Comprado": False, "Preço Médio": "R$ 30,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=brinquedos+para+banho+bebe",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=brinquedos+banho+bebe",
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/brinquedos-banho-bebe"},

    # -------------------------------------------------------------------------
    # CATEGORIA: HIGIENE
    # -------------------------------------------------------------------------
    # Prioridade Alta (3 pontos)
    {"Item": "Fralda descartável tamanho RN", "Categoria": "Higiene", "Qtd": 2, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 60,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=Fralda+descartavel+tamanho+RN",
     "Busca 2 (Específica)": "https://www.drogasil.com.br/search?w=fralda+rn",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=fralda+rn"},

    {"Item": "Fralda descartável tamanho P", "Categoria": "Higiene", "Qtd": 15, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 75,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=Fralda+descartavel+tamanho+P",
     "Busca 2 (Específica)": "https://www.drogasil.com.br/search?w=fralda+tamanho+p",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=fralda+tamanho+p"},

    {"Item": "Fralda descartável tamanho M", "Categoria": "Higiene", "Qtd": 30, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Entre 3 e 6 meses", "Comprado": False, "Preço Médio": "R$ 85,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=Fralda+descartavel+tamanho+M",
     "Busca 2 (Específica)": "https://www.drogasil.com.br/search?w=fralda+tamanho+m",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=fralda+tamanho+m"},

    {"Item": "Fralda descartável tamanho G", "Categoria": "Higiene", "Qtd": 25, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Entre 6 e 12 meses", "Comprado": False, "Preço Médio": "R$ 90,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=Fralda+descartavel+tamanho+G",
     "Busca 2 (Específica)": "https://www.drogasil.com.br/search?w=fralda+tamanho+g",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=fralda+tamanho+g"},

    {"Item": "Lenço umedecido", "Categoria": "Higiene", "Qtd": 12, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 45,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=lenco+umedecido+bebe+recem+nascido",
     "Busca 2 (Específica)": "https://www.drogaraia.com.br/search?w=lenco+umedecido",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=lenco+umedecido+bebe"},

    {"Item": "Creme para assadura", "Categoria": "Higiene", "Qtd": 3, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 40,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=creme+para+assadura+bebe+bepantol",
     "Busca 2 (Específica)": "https://www.drogasil.com.br/search?w=creme+assadura+bebe",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=creme+assadura+bebe"},

    {"Item": "Algodão", "Categoria": "Higiene", "Qtd": 6, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 15,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=algodao+em+disco+ou+quadrado+bebe",
     "Busca 2 (Específica)": "https://www.drogasil.com.br/search?w=algodao+bebe",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=algodao+bebe"},

    {"Item": "Shampoo", "Categoria": "Higiene", "Qtd": 1, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 22,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=shampoo+bebe+recem+nascido",
     "Busca 2 (Específica)": "https://www.drogasil.com.br/search?w=shampoo+bebe",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=shampoo+bebe"},

    {"Item": "Sabonete", "Categoria": "Higiene", "Qtd": 1, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 25,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=sabonete+liquido+bebe+glicerina",
     "Busca 2 (Específica)": "https://www.drogasil.com.br/search?w=sabonete+liquido+bebe",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=sabonete+liquido+bebe"},

    {"Item": "Hastes flexíveis (cotonetes)", "Categoria": "Higiene", "Qtd": 3, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 12,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=hastes+flexiveis+cotonetes+bebe",
     "Busca 2 (Específica)": "https://www.drogasil.com.br/search?w=hastes+flexiveis+bebe",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=cotonete+bebe"},

    {"Item": "Pente / escova de cabelo", "Categoria": "Higiene", "Qtd": 1, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 25,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=pente+escova+de+cabelo+bebe",
     "Busca 2 (Específica)": "https://www.drogasil.com.br/search?w=escova+cabelo+bebe",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=kit+escova+pente+bebe"},

    # Prioridade Média (2 pontos)
    {"Item": "Fralda de tecido", "Categoria": "Higiene", "Qtd": 2, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 35,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=fralda+de+tecido+bebe",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=fralda+tecido+bebe",
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/fralda-tecido-bebe"},

    {"Item": "Creme hidratante", "Categoria": "Higiene", "Qtd": 1, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Entre 0 e 3 meses", "Comprado": False, "Preço Médio": "R$ 38,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=creme+hidratante+bebe+recem+nascido",
     "Busca 2 (Específica)": "https://www.drogasil.com.br/search?w=hidratante+bebe",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=hidratante+bebe"},

    # Prioridade Baixa (1 ponto)
    {"Item": "Lixeira anti odor", "Categoria": "Higiene", "Qtd": 1, "Prioridade": "⭐ Baixa", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 140,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=lixeira+anti+odor+fraldas+bebe",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=lixeira+anti+odor+fraldas",
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/lixeira-anti-odor-fraldas"},

    {"Item": "Perfume (colônia)", "Categoria": "Higiene", "Qtd": 1, "Prioridade": "⭐ Baixa", "Quando Comprar": "Entre 3 e 6 meses", "Comprado": False, "Preço Médio": "R$ 30,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=perfume+colonia+bebe+sem+alcool",
     "Busca 2 (Específica)": "https://www.drogasil.com.br/search?w=colonia+bebe",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=colonia+bebe"},

    # -------------------------------------------------------------------------
    # CATEGORIA: ROUPAS (REGRA NUNCA SHOPEE / MERCADO LIVRE)
    # -------------------------------------------------------------------------
    # Prioridade Alta (3 pontos)
    {"Item": "Body RN", "Categoria": "Roupas", "Qtd": 6, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 80,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=kit+body+bebe+rn",
     "Busca 2 (Específica)": "https://www.renner.com.br/b?q=body+bebe+rn",
     "Busca 3 (Alternativa)": "https://www.dafiti.com.br/catalog/?q=body+bebe+rn"},

    {"Item": "Body P", "Categoria": "Roupas", "Qtd": 6, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 80,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=kit+body+bebe+p",
     "Busca 2 (Específica)": "https://www.renner.com.br/b?q=body+bebe+p",
     "Busca 3 (Alternativa)": "https://www.dafiti.com.br/catalog/?q=body+bebe+p"},

    {"Item": "Body M", "Categoria": "Roupas", "Qtd": 4, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Entre 0 e 3 meses", "Comprado": False, "Preço Médio": "R$ 75,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=kit+body+bebe+m",
     "Busca 2 (Específica)": "https://www.renner.com.br/b?q=body+bebe+m",
     "Busca 3 (Alternativa)": "https://www.dafiti.com.br/catalog/?q=body+bebe+m"},

    {"Item": "Body G", "Categoria": "Roupas", "Qtd": 4, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Entre 3 e 6 meses", "Comprado": False, "Preço Médio": "R$ 75,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=kit+body+bebe+g",
     "Busca 2 (Específica)": "https://www.renner.com.br/b?q=body+bebe+g",
     "Busca 3 (Alternativa)": "https://www.dafiti.com.br/catalog/?q=body+bebe+g"},

    {"Item": "Macacão RN", "Categoria": "Roupas", "Qtd": 6, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 60,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=macacao+bebe+rn+algodao",
     "Busca 2 (Específica)": "https://www.renner.com.br/b?q=macacao+bebe+rn",
     "Busca 3 (Alternativa)": "https://www.cea.com.br/busca?q=macacao%20bebe%20rn"},

    {"Item": "Macacão P", "Categoria": "Roupas", "Qtd": 6, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 60,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=macacao+bebe+p+algodao",
     "Busca 2 (Específica)": "https://www.renner.com.br/b?q=macacao+bebe+p",
     "Busca 3 (Alternativa)": "https://www.cea.com.br/busca?q=macacao%20bebe%20p"},

    {"Item": "Macacão M", "Categoria": "Roupas", "Qtd": 4, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Entre 0 e 3 meses", "Comprado": False, "Preço Médio": "R$ 65,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=macacao+bebe+m+algodao",
     "Busca 2 (Específica)": "https://www.renner.com.br/b?q=macacao+bebe+m",
     "Busca 3 (Alternativa)": "https://www.cea.com.br/busca?q=macacao%20bebe%20m"},

    {"Item": "Culote RN", "Categoria": "Roupas", "Qtd": 6, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 45,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=culote+mijao+bebe+rn",
     "Busca 2 (Específica)": "https://www.renner.com.br/b?q=culote+bebe+rn",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=mijao+bebe+rn"},

    {"Item": "Culote P", "Categoria": "Roupas", "Qtd": 6, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 45,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=culote+mijao+bebe+p",
     "Busca 2 (Específica)": "https://www.renner.com.br/b?q=culote+bebe+p",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=mijao+bebe+p"},

    {"Item": "Culote M", "Categoria": "Roupas", "Qtd": 4, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Entre 0 e 3 meses", "Comprado": False, "Preço Médio": "R$ 50,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=culote+mijao+bebe+m",
     "Busca 2 (Específica)": "https://www.renner.com.br/b?q=culote+bebe+m",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=mijao+bebe+m"},

    {"Item": "Meia", "Categoria": "Roupas", "Qtd": 6, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 30,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=kit+meia+recem+nascido+bebe",
     "Busca 2 (Específica)": "https://www.renner.com.br/b?q=meia+bebe",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=meia+bebe"},

    {"Item": "Sapatinho bebê", "Categoria": "Roupas", "Qtd": 4, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Entre 0 e 3 meses", "Comprado": False, "Preço Médio": "R$ 40,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=sapatinho+bebe+tricot+ou+tecido",
     "Busca 2 (Específica)": "https://www.renner.com.br/b?q=sapatinho+bebe",
     "Busca 3 (Alternativa)": "https://www.dafiti.com.br/catalog/?q=sapatinho+bebe"},

    # Prioridade Média (2 pontos)
    {"Item": "Macacão G", "Categoria": "Roupas", "Qtd": 4, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Entre 3 e 6 meses", "Comprado": False, "Preço Médio": "R$ 65,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=macacao+bebe+g+algodao",
     "Busca 2 (Específica)": "https://www.renner.com.br/b?q=macacao+bebe+g",
     "Busca 3 (Alternativa)": "https://www.cea.com.br/busca?q=macacao%20bebe%20g"},

    {"Item": "Culote G", "Categoria": "Roupas", "Qtd": 4, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Entre 3 e 6 meses", "Comprado": False, "Preço Médio": "R$ 50,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=culote+mijao+bebe+g",
     "Busca 2 (Específica)": "https://www.renner.com.br/b?q=culote+bebe+g",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=mijao+bebe+g"},

    {"Item": "Casaquinho P", "Categoria": "Roupas", "Qtd": 3, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 50,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=casaquinho+bebe+p+tricot+algodao",
     "Busca 2 (Específica)": "https://www.renner.com.br/b?q=casaquinho+bebe",
     "Busca 3 (Alternativa)": "https://www.dafiti.com.br/catalog/?q=casaquinho+bebe"},

    {"Item": "Casaquinho M", "Categoria": "Roupas", "Qtd": 2, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Entre 0 e 3 meses", "Comprado": False, "Preço Médio": "R$ 55,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=casaquinho+bebe+m+tricot+algodao",
     "Busca 2 (Específica)": "https://www.renner.com.br/b?q=casaquinho+bebe",
     "Busca 3 (Alternativa)": "https://www.dafiti.com.br/catalog/?q=casaquinho+bebe"},

    {"Item": "Casaquinho G", "Categoria": "Roupas", "Qtd": 2, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Entre 3 e 6 meses", "Comprado": False, "Preço Médio": "R$ 55,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=casaquinho+bebe+g+tricot+algodao",
     "Busca 2 (Específica)": "https://www.renner.com.br/b?q=casaquinho+bebe",
     "Busca 3 (Alternativa)": "https://www.dafiti.com.br/catalog/?q=casaquinho+bebe"},

    {"Item": "Conjunto bebê P", "Categoria": "Roupas", "Qtd": 2, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Entre 0 e 3 meses", "Comprado": False, "Preço Médio": "R$ 60,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=conjunto+bebe+p",
     "Busca 2 (Específica)": "https://www.renner.com.br/b?q=conjunto+bebe",
     "Busca 3 (Alternativa)": "https://www.cea.com.br/busca?q=conjunto%20bebe"},

    {"Item": "Conjunto bebê M", "Categoria": "Roupas", "Qtd": 3, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Entre 0 e 3 meses", "Comprado": False, "Preço Médio": "R$ 65,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=conjunto+bebe+m",
     "Busca 2 (Específica)": "https://www.renner.com.br/b?q=conjunto+bebe",
     "Busca 3 (Alternativa)": "https://www.cea.com.br/busca?q=conjunto%20bebe"},

    {"Item": "Conjunto bebê G", "Categoria": "Roupas", "Qtd": 3, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Entre 3 e 6 meses", "Comprado": False, "Preço Médio": "R$ 70,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=conjunto+bebe+g",
     "Busca 2 (Específica)": "https://www.renner.com.br/b?q=conjunto+bebe",
     "Busca 3 (Alternativa)": "https://www.cea.com.br/busca?q=conjunto%20bebe"},

    {"Item": "Conjunto bebê GG", "Categoria": "Roupas", "Qtd": 3, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Entre 6 e 12 meses", "Comprado": False, "Preço Médio": "R$ 70,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=conjunto+bebe+gg",
     "Busca 2 (Específica)": "https://www.renner.com.br/b?q=conjunto+bebe",
     "Busca 3 (Alternativa)": "https://www.cea.com.br/busca?q=conjunto%20bebe"},

    {"Item": "Luva", "Categoria": "Roupas", "Qtd": 2, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 15,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=luva+para+bebe+recem+nascido",
     "Busca 2 (Específica)": "https://www.renner.com.br/b?q=luva+bebe",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=luva+bebe"},

    {"Item": "Touca", "Categoria": "Roupas", "Qtd": 2, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Entre 0 e 3 meses", "Comprado": False, "Preço Médio": "R$ 20,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=touca+gorro+bebe+recem+nascido",
     "Busca 2 (Específica)": "https://www.renner.com.br/b?q=touca+bebe",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=touca+bebe"},

    # -------------------------------------------------------------------------
    # CATEGORIA: PASSEIO
    # -------------------------------------------------------------------------
    # Prioridade Alta (3 pontos)
    {"Item": "Cadeirinha para carro / bebê conforto", "Categoria": "Passeio", "Qtd": 1, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 450,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=cadeirinha+para+carro+bebe+conforto",
     "Busca 2 (Específica)": "https://www.magazineluiza.com.br/busca/bebe+conforto/",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=bebe+conforto"},

    {"Item": "Carrinho de bebê", "Categoria": "Passeio", "Qtd": 1, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 850,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=carrinho+de+bebe+travel+system",
     "Busca 2 (Específica)": "https://www.magazineluiza.com.br/busca/carrinho+de+bebe/",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=carrinho+de+bebe"},

    {"Item": "Bolsa / mochila", "Categoria": "Passeio", "Qtd": 2, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 180,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=mochila+maternidade+bebe+termica",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=bolsa+maternidade",
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/bolsa-maternidade"},

    # Prioridade Média (2 pontos)
    {"Item": "Canguru", "Categoria": "Passeio", "Qtd": 1, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Entre 0 e 3 meses", "Comprado": False, "Preço Médio": "R$ 120,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=canguru+ergonomico+para+bebe",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=canguru+bebe",
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/canguru-bebe"},

    {"Item": "Trocador portátil", "Categoria": "Passeio", "Qtd": 1, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 45,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=trocador+portatil+bolsa+bebe",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=trocador+portatil+bebe",
     "Busca 3 (Alternativa)": "https://www.drogasil.com.br/search?w=trocador+portatil"},

    {"Item": "Apoio para cabeça", "Categoria": "Passeio", "Qtd": 1, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Entre 0 e 3 meses", "Comprado": False, "Preço Médio": "R$ 35,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=apoio+para+cabeca+bebe+conforto",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=apoio+cabeca+bebe+conforto",
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/apoio-cabeca-bebe"},

    {"Item": "Protetor solar para vidro do carro", "Categoria": "Passeio", "Qtd": 2, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 30,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=protetor+solar+vidro+carro+bebe",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=protetor+solar+carro+bebe",
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/protetor-solar-carro-bebe"},

    # Prioridade Baixa (1 ponto)
    {"Item": "Colchonete / capa para carrinho", "Categoria": "Passeio", "Qtd": 1, "Prioridade": "⭐ Baixa", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 50,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=colchonete+capa+para+carrinho+bebe",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=capa+carrinho+bebe",
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/capa-carrinho-bebe"},

    {"Item": "Capa de chuva para carrinho", "Categoria": "Passeio", "Qtd": 1, "Prioridade": "⭐ Baixa", "Quando Comprar": "Entre 0 e 3 meses", "Comprado": False, "Preço Médio": "R$ 40,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=capa+de+chuva+para+carrinho+bebe",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=capa+chuva+carrinho+bebe",
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/capa-chuva-carrinho-bebe"},

    {"Item": "Espelho retrovisor para carro", "Categoria": "Passeio", "Qtd": 1, "Prioridade": "⭐ Baixa", "Quando Comprar": "Entre 0 e 3 meses", "Comprado": False, "Preço Médio": "R$ 45,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=espelho+retrovisor+carro+bebe+conforto",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=espelho+retrovisor+bebe+carro",
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/espelho-retrovisor-bebe-carro"},

    {"Item": "Capa protetora para banco do carro", "Categoria": "Passeio", "Qtd": 1, "Prioridade": "⭐ Baixa", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 50,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=capa+protetora+banco+carro+cadeirinha",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=protetor+banco+carro+cadeirinha",
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/protetor-banco-carro-cadeirinha"},

    # -------------------------------------------------------------------------
    # CATEGORIA: PARA MAMÃE (MAMÃE BRUNA)
    # -------------------------------------------------------------------------
    # Prioridade Alta (3 pontos)
    {"Item": "Absorvente para seios", "Categoria": "Para mamãe", "Qtd": 4, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 25,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=absorvente+para+seios+amamentacao",
     "Busca 2 (Específica)": "https://www.drogasil.com.br/search?w=absorvente+seios",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=absorvente+seios"},

    {"Item": "Bomba Tira Leite Elétrica", "Categoria": "Para mamãe", "Qtd": 1, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 180,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=bomba+tira+leite+eletrica",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=bomba+tira+leite+eletrica",
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/bomba-tira-leite-eletrica"},

    {"Item": "Pomada de Lanolina (Fissuras Mamilo)", "Categoria": "Para mamãe", "Qtd": 1, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 60,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=pomada+lanolina+lansinoh",
     "Busca 2 (Específica)": "https://www.drogasil.com.br/search?w=lanolina",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=lanolina"},

    {"Item": "Absorvente Pós-Parto", "Categoria": "Para mamãe", "Qtd": 2, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 22,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=absorvente+pos-parto",
     "Busca 2 (Específica)": "https://www.drogasil.com.br/search?w=absorvente+pos+parto",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=absorvente+pos+parto"},

    # Prioridade Média (2 pontos)
    {"Item": "Almofada de amamentação", "Categoria": "Para mamãe", "Qtd": 1, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 90,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=almofada+de+amamentacao",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=almofada+amamentacao",
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/almofada-amamentacao"},

    # Prioridade Baixa (1 ponto)
    {"Item": "Tira leite manual", "Categoria": "Para mamãe", "Qtd": 1, "Prioridade": "⭐ Baixa", "Quando Comprar": "Entre 0 e 3 meses", "Comprado": False, "Preço Médio": "R$ 50,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=tira+leite+manual+bebe",
     "Busca 2 (Específica)": "https://www.drogasil.com.br/search?w=tira+leite+manual",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=tira+leite+manual"},

    {"Item": "Protetor para seios", "Categoria": "Para mamãe", "Qtd": 2, "Prioridade": "⭐ Baixa", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 35,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=protetor+para+seios+silicone+amamentacao",
     "Busca 2 (Específica)": "https://www.drogasil.com.br/search?w=protetor+seios+silicone",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=protetor+seios+silicone"},

    # -------------------------------------------------------------------------
    # CATEGORIA: ALIMENTAÇÃO
    # -------------------------------------------------------------------------
    # Prioridade Alta (3 pontos)
    {"Item": "Cadeira alimentação", "Categoria": "Alimentação", "Qtd": 1, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Entre 3 e 6 meses", "Comprado": False, "Preço Médio": "R$ 250,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=cadeira+de+alimentacao+bebe+alta",
     "Busca 2 (Específica)": "https://www.magazineluiza.com.br/busca/cadeira+alimentacao/",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=cadeira+alimentacao+bebe"},

    {"Item": "Mamadeira", "Categoria": "Alimentação", "Qtd": 3, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 130,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=kit+mamadeiras+philips+avent+petala",
     "Busca 2 (Específica)": "https://www.drogasil.com.br/search?w=mamadeira+avent",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=mamadeira+avent+petala"},

    {"Item": "Escova para mamadeira", "Categoria": "Alimentação", "Qtd": 1, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Entre 0 e 3 meses", "Comprado": False, "Preço Médio": "R$ 25,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=escova+lavar+mamadeira+e+bico",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=escova+mamadeira",
     "Busca 3 (Alternativa)": "https://www.drogasil.com.br/search?w=escova+mamadeira"},

    {"Item": "Babador", "Categoria": "Alimentação", "Qtd": 6, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Entre 0 e 3 meses", "Comprado": False, "Preço Médio": "R$ 45,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=babador+bebe+silicone+ou+tecido",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=babador+bebe",
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/babador-bebe"},

    {"Item": "Colher / talheres", "Categoria": "Alimentação", "Qtd": 1, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Entre 6 e 12 meses", "Comprado": False, "Preço Médio": "R$ 30,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=kit+colher+talheres+silicone+bebe",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=colher+silicone+bebe",
     "Busca 3 (Alternativa)": "https://www.drogasil.com.br/search?w=colher+bebe"},

    {"Item": "Prato", "Categoria": "Alimentação", "Qtd": 2, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Entre 6 e 12 meses", "Comprado": False, "Preço Médio": "R$ 45,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=prato+termico+ventosa+bebe",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=prato+bebe+ventosa",
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/prato-bebe"},

    # Prioridade Média (2 pontos)
    {"Item": "Bico de mamadeira", "Categoria": "Alimentação", "Qtd": 3, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Entre 0 e 3 meses", "Comprado": False, "Preço Médio": "R$ 35,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=bico+de+mamadeira+philips+avent",
     "Busca 2 (Específica)": "https://www.drogasil.com.br/search?w=bico+mamadeira",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=bico+mamadeira"},

    {"Item": "Esterilizador de mamadeira", "Categoria": "Alimentação", "Qtd": 1, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Entre 0 e 3 meses", "Comprado": False, "Preço Médio": "R$ 90,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=esterilizador+de+mamadeira+microondas",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=esterilizador+mamadeira",
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/esterilizador-mamadeira"},

    {"Item": "Escorredor de mamadeira", "Categoria": "Alimentação", "Qtd": 1, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Entre 0 e 3 meses", "Comprado": False, "Preço Médio": "R$ 45,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=escorredor+de+mamadeiras+e+copos",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=escorredor+mamadeira",
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/escorredor-mamadeira"},

    {"Item": "Pote para alimentos", "Categoria": "Alimentação", "Qtd": 1, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Entre 6 e 12 meses", "Comprado": False, "Preço Médio": "R$ 35,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=kit+potes+papinha+congelar+bebe",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=pote+papinha+bebe",
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/pote-papinha-bebe"},

    {"Item": "Copo transição", "Categoria": "Alimentação", "Qtd": 1, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Entre 6 e 12 meses", "Comprado": False, "Preço Médio": "R$ 40,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=copo+de+transicao+treinamento+bebe",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=copo+transicao+bebe",
     "Busca 3 (Alternativa)": "https://www.drogasil.com.br/search?w=copo+transicao"},

    {"Item": "Alimentador", "Categoria": "Alimentação", "Qtd": 1, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Entre 6 e 12 meses", "Comprado": False, "Preço Médio": "R$ 30,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=alimentador+porta+frutas+bebe+silicone",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=alimentador+silicone+bebe",
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/alimentador-bebe"},

    {"Item": "Chupeta", "Categoria": "Alimentação", "Qtd": 2, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Entre 0 e 3 meses", "Comprado": False, "Preço Médio": "R$ 40,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=chupeta+ortodontica+silicone+bebe",
     "Busca 2 (Específica)": "https://www.drogasil.com.br/search?w=chupeta",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=chupeta+bebe"},

    {"Item": "Porta chupeta", "Categoria": "Alimentação", "Qtd": 2, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Entre 0 e 3 meses", "Comprado": False, "Preço Médio": "R$ 20,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=porta+chupeta+esterilizavel",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=porta+chupeta",
     "Busca 3 (Alternativa)": "https://www.drogasil.com.br/search?w=porta+chupeta"},

    {"Item": "Prendedor de chupeta", "Categoria": "Alimentação", "Qtd": 2, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Entre 0 e 3 meses", "Comprado": False, "Preço Médio": "R$ 25,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=prendedor+de+chupeta+bebe",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=prendedor+chupeta",
     "Busca 3 (Alternativa)": "https://www.drogasil.com.br/search?w=prendedor+chupeta"},

    # Prioridade Baixa (1 ponto)
    {"Item": "Pote para leite materno", "Categoria": "Alimentação", "Qtd": 2, "Prioridade": "⭐ Baixa", "Quando Comprar": "Entre 0 e 3 meses", "Comprado": False, "Preço Médio": "R$ 35,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=potes+armazenamento+leite+materno",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=pote+leite+materno",
     "Busca 3 (Alternativa)": "https://www.drogasil.com.br/search?w=pote+leite+materno"},

    {"Item": "Porta leite em pó", "Categoria": "Alimentação", "Qtd": 1, "Prioridade": "⭐ Baixa", "Quando Comprar": "Entre 3 e 6 meses", "Comprado": False, "Preço Médio": "R$ 25,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=dosador+porta+leite+em+po+bebe",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=porta+leite+po",
     "Busca 3 (Alternativa)": "https://www.drogasil.com.br/search?w=porta+leite+po"},

    # -------------------------------------------------------------------------
    # CATEGORIA: SAÚDE
    # -------------------------------------------------------------------------
    # Prioridade Alta (3 pontos)
    {"Item": "Aspirador nasal", "Categoria": "Saúde", "Qtd": 1, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Entre 0 e 3 meses", "Comprado": False, "Preço Médio": "R$ 40,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=aspirador+nasal+bebe+sugador",
     "Busca 2 (Específica)": "https://www.drogasil.com.br/search?w=aspirador+nasal",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=aspirador+nasal+bebe"},

    {"Item": "Termômetro", "Categoria": "Saúde", "Qtd": 1, "Prioridade": "⭐⭐⭐ Alta", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 35,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=termometro+digital+bebe+infrvermelho+ou+ponta+flexivel",
     "Busca 2 (Específica)": "https://www.drogasil.com.br/search?w=termometro+digital",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=termometro+digital+bebe"},

    # Prioridade Média (2 pontos)
    {"Item": "Bolsa térmica para cólica", "Categoria": "Saúde", "Qtd": 1, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Gravidez", "Comprado": False, "Preço Médio": "R$ 35,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=bolsa+termica+para+colica+bebe+sementes",
     "Busca 2 (Específica)": "https://www.drogasil.com.br/search?w=bolsa+termica+colica",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=bolsa+termica+colica+bebe"},

    # -------------------------------------------------------------------------
    # CATEGORIA: ENTRETENIMENTO
    # -------------------------------------------------------------------------
    # Prioridade Média (2 pontos)
    {"Item": "Mordedor", "Categoria": "Entretenimento", "Qtd": 2, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Entre 0 e 3 meses", "Comprado": False, "Preço Médio": "R$ 25,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=mordedor+bebe+gel+silicone",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=mordedor+bebe",
     "Busca 3 (Alternativa)": "https://www.drogasil.com.br/search?w=mordedor+bebe"},

    {"Item": "Brinquedos interativos", "Categoria": "Entretenimento", "Qtd": 4, "Prioridade": "⭐⭐ Média", "Quando Comprar": "Entre 3 e 6 meses", "Comprado": False, "Preço Médio": "R$ 60,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=brinquedo+educativo+interativo+bebe",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=brinquedos+interativos+bebe",
     "Busca 3 (Alternativa)": "https://www.magazineluiza.com.br/busca/brinquedo+bebe/"},

    # Prioridade Baixa (1 ponto)
    {"Item": "Cadeira de descanso", "Categoria": "Entretenimento", "Qtd": 1, "Prioridade": "⭐ Baixa", "Quando Comprar": "Entre 0 e 3 meses", "Comprado": False, "Preço Médio": "R$ 280,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=cadeira+de+descanso+bebe+vibratoria",
     "Busca 2 (Específica)": "https://www.magazineluiza.com.br/busca/cadeira+descanso+bebe/",
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=cadeira+descanso+bebe"},

    {"Item": "Tapete de atividades", "Categoria": "Entretenimento", "Qtd": 1, "Prioridade": "⭐ Baixa", "Quando Comprar": "Entre 0 e 3 meses", "Comprado": False, "Preço Médio": "R$ 150,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=tapete+de+atividades+bebe+com+arco",
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=tapete+atividades+bebe",
     "Busca 3 (Alternativa)": "https://www.magazineluiza.com.br/busca/tapete+atividades+bebe/"}
]

INITIAL_LOJAS = [
    {"Loja": "Amazon - Categoria Bebês", "Link": "https://www.amazon.com.br/s?i=baby", "Monitorar": True},
    {"Loja": "Drogasil - Infantil", "Link": "https://www.drogasil.com.br/infantil.html", "Monitorar": True},
    {"Loja": "Riachuelo - Carter's", "Link": "https://www.riachuelo.com.br/infantil/bebes/carters", "Monitorar": True}
]

INITIAL_SHEIN = [
    {"Look": "Conjunto Moletom Infantil", "Preço Estimado": "R$ 45,00", "Link Shein": "https://br.shein.com/Kids-Clothing-c-2053.html", "Comprado": False}
]

def load_data(file_path, default_data):
    if os.path.exists(file_path):
        try:
            df = pd.read_csv(file_path)
            # Se a quantidade de itens for muito diferente da lista completa atualizada, atualiza com a nova lista completa
            if len(df) < len(default_data) or "Prioridade" not in df.columns or "Qtd" not in df.columns:
                df = pd.DataFrame(default_data)
                df.to_csv(file_path, index=False)
            return df
        except Exception:
            df = pd.DataFrame(default_data)
            df.to_csv(file_path, index=False)
            return df
    else:
        df = pd.DataFrame(default_data)
        df.to_csv(file_path, index=False)
        return df

if 'df' not in st.session_state:
    st.session_state.df = load_data(DATA_FILE, INITIAL_DATA)

if 'df_lojas' not in st.session_state:
    st.session_state.df_lojas = load_data(LOJAS_FILE, INITIAL_LOJAS)

if 'df_shein' not in st.session_state:
    st.session_state.df_shein = load_data(SHEIN_FILE, INITIAL_SHEIN)

# Navegação por Abas
tab1, tab2, tab3 = st.tabs(["📜 Pergaminho de Itens", "🏬 Lojas Monitoradas", "👗 Shein Kids"])

with tab1:
    st.subheader("📜 Lista Completa de Enxoval do Vicente")
    
    # Métricas de Resumo
    total_itens = len(st.session_state.df)
    itens_comprados = int(st.session_state.df["Comprado"].sum()) if "Comprado" in st.session_state.df else 0
    itens_pendentes = total_itens - itens_comprados
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("📦 Total de Itens", total_itens)
    m2.metric("✅ Já Comprados", itens_comprados)
    m3.metric("⏳ Missão Pendente", itens_pendentes)
    progresso = (itens_comprados / total_itens) if total_itens > 0 else 0.0
    m4.metric("🎯 Progresso do Enxoval", f"{int(progresso * 100)}%")
    
    st.progress(progresso)
    st.divider()

    # Filtros por Categoria e Prioridade
    f1, f2, f3 = st.columns([2, 2, 2])
    with f1:
        categorias_disponiveis = ["Todas"] + list(st.session_state.df['Categoria'].unique())
        cat_filtro = st.selectbox("📂 Filtrar por Categoria:", categorias_disponiveis)
    with f2:
        prioridades_disponiveis = ["Todas", "⭐⭐⭐ Alta", "⭐⭐ Média", "⭐ Baixa"]
        prio_filtro = st.selectbox("⭐ Filtrar por Prioridade:", prioridades_disponiveis)
    with f3:
        status_filtro = st.selectbox("📌 Status da Compra:", ["Todos", "Apenas Pendentes", "Apenas Comprados"])

    # Aplicando filtros
    df_filtrado = st.session_state.df.copy()
    if cat_filtro != "Todas":
        df_filtrado = df_filtrado[df_filtrado['Categoria'] == cat_filtro]
    if prio_filtro != "Todas":
        df_filtrado = df_filtrado[df_filtrado['Prioridade'] == prio_filtro]
    if status_filtro == "Apenas Pendentes":
        df_filtrado = df_filtrado[df_filtrado['Comprado'] == False]
    elif status_filtro == "Apenas Comprados":
        df_filtrado = df_filtrado[df_filtrado['Comprado'] == True]

    # Ordenação por Prioridade (Alta > Média > Baixa)
    ordem_prio = {"⭐⭐⭐ Alta": 1, "⭐⭐ Média": 2, "⭐ Baixa": 3}
    df_filtrado['ordem'] = df_filtrado['Prioridade'].map(ordem_prio).fillna(99)
    df_filtrado = df_filtrado.sort_values(by=['Categoria', 'ordem']).drop(columns=['ordem'])

    # Editor de Dados
    edited_df = st.data_editor(
        df_filtrado,
        column_config={
            "Qtd": st.column_config.NumberColumn("Qtd", min_value=1, step=1, width="small"),
            "Item": st.column_config.TextColumn("Item / Produto", width="medium"),
            "Categoria": st.column_config.SelectboxColumn("Categoria", options=["Quarto", "Banho", "Higiene", "Roupas", "Passeio", "Para mamãe", "Alimentação", "Saúde", "Entretenimento"], width="small"),
            "Prioridade": st.column_config.SelectboxColumn("Prioridade", options=["⭐⭐⭐ Alta", "⭐⭐ Média", "⭐ Baixa"], width="small"),
            "Quando Comprar": st.column_config.SelectboxColumn("Quando Comprar", options=["Gravidez", "Entre 0 e 3 meses", "Entre 3 e 6 meses", "Entre 6 e 12 meses"], width="medium"),
            "Comprado": st.column_config.CheckboxColumn("Comprado?", default=False, width="small"),
            "Preço Médio": st.column_config.TextColumn("Preço Médio", help="Estimativa base calculada"),
            "Busca 1 (Google)": st.column_config.LinkColumn("Google Shopping", display_text="Google 🛒"),
            "Busca 2 (Específica)": st.column_config.LinkColumn("Loja Direta", display_text="Loja 🛒"),
            "Busca 3 (Alternativa)": st.column_config.LinkColumn("Alternativa", display_text="Alternativa 🛒")
        },
        hide_index=True,
        use_container_width=True,
        key="data_editor_enxoval"
    )

    col_btn1, col_btn2 = st.columns([2, 4])
    with col_btn1:
        if st.button("Salvar Alterações no Pergaminho 💾", use_container_width=True):
            # Atualiza o dataframe global mantendo linhas filtradas
            st.session_state.df.update(edited_df)
            st.session_state.df.to_csv(DATA_FILE, index=False)
            st.success("Pergaminho Ninja atualizado com sucesso! 🍥")
            st.rerun()
    with col_btn2:
        if st.button("🔄 Restaurar Lista Oficial Completa dos Prints", help="Restaura a lista com todos os itens, quantidades e prioridades dos prints"):
            st.session_state.df = pd.DataFrame(INITIAL_DATA)
            st.session_state.df.to_csv(DATA_FILE, index=False)
            st.success("Lista oficial restaurada com sucesso!")
            st.rerun()

    st.divider()

    st.subheader("➕ Adicionar Novo Item à Missão")
    with st.form("add_item_form"):
        col_form1, col_form2 = st.columns([3, 1])
        with col_form1:
            new_item = st.text_input("Nome do Item / Produto")
        with col_form2:
            new_qtd = st.number_input("Quantidade", min_value=1, value=1, step=1)

        col_form3, col_form4, col_form5 = st.columns([2, 2, 2])
        
        categorias_existentes = list(st.session_state.df['Categoria'].unique())
        for cat_padrao in ["Quarto", "Banho", "Higiene", "Roupas", "Passeio", "Para mamãe", "Alimentação", "Saúde", "Entretenimento"]:
            if cat_padrao not in categorias_existentes:
                categorias_existentes.append(cat_padrao)
                
        with col_form3:
            cat_opcao = st.selectbox("Categoria", categorias_existentes + ["-- Criar Nova Categoria --"])
            nova_categoria_manual = st.text_input("Se escolheu criar nova, digite o nome:")
        with col_form4:
            new_prio = st.selectbox("Prioridade", ["⭐⭐⭐ Alta", "⭐⭐ Média", "⭐ Baixa"])
        with col_form5:
            new_quando = st.selectbox("Quando Comprar", ["Gravidez", "Entre 0 e 3 meses", "Entre 3 e 6 meses", "Entre 6 e 12 meses"])
            
        preco_medio_manual = st.text_input("Preço Médio Estimado (Ex: R$ 50,00)", value="R$ ")
        submit_button = st.form_submit_button("Adicionar à Missão Ninja 🥷")

        if submit_button and new_item:
            cat_final = nova_categoria_manual.strip() if cat_opcao == "-- Criar Nova Categoria --" and nova_categoria_manual.strip() else cat_opcao
            if cat_opcao == "-- Criar Nova Categoria --" and not nova_categoria_manual.strip():
                st.error("Por favor, digite o nome da nova categoria.")
            else:
                search_query = new_item.replace(' ', '+')
                link1 = f"https://www.google.com/search?tbm=shop&q={search_query}"
                
                if cat_final == "Roupas":
                    link2 = f"https://www.renner.com.br/b?q={search_query}"
                    link3 = f"https://www.dafiti.com.br/catalog/?q={search_query}"
                elif cat_final in ["Higiene", "Banho", "Para mamãe", "Saúde"]:
                    link2 = f"https://www.drogasil.com.br/search?w={search_query}"
                    link3 = f"https://www.amazon.com.br/s?k={search_query}"
                else:
                    link2 = f"https://www.amazon.com.br/s?k={search_query}"
                    link3 = f"https://www.magazineluiza.com.br/busca/{search_query}/"
                
                new_row = {
                    "Item": new_item, 
                    "Categoria": cat_final, 
                    "Qtd": int(new_qtd),
                    "Prioridade": new_prio,
                    "Quando Comprar": new_quando,
                    "Comprado": False, 
                    "Preço Médio": preco_medio_manual,
                    "Busca 1 (Google)": link1, 
                    "Busca 2 (Específica)": link2, 
                    "Busca 3 (Alternativa)": link3
                }
                
                st.session_state.df = pd.concat([st.session_state.df, pd.DataFrame([new_row])], ignore_index=True)
                st.session_state.df.to_csv(DATA_FILE, index=False)
                st.success(f"'{new_item}' adicionado com sucesso ao Pergaminho!")
                st.rerun()

with tab2:
    st.subheader("🏬 Lojas Aliadas (Monitoramento)")
    st.markdown("Adicione os links das lojas que vocês confiam e gostam de comprar. O bot focará nestas opções.")
    
    edited_lojas = st.data_editor(
        st.session_state.df_lojas,
        column_config={
            "Monitorar": st.column_config.CheckboxColumn("Monitorar?", default=True),
            "Link": st.column_config.LinkColumn("Acessar Loja")
        },
        num_rows="dynamic",
        hide_index=True,
        use_container_width=True
    )
    
    if st.button("Salvar Lojas 💾"):
        st.session_state.df_lojas = edited_lojas
        st.session_state.df_lojas.to_csv(LOJAS_FILE, index=False)
        st.success("Lista de Lojas atualizada!")

with tab3:
    st.subheader("👗 Shein Kids - Monitoramento de Looks")
    st.markdown("Área exclusiva para acompanhar as roupas de bebê da Shein!")
    
    edited_shein = st.data_editor(
        st.session_state.df_shein,
        column_config={
            "Look": st.column_config.TextColumn("Descrição da Roupa", width="medium"),
            "Comprado": st.column_config.CheckboxColumn("Comprado?", default=False),
            "Preço Estimado": st.column_config.TextColumn("Preço Estimado (R$)"),
            "Link Shein": st.column_config.LinkColumn("Link do Produto", display_text="Ver na Shein 🔗")
        },
        num_rows="dynamic",
        hide_index=True,
        use_container_width=True
    )
    
    if st.button("Salvar Looks da Shein 💾"):
        st.session_state.df_shein = edited_shein
        st.session_state.df_shein.to_csv(SHEIN_FILE, index=False)
        st.success("Looks atualizados com sucesso!")
