import streamlit as st
import pandas as pd
import os

# Configuração da página
st.set_page_config(page_title="Enxoval do Vicente - Dattebayo!", page_icon="🦊", layout="wide")

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
st.markdown("Bem-vindos ao painel de controle do enxoval e chá de bebê do **Vicente** e da **Mamãe Bruna**! *Dattebayo!*")

DATA_FILE = "enxoval.csv"
LOJAS_FILE = "lojas.csv"

# Dados iniciais
INITIAL_DATA = [
    {"Item": "Fralda Pampers RN", "Categoria": "Higiene", "Comprado": False, "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=fralda+pampers+rn", "Busca 2 (Específica)": "https://www.drogasil.com.br/search?w=pampers+rn", "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=fralda+pampers+rn"},
    {"Item": "Lenço Umedecido", "Categoria": "Higiene", "Comprado": False, "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=lenco+umedecido+bebe", "Busca 2 (Específica)": "https://www.drogasil.com.br/search?w=lenco+umedecido", "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=lenco+umedecido"},
    {"Item": "Body Manga Curta (Kit)", "Categoria": "Roupas", "Comprado": False, "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=kit+body+bebe+manga+curta", "Busca 2 (Específica)": "https://www.renner.com.br/b?q=kit%20body%20bebe", "Busca 3 (Alternativa)": "https://www.cea.com.br/busca?q=body%20bebe"},
    {"Item": "Macacão Bebê", "Categoria": "Roupas", "Comprado": False, "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=macacao+bebe", "Busca 2 (Específica)": "https://www.riachuelo.com.br/busca?q=macacao%20bebe", "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=macacao+bebe"},
    {"Item": "Absorvente Pós-Parto", "Categoria": "MamãeBruna", "Comprado": False, "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=absorvente+pos+parto", "Busca 2 (Específica)": "https://www.drogasil.com.br/search?w=absorvente+pos+parto", "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=absorvente+pos+parto"},
    {"Item": "Bomba Tira Leite", "Categoria": "MamãeBruna", "Comprado": False, "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=bomba+tira+leite", "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=bomba+tira+leite", "Busca 3 (Alternativa)": "https://www.magazineluiza.com.br/busca/bomba+tira+leite/"},
    {"Item": "Carrinho de Bebê", "Categoria": "Passeio", "Comprado": False, "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=carrinho+de+bebe", "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=carrinho+de+bebe", "Busca 3 (Alternativa)": "https://www.magazineluiza.com.br/busca/carrinho+de+bebe/"},
]

INITIAL_LOJAS = [
    {"Loja": "Amazon - Loja do Bebê", "Link": "https://www.amazon.com.br/b?node=16245642011", "Monitorar": True}
]

def load_data(file_path, default_data):
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        df = pd.DataFrame(default_data)
        df.to_csv(file_path, index=False)
        return df

if 'df' not in st.session_state:
    st.session_state.df = load_data(DATA_FILE, INITIAL_DATA)

if 'df_lojas' not in st.session_state:
    st.session_state.df_lojas = load_data(LOJAS_FILE, INITIAL_LOJAS)

tab1, tab2 = st.tabs(["📜 Pergaminho de Itens", "🏬 Lojas Monitoradas"])

with tab1:
    st.subheader("Lista de Enxoval")
    
    edited_df = st.data_editor(
        st.session_state.df,
        column_config={
            "Item": st.column_config.TextColumn("Item", width="medium"),
            "Comprado": st.column_config.CheckboxColumn("Comprado?", default=False),
            "Busca 1 (Google)": st.column_config.LinkColumn("Google Shopping", display_text="Google 🛒"),
            "Busca 2 (Específica)": st.column_config.LinkColumn("Loja 1", display_text="Loja 🛒"),
            "Busca 3 (Alternativa)": st.column_config.LinkColumn("Loja 2", display_text="Alternativa 🛒")
        },
        hide_index=True,
        use_container_width=True
    )

    if st.button("Salvar Alterações no Pergaminho 💾"):
        st.session_state.df = edited_df
        st.session_state.df.to_csv(DATA_FILE, index=False)
        st.success("Alterações salvas com sucesso!")

    st.divider()

    st.subheader("➕ Adicionar Novo Item")
    with st.form("add_item_form"):
        new_item = st.text_input("Nome do Item")
        
        # Categorias existentes + MamãeBruna
        categorias_existentes = list(st.session_state.df['Categoria'].unique())
        if "MamãeBruna" not in categorias_existentes:
            categorias_existentes.append("MamãeBruna")
            
        cat_opcao = st.selectbox("Categoria", categorias_existentes + ["-- Criar Nova Categoria --"])
        nova_categoria_manual = st.text_input("Se escolheu criar nova, digite o nome da categoria:")
        
        submit_button = st.form_submit_button("Adicionar à Missão")

        if submit_button and new_item:
            cat_final = nova_categoria_manual if cat_opcao == "-- Criar Nova Categoria --" and nova_categoria_manual else cat_opcao
            if cat_opcao == "-- Criar Nova Categoria --" and not nova_categoria_manual:
                st.error("Por favor, digite o nome da nova categoria.")
            else:
                search_query = new_item.replace(' ', '+')
                link1 = f"https://www.google.com/search?tbm=shop&q={search_query}"
                
                # Regra de Roupas
                if cat_final == "Roupas":
                    link2 = f"https://www.renner.com.br/b?q={search_query}"
                    link3 = f"https://www.amazon.com.br/s?k={search_query}"
                elif cat_final == "Higiene" or cat_final == "MamãeBruna":
                    link2 = f"https://www.drogasil.com.br/search?w={search_query}"
                    link3 = f"https://www.amazon.com.br/s?k={search_query}"
                else:
                    link2 = f"https://www.amazon.com.br/s?k={search_query}"
                    link3 = f"https://www.magazineluiza.com.br/busca/{search_query}/"
                
                new_row = {"Item": new_item, "Categoria": cat_final, "Comprado": False, 
                           "Busca 1 (Google)": link1, "Busca 2 (Específica)": link2, "Busca 3 (Alternativa)": link3}
                
                st.session_state.df = pd.concat([st.session_state.df, pd.DataFrame([new_row])], ignore_index=True)
                st.session_state.df.to_csv(DATA_FILE, index=False)
                st.success(f"'{new_item}' adicionado!")
                st.rerun()

with tab2:
    st.subheader("Lojas Aliadas (Monitoramento)")
    st.markdown("Adicione os links das suas lojas favoritas. O nosso robô (e o futuro bot do Telegram) usarão essas lojas como base principal de monitoramento!")
    
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

st.divider()
st.info("💡 **Dica ninja:** Mande uma imagem pro chat para eu colocar como papel de parede deste painel!")
