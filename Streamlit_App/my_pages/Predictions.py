import streamlit as st
import pandas as pd

def display():
    #====================Importation de la base
    df = pd.read_csv('Data/x_processed.csv')

    st.title("Prédiction du prix des maisons")

    with st.form(key='maison_form'):
        overall_qual = st.selectbox("Qualité générale", df['OverallQual'].unique())
        neighborhood = st.selectbox("Quartier", df['Neighborhood'].unique())
        garage_cars = st.number_input("Nombre de voitures dans le garage", min_value=0, max_value=5)
        bsmt_qual = st.selectbox("Qualité du sous-sol", df['BsmtQual'].unique())
        kitchen_qual = st.selectbox("Qualité de la cuisine", df['KitchenQual'].unique())
        exter_qual = st.selectbox("Qualité de l'extérieur", df['ExterQual'].unique())
        garage_area = st.number_input("Surface du garage (en pieds carrés)", min_value=0)
        full_bath = st.number_input("Nombre de salles de bain complètes", min_value=0, max_value=5)
        garage_finish = st.selectbox("Finition du garage", df['GarageFinish'].unique())
        dure_garage = st.number_input("Durée du garage", min_value=0)
        garage_type = st.selectbox("Type de garage", df['GarageType'].unique())
        foundation = st.selectbox("Fondation", df['Foundation'].unique())
        fireplace_qu = st.selectbox("Qualité de la cheminée", df['FireplaceQu'].unique())
        tot_rms_abv_grd = st.number_input("Total des pièces au-dessus du sol", min_value=0)
        ms_subclass = st.selectbox("Sous-classe MS", df['MSSubClass'].unique())
        dure_house = st.number_input("Durée de la maison", min_value=0)
        heating_qc = st.selectbox("Qualité du chauffage", df['HeatingQC'].unique())
        bsmt_fin_type1 = st.selectbox("Type de finition du sous-sol 1", df['BsmtFinType1'].unique())
        fireplaces = st.number_input("Nombre de cheminées", min_value=0)
        exterior1st = st.selectbox("Premier matériau extérieur", df['Exterior1st'].unique())
        exterior2nd = st.selectbox("Deuxième matériau extérieur", df['Exterior2nd'].unique())
        mas_vnr_type = st.selectbox("Type de revêtement", df['MasVnrType'].unique())
        gr_liv_area = st.number_input("Surface habitable (en pieds carrés)", min_value=0)
        ms_zoning = st.selectbox("Zonage MS", df['MSZoning'].unique())
        overall_cond = st.selectbox("Condition générale", df['OverallCond'].unique())
        house_style = st.selectbox("Style de la maison", df['HouseStyle'].unique())
        bsmt_exposure = st.selectbox("Exposition du sous-sol", df['BsmtExposure'].unique())
        sale_condition = st.selectbox("Condition de vente", df['SaleCondition'].unique())
        sale_type = st.selectbox("Type de vente", df['SaleType'].unique())
        garage_cond = st.selectbox("Condition du garage", df['GarageCond'].unique())
        second_flr_sf = st.number_input("Surface du deuxième étage (en pieds carrés)", min_value=0)
        total_bsmt_sf = st.number_input("Surface totale du sous-sol (en pieds carrés)", min_value=0)
        lot_shape = st.selectbox("Forme du terrain", df['LotShape'].unique())
        garage_qual = st.selectbox("Qualité du garage", df['GarageQual'].unique())
        central_air = st.selectbox("Climatisation centrale", df['CentralAir'].unique())
        half_bath = st.number_input("Nombre de salles de bain à moitié", min_value=0, max_value=5)
        lot_frontage = st.number_input("Front de lot (en pieds)", min_value=0)
        fence = st.selectbox("Clôture", df['Fence'].unique())
        electric = st.selectbox("Électricité", df['Electric'].unique())
        open_porch_sf = st.number_input("Surface du porche ouvert (en pieds carrés)", min_value=0)
        electrical = st.selectbox("Électrique", df['Electrical'].unique())

        submit_button = st.form_submit_button(label='Prédire le prix')

    if submit_button:
        user_input = {
            'OverallQual': overall_qual,
            'Neighborhood': neighborhood,
            'GarageCars': garage_cars,
            'BsmtQual': bsmt_qual,
            'KitchenQual': kitchen_qual,
            'ExterQual': exter_qual,
            'GarageArea': garage_area,
            'FullBath': full_bath,
            'GarageFinish': garage_finish,
            'Dure_garage': dure_garage,
            'GarageType': garage_type,
            'Foundation': foundation,
            'FireplaceQu': fireplace_qu,
            'TotRmsAbvGrd': tot_rms_abv_grd,
            'MSSubClass': ms_subclass,
            'Dure_house': dure_house,
            'HeatingQC': heating_qc,
            'BsmtFinType1': bsmt_fin_type1,
            'Fireplaces': fireplaces,
            'Exterior1st': exterior1st,
            'Exterior2nd': exterior2nd,
            'MasVnrType': mas_vnr_type,
            'GrLivArea': gr_liv_area,
            'MSZoning': ms_zoning,
            'OverallCond': overall_cond,
            'HouseStyle': house_style,
            'BsmtExposure': bsmt_exposure,
            'SaleCondition': sale_condition,
            'SaleType': sale_type,
            'GarageCond': garage_cond,
            '2ndFlrSF': second_flr_sf,
            'TotalBsmtSF': total_bsmt_sf,
            'LotShape': lot_shape,
            'GarageQual': garage_qual,
            'CentralAir': central_air,
            'HalfBath': half_bath,
            'LotFrontage': lot_frontage,
            'Fence': fence,
            'Electric': electric,
            'OpenPorchSF': open_porch_sf,
            'Electrical': electrical,
        }

        input_df = pd.DataFrame([user_input])

        st.write("Caractéristiques de la maison saisies :")
        st.write(input_df)

        # Ici, vous pouvez ajouter le code pour faire la prédiction avec votre modèle
        # par exemple : prediction = model.predict(input_df)
        # st.write(f"Le prix prédit de la maison est : {prediction[0]}")