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
# Dados Iniciais - Lista Completa de Enxoval e Links Revisados 100%
INITIAL_DATA = [
    # --- HIGIENE ---
    {"Item": "Fralda Pampers Premium Care RN", "Categoria": "Higiene", "Comprado": False, "Preço Médio": "R$ 60,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=Fralda+Pampers+Premium+Care+RN", 
     "Busca 2 (Específica)": "https://www.drogasil.com.br/search?w=pampers+premium+care+rn", 
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=fralda+pampers+premium+care+rn"},
    
    {"Item": "Fralda Pampers Premium Care P", "Categoria": "Higiene", "Comprado": False, "Preço Médio": "R$ 75,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=Fralda+Pampers+Premium+Care+P", 
     "Busca 2 (Específica)": "https://www.drogasil.com.br/search?w=pampers+premium+care+p", 
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=fralda+pampers+premium+care+p"},
    
    {"Item": "Lenço Umedecido Huggies (Kit Leve Mais)", "Categoria": "Higiene", "Comprado": False, "Preço Médio": "R$ 45,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=Lenco+Umedecido+Huggies+Recem+Nascido", 
     "Busca 2 (Específica)": "https://www.drogaraia.com.br/search?w=lenco+umedecido+huggies", 
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=lenco+umedecido+huggies"},
     
    {"Item": "Pomada Antiassaduras Bepantol Baby", "Categoria": "Higiene", "Comprado": False, "Preço Médio": "R$ 40,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=bepantol+baby+pomada", 
     "Busca 2 (Específica)": "https://www.drogasil.com.br/search?w=bepantol+baby", 
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=bepantol+baby"},
     
    {"Item": "Sabonete Líquido Granado Bebê", "Categoria": "Higiene", "Comprado": False, "Preço Médio": "R$ 25,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=sabonete+liquido+granado+bebe", 
     "Busca 2 (Específica)": "https://www.drogasil.com.br/search?w=sabonete+granado+bebe", 
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=sabonete+granado+bebe"},
     
    {"Item": "Kit Cortador e Lixa de Unha Bebê", "Categoria": "Higiene", "Comprado": False, "Preço Médio": "R$ 35,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=kit+unha+bebe+tesoura", 
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=kit+unha+bebe", 
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/kit-unha-bebe"},

    # --- ROUPAS ---
    {"Item": "Body Manga Curta Carter's (Kit)", "Categoria": "Roupas", "Comprado": False, "Preço Médio": "R$ 130,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=kit+body+manga+curta+carters", 
     "Busca 2 (Específica)": "https://www.riachuelo.com.br/busca?q=kit%20body%20carter%27s", 
     "Busca 3 (Alternativa)": "https://www.dafiti.com.br/catalog/?q=kit+body+carters"},
    
    {"Item": "Body Manga Longa Básico", "Categoria": "Roupas", "Comprado": False, "Preço Médio": "R$ 70,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=kit+body+manga+longa+bebe", 
     "Busca 2 (Específica)": "https://www.renner.com.br/b?q=kit+body+manga+longa", 
     "Busca 3 (Alternativa)": "https://www.cea.com.br/busca?q=body%20manga%20longa%20bebe"},
    
    {"Item": "Macacão Suedine (Zíper ou Botão)", "Categoria": "Roupas", "Comprado": False, "Preço Médio": "R$ 60,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=macacao+bebe+suedine+ziper", 
     "Busca 2 (Específica)": "https://www.renner.com.br/b?q=macacao+bebe", 
     "Busca 3 (Alternativa)": "https://www.dafiti.com.br/catalog/?q=macacao+bebe"},
     
    {"Item": "Kit Mijão/Culote", "Categoria": "Roupas", "Comprado": False, "Preço Médio": "R$ 50,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=kit+mijao+bebe+culote", 
     "Busca 2 (Específica)": "https://www.renner.com.br/b?q=mijao+bebe", 
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=kit+mijao+bebe"},
     
    {"Item": "Kit Meias para Recém-Nascido", "Categoria": "Roupas", "Comprado": False, "Preço Médio": "R$ 30,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=kit+meia+recem+nascido", 
     "Busca 2 (Específica)": "https://www.renner.com.br/b?q=meia+bebe", 
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=meia+bebe"},

    # --- PASSEIO / QUARTO ---
    {"Item": "Carrinho de Bebê c/ Bebê Conforto", "Categoria": "Passeio", "Comprado": False, "Preço Médio": "R$ 900,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=carrinho+de+bebe+com+bebe+conforto", 
     "Busca 2 (Específica)": "https://www.magazineluiza.com.br/busca/carrinho+bebe+conforto/", 
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=carrinho+de+bebe+travel+system"},
     
    {"Item": "Babá Eletrônica com Câmera", "Categoria": "Quarto", "Comprado": False, "Preço Médio": "R$ 300,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=baba+eletronica+com+camera", 
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=baba+eletronica+camera", 
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/baba-eletronica-camera"},
     
    {"Item": "Kit Berço (Lençol e Fronha)", "Categoria": "Quarto", "Comprado": False, "Preço Médio": "R$ 150,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=kit+berco+algodao", 
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=kit+berco", 
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/kit-berco"},

    # --- ALIMENTAÇÃO ---
    {"Item": "Kit Mamadeiras Philips Avent Pétala", "Categoria": "Alimentação", "Comprado": False, "Preço Médio": "R$ 160,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=kit+mamadeiras+avent+petala", 
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=mamadeira+avent+petala", 
     "Busca 3 (Alternativa)": "https://www.drogasil.com.br/search?w=mamadeira+avent"},
     
    {"Item": "Escova para Lavar Mamadeira", "Categoria": "Alimentação", "Comprado": False, "Preço Médio": "R$ 25,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=escova+lavar+mamadeira", 
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=escova+mamadeira", 
     "Busca 3 (Alternativa)": "https://www.drogasil.com.br/search?w=escova+mamadeira"},

    # --- MAMÃE BRUNA ---
    {"Item": "Absorvente Pós-Parto", "Categoria": "MamãeBruna", "Comprado": False, "Preço Médio": "R$ 22,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=absorvente+pos-parto", 
     "Busca 2 (Específica)": "https://www.drogasil.com.br/search?w=absorvente+pos+parto", 
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=absorvente+pos+parto"},
    
    {"Item": "Bomba Tira Leite Elétrica", "Categoria": "MamãeBruna", "Comprado": False, "Preço Médio": "R$ 180,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=bomba+tira+leite+eletrica", 
     "Busca 2 (Específica)": "https://www.amazon.com.br/s?k=bomba+tira+leite+eletrica", 
     "Busca 3 (Alternativa)": "https://lista.mercadolivre.com.br/bomba-tira-leite-eletrica"},
     
    {"Item": "Pomada de Lanolina (Fissuras Mamilo)", "Categoria": "MamãeBruna", "Comprado": False, "Preço Médio": "R$ 60,00",
     "Busca 1 (Google)": "https://www.google.com/search?tbm=shop&q=pomada+lanolina+lansinoh", 
     "Busca 2 (Específica)": "https://www.drogasil.com.br/search?w=lanolina", 
     "Busca 3 (Alternativa)": "https://www.amazon.com.br/s?k=lanolina"},
]

INITIAL_LOJAS = [
    {"Loja": "Amazon - Categoria Bebês", "Link": "https://www.amazon.com.br/s?i=baby", "Monitorar": True},
    {"Loja": "Drogasil - Infantil", "Link": "https://www.drogasil.com.br/infantil.html", "Monitorar": True},
    {"Loja": "Riachuelo - Carter's", "Link": "https://www.riachuelo.com.br/infantil/bebes/carters", "Monitorar": True}
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
