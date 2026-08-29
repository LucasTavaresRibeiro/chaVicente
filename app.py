import streamlit as st
import pandas as pd
import os

# Configuração da página
st.set_page_config(page_title="Enxoval do Vicente - Dattebayo!", page_icon="🦊", layout="wide")

# CSS para o tema do Naruto (Laranja e Azul)
st.markdown("""
<style>
    h1, h2, h3 {
        color: #ff7b00; /* Laranja Naruto */
        font-family: 'Arial Black', sans-serif;
    }
    .stButton>button {
        background-color: #004b87; /* Azul Escuro */
        color: white;
        border-radius: 8px;
        border: 2px solid #ff7b00;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #ff7b00;
        color: white;
        border: 2px solid #004b87;
    }
</style>
""", unsafe_allow_html=True)

st.title("🦊 Enxoval do Vicente - Missão Nível S 🍥")
st.markdown("Bem-vindos ao painel de controle do enxoval e chá de bebê do **Vicente**! Marquem os itens já garantidos e fiquem de olho nas promoções (Links de busca inclusos). *Dattebayo!*")

DATA_FILE = "enxoval.csv"

# Dados iniciais genéricos + links de busca para promoções
INITIAL_DATA = [
    {"Item": "Fralda Pampers RN", "Categoria": "Higiene", "Comprado": False, "Link Promoção/Busca": "https://www.drogasil.com.br/search?w=pampers+rn"},
    {"Item": "Fralda Pampers P", "Categoria": "Higiene", "Comprado": False, "Link Promoção/Busca": "https://lista.mercadolivre.com.br/fralda-pampers-premium-care-p"},
    {"Item": "Fralda Pampers M", "Categoria": "Higiene", "Comprado": False, "Link Promoção/Busca": "https://lista.mercadolivre.com.br/fralda-pampers-premium-care-m"},
    {"Item": "Fralda Pampers G", "Categoria": "Higiene", "Comprado": False, "Link Promoção/Busca": "https://lista.mercadolivre.com.br/fralda-pampers-premium-care-g"},
    {"Item": "Lenço Umedecido (Kit)", "Categoria": "Higiene", "Comprado": False, "Link Promoção/Busca": "https://www.amazon.com.br/s?k=len%C3%A7o+umedecido+bebe"},
    {"Item": "Pomada Assadura (Bepantol)", "Categoria": "Higiene", "Comprado": False, "Link Promoção/Busca": "https://www.amazon.com.br/s?k=bepantol+baby"},
    {"Item": "Kit Mamadeiras Avent", "Categoria": "Alimentação", "Comprado": False, "Link Promoção/Busca": "https://www.amazon.com.br/s?k=mamadeira+avent+petala"},
    {"Item": "Body Manga Curta (Kit 5)", "Categoria": "Roupas", "Comprado": False, "Link Promoção/Busca": "https://www.shopee.com.br/search?keyword=kit%20body%20bebe%20manga%20curta"},
    {"Item": "Body Manga Longa (Kit 5)", "Categoria": "Roupas", "Comprado": False, "Link Promoção/Busca": "https://www.shopee.com.br/search?keyword=kit%20body%20bebe%20manga%20longa"},
    {"Item": "Mijão / Culote (Kit)", "Categoria": "Roupas", "Comprado": False, "Link Promoção/Busca": "https://www.shopee.com.br/search?keyword=mijao%20bebe"},
    {"Item": "Toalha com Capuz", "Categoria": "Banho", "Comprado": False, "Link Promoção/Busca": "https://www.amazon.com.br/s?k=toalha+bebe+capuz"},
    {"Item": "Carrinho de Bebê", "Categoria": "Passeio", "Comprado": False, "Link Promoção/Busca": "https://www.amazon.com.br/s?k=carrinho+de+bebe"},
    {"Item": "Bebê Conforto", "Categoria": "Passeio", "Comprado": False, "Link Promoção/Busca": "https://www.amazon.com.br/s?k=bebe+conforto"},
]

def load_data():
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    else:
        df = pd.DataFrame(INITIAL_DATA)
        df.to_csv(DATA_FILE, index=False)
        return df

if 'df' not in st.session_state:
    st.session_state.df = load_data()

st.subheader("📜 Pergaminho de Itens (Lista de Enxoval)")

# Edição da tabela
edited_df = st.data_editor(
    st.session_state.df,
    column_config={
        "Item": st.column_config.TextColumn("Item", width="large"),
        "Comprado": st.column_config.CheckboxColumn(
            "Comprado?",
            help="Marque se você já garantiu esse item!",
            default=False,
        ),
        "Link Promoção/Busca": st.column_config.LinkColumn(
            "Link Ofertas / Pesquisa do Robô",
            help="Clique para buscar promoções deste item.",
            display_text="Buscar Ofertas 🛒"
        )
    },
    disabled=["Categoria"],
    hide_index=True,
    use_container_width=True
)

# Salvar alterações
if st.button("Salvar Alterações no Pergaminho 💾"):
    st.session_state.df = edited_df
    st.session_state.df.to_csv(DATA_FILE, index=False)
    st.success("Alterações salvas com sucesso! Jutsu de Salvamento concluído!")

st.divider()

st.subheader("➕ Adicionar Novo Item")
with st.form("add_item_form"):
    new_item = st.text_input("Nome do Item")
    new_cat = st.selectbox("Categoria", ["Higiene", "Roupas", "Alimentação", "Banho", "Quarto", "Passeio", "Outros"])
    submit_button = st.form_submit_button("Adicionar à Missão")

    if submit_button and new_item:
        # Gera link automático de busca no Google Shopping para o novo item
        search_query = new_item.replace(' ', '+')
        new_link = f"https://www.google.com/search?tbm=shop&q={search_query}"
        
        new_row = {"Item": new_item, "Categoria": new_cat, "Comprado": False, "Link Promoção/Busca": new_link}
        new_row_df = pd.DataFrame([new_row])
        st.session_state.df = pd.concat([st.session_state.df, new_row_df], ignore_index=True)
        st.session_state.df.to_csv(DATA_FILE, index=False)
        st.success(f"'{new_item}' adicionado! O robô gerou um link de busca automático para você.")
        st.rerun()

st.divider()
st.info("💡 **Aviso Ninja:** O app está configurado para salvar os dados em um arquivo local (`enxoval.csv`). Se você hospedar no **Streamlit Cloud**, o arquivo reiniciará se o app ficar inativo por muito tempo. Para resolver isso no futuro, me avise que ensino a usar o Google Sheets!")
