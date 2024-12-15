
import streamlit as st
import pandas as pd
import plotly.express as px

def display():

#-------------------------------------------- Chargement des donnes
    df = pd.read_csv("Data/train.csv")
        
#-------------------------------------------- Chargement du css pour les textes
    st.markdown("""
    <style>
    /* Conteneurs personnalisés */
    [data-testid="metric-container"] {
        box-shadow: 0 0 4px #686664;
        padding: 10px;
    }

    .plot-container > div {
        box-shadow: 0 0 2px #070505;
        padding: 5px;
        border-color: #000000;
    }

    /* Expander */
    div[data-testid="stExpander"] div[role="button"] p {
        font-size: 1.2rem;
        color: rgb(0, 0, 0);
        border-color: #000000;
    }

    /* Barre latérale */
    .sidebar-content, [data-testid="stSidebar"] {
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)


#-------------------------------------------- Texte perso du siderbar
    st.sidebar.markdown("""
        <div class="dashboard-header animate-fade-in">
            <h2 style = "text-align: center;font-weight: bold;">Page d'accueil</h2>
        </div>
    """, unsafe_allow_html=True)

#-------------------------------------------- Affichage des donnes clef:Total produit,...
    mean_price = df["SalePrice"].mean()
    median_price = df["SalePrice"].median()
    price_variance = df["SalePrice"].var()
    max_price = df["SalePrice"].max()
    min_price = df["SalePrice"].min()

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.info('Moyenne des prix',icon="📌")
        display_custom_metric("Moyenne des prix", int(mean_price), "#0000FF")
    with col2:
        st.info('Médiane des prix',icon="📌")
        display_custom_metric("Médiane des prix", int(median_price), "#228B22")
    with col3:
        st.info('Variance des prix',icon="📌")
        display_custom_metric("Variance des prix", int(price_variance), "#FF0000")
    with col4:
        st.info('Prix maximal',icon="📌")
        display_custom_metric("Prix maximal", int(max_price), "#FE9900")
    with col5:
        st.info('Prix minimal',icon="📌")
        display_custom_metric("Prix minimal", int(min_price), "#582698")


    st.markdown("---")
    
    
#----------------------------------------------- Graphique croise avec les 10 variables qui infuencent le plus 

    Best_quanti = ["GarageCars","YearBuilt","FullBath","GarageArea"]
    
    Best_quali = ["OverallQual","Neighborhood","ExterQual","BsmtQual","KitchenQual","Alley","GarageFinish"]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
            <div class="dashboard-header animate-fade-in">
                <h3 style = "text-align: center;font-weight: bold;">Graphique croise avec les variables quantitatives</h3>
            </div>
        """, unsafe_allow_html=True)
        
        st.selectbox("Selectionnez une variable", options = Best_quanti, key = "key_quanti")
        
        if st.session_state['key_quanti']:
            fig = px.scatter(df, x = "{st.session_state['key_quanti']}", y='SalePrice', title=f"Graphique de {st.session_state['key_quanti']} vs SalePrice",
                            labels={st.session_state['key_quanti']: st.session_state['key_quanti'], 'SalePrice': 'SalePrice'})

            st.plotly_chart(fig)
    
    
    

#--------------------------------------------Affichage des produits en rupture de stock par categorie

    out_of_stock_data = st.session_state["df"][st.session_state["df"]["is_out_of_stock"] == True]

    if not out_of_stock_data.empty:
        fig2 = px.pie(
            out_of_stock_data,
            names="category",      
            title="Produits en rupture de stock par catégorie",
            hole=0.3               
        )
        
        fig2.update_traces(textinfo="label+value", textfont_size=10) 
        fig2.update_layout(title_font_size=24, legend_font_size=16)
        
        with col2: 
            st.plotly_chart(fig2, use_container_width=True)

    else:
        with col2: 
            st.info("Aucun produit en rupture de stock.")

    # Fin de la page d'acceuil