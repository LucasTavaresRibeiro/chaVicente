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
        background-color: rgba(18, 18, 18, 0.85); /* Fundo escuro com 85% de opacidade */
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.5);
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

# Dados Iniciais - Com Links Revisados e Preço Médio
INITIAL_DATA = [
    {"Item": "Fralda Pampers Premium Care RN", "Categoria": "Higiene", "Comprado": False, "Preço Médio": "R$ 60,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=Fralda+Pampers+Premium+Care+RN", 
     "Busca 2 (Específica)": "https://www.drogasil.com.br/pampers-fralda-premium-care-recem-nascido-36-unidades.html", 
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/fralda-pampers-premium-care-rn"},
    
    {"Item": "Lenço Umedecido Huggies RN (Kit 4)", "Categoria": "Higiene", "Comprado": False, "Preço Médio": "R$ 45,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=Lenco+Umedecido+Huggies+RN", 
     "Busca 2 (Específica)": "https://www.drogaraia.com.br/huggies-primeiros-100-dias-lenco-umedecido-recem-nascido-48-unidades.html", 
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/Len%C3%A7os-Umedecidos-Rec%C3%A9m-Nascido-Huggies-unidades/dp/B07Z49V4T1"},
    
    {"Item": "Body Manga Curta (Kit 5 - Carter's)", "Categoria": "Roupas", "Comprado": False, "Preço Médio": "R$ 130,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=kit+body+bebe+manga+curta+carters", 
     "Busca 2 (Específica)": "https://www.riachuelo.com.br/busca?q=kit%20body%20carter%27s", 
     "Busca 3 (Alternativa)": "https://www.dafiti.com.br/catalog/?q=kit+body+carters"},
    
    {"Item": "Macacão Bebê Algodão", "Categoria": "Roupas", "Comprado": False, "Preço Médio": "R$ 60,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=macacao+bebe+algodao+suedine", 
     "Busca 2 (Específica)": "https://www.renner.com.br/b/infantil/bebes/macacao-e-macaquinho", 
     "Busca 3 (Alternativa)": "https://www.cea.com.br/busca?q=macacao%20bebe"},
    
    {"Item": "Absorvente Pós-Parto Plenitud", "Categoria": "MamãeBruna", "Comprado": False, "Preço Médio": "R$ 22,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=Absorvente+Pos-Parto+Plenitud", 
     "Busca 2 (Específica)": "https://www.drogasil.com.br/plenitud-femme-absorvente-pos-parto-8-unidades.html", 
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/Absorvente-P%C3%B3s-Parto-Plenitud-Femme-Unidades/dp/B07Q5W5R5W"},
    
    {"Item": "Bomba Tira Leite Elétrica G-Tech Smart", "Categoria": "MamãeBruna", "Comprado": False, "Preço Médio": "R$ 180,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=Bomba+Tira+Leite+Eletrica+G-Tech+Smart", 
     "Busca 2 (Específica)": "https://www.drogaraia.com.br/bomba-tira-leite-materno-eletrica-g-tech-smart.html", 
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/bomba-tira-leite-eletrica-g-tech-smart"},
    
    {"Item": "Carrinho de Bebê Burigotto", "Categoria": "Passeio", "Comprado": False, "Preço Médio": "R$ 750,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=Carrinho+de+Bebe+Burigotto", 
     "Busca 2 (Específica)": "https://www.magazineluiza.com.br/busca/carrinho+de+bebe+burigotto/", 
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/Carrinho-Beb%C3%AA-Burigotto-Ecce-Preto/dp/B08V5QZXYQ"},
]

INITIAL_LOJAS = [
    {"Loja": "Amazon - Loja do Bebê", "Link": "https://www.amazon.com.br/b?node=16245642011", "Monitorar": True}
]

SHEIN_FILE = "shein.csv"
INITIAL_SHEIN = [
    {"Look": "Conjunto Moletom Infantil", "Preço Estimado": "R$ 45,00", "Link Shein": "https://br.shein.com/Kids-Clothing-c-2053.html", "Comprado": False}
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

if 'df_shein' not in st.session_state:
    st.session_state.df_shein = load_data(SHEIN_FILE, INITIAL_SHEIN)

tab1, tab2, tab3 = st.tabs(["📜 Pergaminho de Itens", "🏬 Lojas Monitoradas", "👗 Shein Kids"])

with tab1:
    st.subheader("Lista de Enxoval")
    
    edited_df = st.data_editor(
        st.session_state.df,
        column_config={
            "Item": st.column_config.TextColumn("Item", width="medium"),
            "Comprado": st.column_config.CheckboxColumn("Comprado?", default=False),
            "Preço Médio": st.column_config.TextColumn("Preço Médio", help="Preço base pesquisado pelo robô"),
            "Busca 1 (Google)": st.column_config.LinkColumn("Google Shopping", display_text="Google 🛒"),
            "Busca 2 (Específica)": st.column_config.LinkColumn("Loja Direta", display_text="Loja 🛒"),
            "Busca 3 (Alternativa)": st.column_config.LinkColumn("Alternativa", display_text="Alternativa 🛒")
        },
        hide_index=True,
        use_container_width=True
    )

    if st.button("Salvar Alterações no Pergaminho 💾"):
        st.session_state.df = edited_df
        st.session_state.df.to_csv(DATA_FILE, index=False)
        st.success("Alterações salvas com sucesso!")

    st.divider()

    st.subheader("➕ Adicionar Novo Item (O Robô vai buscar os links)")
    with st.form("add_item_form"):
        new_item = st.text_input("Nome do Item")
        preco_medio_manual = st.text_input("Preço Médio (Ex: R$ 50,00)", value="R$ ")
        
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
                
                if cat_final == "Roupas":
                    link2 = f"https://www.renner.com.br/b?q={search_query}"
                    link3 = f"https://www.dafiti.com.br/catalog/?q={search_query}"
                elif cat_final == "Higiene" or cat_final == "MamãeBruna":
                    link2 = f"https://www.drogasil.com.br/search?w={search_query}"
                    link3 = f"https://lista.mercadolivre.com.br/{search_query}"
                else:
                    link2 = f"https://www.amazon.com.br/s?k={search_query}"
                    link3 = f"https://www.magazineluiza.com.br/busca/{search_query}/"
                
                new_row = {"Item": new_item, "Categoria": cat_final, "Comprado": False, "Preço Médio": preco_medio_manual,
                           "Busca 1 (Google)": link1, "Busca 2 (Específica)": link2, "Busca 3 (Alternativa)": link3}
                
                st.session_state.df = pd.concat([st.session_state.df, pd.DataFrame([new_row])], ignore_index=True)
                st.session_state.df.to_csv(DATA_FILE, index=False)
                st.success(f"'{new_item}' adicionado!")
                st.rerun()

with tab2:
    st.subheader("Lojas Aliadas (Monitoramento)")
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
