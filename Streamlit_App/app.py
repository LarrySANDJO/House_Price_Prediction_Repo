import streamlit as st
from streamlit_option_menu import option_menu
from my_pages import accueil, Predictions

#--------------------------------------------  l'en-tête commun
st.set_page_config(
    page_title="House Price Prediction",
      page_icon="🏬", 
      layout="wide",
    initial_sidebar_state = "expanded"
)
#-------------------------------------------- chargement css

# Chargement du css personnalise (modifications des classe et id par defaut de streamlit)

st.markdown("""
<style>

/* Variables globales */
:root {
    --House-blue: #25227A;
    --House-blue-dark: #061545;
    --House-blue-light: #649EFB;
    --background-light: #E8E8E8;
    --shadow-sm: 0 2px 4px rgba(0,0,0,0.1);
    --shadow-md: 0 4px 6px rgba(0,0,0,0.1);
    --border-radius: 8px;
}



.main {
    padding: 1.5rem;
}

/* Sidebar */
.sidebar .sidebar-content {
    background-color: white;
    padding: 1rem;
}

.sidebar-logo {
    padding: 1rem;
    margin-bottom: 2rem;
}

.sidebar-logo img {
    border-radius: var(--border-radius);
    box-shadow: var(--shadow-sm);
    transition: transform 0.3s ease;
}

.sidebar-logo img:hover {
    transform: scale(1.02);
}

.sidebar-logo .caption {
    text-align: center;
    margin-top: 0.5rem;
    color: var(--House-blue);
    font-weight: 500;
}

/* Header */
.dashboard-header {
    background-color:var(--House-blue);
    color: white;
    padding: 1.5rem;
    border-radius: var(--border-radius);
    margin-bottom: 2rem;
    box-shadow: var(--shadow-md);
}

.dashboard-header h1 {
    text-align: center;
    font-size: 3rem;
    color: white;
    font-weight: 600;
    margin: 0;
    text-transform: uppercase;
}

.dashboard-header h2 {
    text-align: center;
    font-size: 2rem;
    color: white;
    font-weight: 600;
    margin: 0;
    text-transform: uppercase;
}

.dashboard-header h3 {
    text-align: center;
    font-size: 1.5rem;
    color: white;
    font-weight: 600;
    margin: 0;
    text-transform: uppercase;
}

/* Menu de navigation */
#MainMenu {
    background-color: white;
    border-radius: var(--border-radius);
    padding: 0.5rem;
    margin-bottom: 2rem;
    box-shadow: var(--shadow-sm);
}

.nav-link {
    color: var(--House-blue) !important;
    transition: all 0.3s ease;
    border-radius: var(--border-radius);
    margin: 0.2rem;
}

.nav-link:hover {
    background-color: var(--House-blue-light) !important;
    transform: translateY(-1px);
}

.nav-link.active {
    background-color:#e63946;
    color: white !important;
    box-shadow: var(--shadow-sm);
}

.nav-link .icon {
    margin-right: 0.5rem;
}

/* Cards */
.custom-card {
    background: white;
    border-radius: var(--border-radius);
    box-shadow: var(--shadow-sm);
    padding: 1.5rem;
    margin-bottom: 1.5rem;
    transition: transform 0.3s ease;
}

.custom-card:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-md);
}

.card-title {
    color: var(--House-blue);
    font-size: 1.2rem;
    font-weight: 600;
    margin-bottom: 1rem;
}

/* Boutons */
.stButton > button {
    background-color: var(--House-blue);
    color: white;
    border: none;
    padding: 0.5rem 1.5rem;
    border-radius: var(--border-radius);
    font-weight: 500;
    transition: all 0.3s ease;
}

.stButton > button:hover {
    background-color: var(--House-blue-dark);
    transform: translateY(-1px);
    box-shadow: var(--shadow-sm);
}

/* Widgets Streamlit */
.stSelectbox, .stTextInput, .stDateInput {
    background-color: white;
    border-radius: var(--border-radius);
    padding: 0.5rem;
    margin-bottom: 1rem;
}

/* Tables */
.dataframe {
    border: none !important;
    box-shadow: var(--shadow-sm);
    border-radius: var(--border-radius);
}

.dataframe th {
    background-color: var(--House-blue) !important;
    color: white !important;
}

.dataframe tr:hover {
    background-color: var(--House-blue-light) !important;
}

/* Footer */
.footer {
    background-color: white;
    padding: 1.5rem;
    margin-top: 2rem;
    border-radius: var(--border-radius) var(--border-radius) 0 0;
    box-shadow: var(--shadow-sm);
    text-align: center;
}

/* Animations */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

.animate-fade-in {
    animation: fadeIn 0.5s ease forwards;
}
/* marche pas ! */
.nav-item{
    background-color:#e63946;


}
.stSidebar{
    background-color:#E8E8E8;
}

            


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

/* Pied de page */
.footer {
    background-color: white;
    padding: 1.5rem;
    margin-top: 2rem;
    border-radius: var(--border-radius) var(--border-radius) 0 0;
    box-shadow: var(--shadow-sm);
    text-align: center;
}

/* Animations */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}
.animate-fade-in {
    animation: fadeIn 0.5s ease forwards;
}
</style>
""", unsafe_allow_html=True)


#-------------------------------------------- Le sliderbar commun


with st.sidebar:
    st.markdown('<div class="sidebar-logo">', unsafe_allow_html=True)
    st.image("images/LaplaceIMMO.png",
             caption="HOUSE PRICE PREDICTION",
             )
    st.markdown('</div>', unsafe_allow_html=True)

def display_header():
    st.markdown("""
        <div class="dashboard-header animate-fade-in">
            <h1 style = "font-weight: bold;">DASHBOARD POUR LA PREDICTION DES PRIX DES APPARTEMENTS</h1>
        </div>
    """, unsafe_allow_html=True)

#--------------------------------------------Affichage de l'en-tête 

display_header()

#-------------------------------------------- menu navigation

page = option_menu( # voir help du package streamlit_option_menu
    menu_title=None,
    options=["Accueil", "Predictions"], #, "Produits",  "Visualisations", "Evolution"],
    icons=["house-fill", "tags-fill"], #, "tags-fill", "diagram-2-fill", "cart-fill", "graph-up-arrow"],
    menu_icon=None,
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important"},
        "icon": {"font-size": "1.3rem"},
        "nav-link": {"font-size": "1.2em", "text-align": "center", "margin": "0px"},
        "nav-link-selected": {"background-color": "#061545"},
    }
)

st.write("\n")

#--------------------------------------------Photo de HPP
st.markdown("---")

st.image("images/picture5.png", width=2000)

#--------------------------------------------action sur les pages
 
if page == "Predictions":
    Predictions.display()
else:
    accueil.display()


#-------------------------------------------- Pied de page

st.markdown("""
    <div class="footer">
        <p>ENSAE 2024/2025- Projet Machine Learning<br>
            - Lesline
            - Anna
            - Yamine
            - Larry
            </p>
            <img src="https://ensai.fr/wp-content/uploads/2019/07/ENSAE-Dakar-logo.png" alt="Image du produit" style="width:5%; height:auto; border-radius: 8px;">
    </div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)