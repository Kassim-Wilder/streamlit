
import streamlit as st
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import requests
import plotly.express as px
from io import StringIO
import certifi

st.title('Hello Wilders, welcome to my  first application : DataFrame Cars')
# Lien vers le fichier CSV
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
# Télécharger le contenu du fichier CSV avec vérification SSL activée en utilisant le certificat CA racine fourni par Certifi
response = requests.get(link, verify=certifi.where())

# Lire le contenu CSV dans un DataFrame Pandas
if response.status_code == 200:
    df_cars = pd.read_csv(StringIO(response.text))
    #df_cars.year =  df_cars.year.replace(",", "")
else:
    st.error("Impossible de télécharger le fichier CSV")

# suppression de la virgule ans les dates
#df_cars.year = pd.to_numeric(df_cars.year.replace(",", ""))

# Trier dans l'ordre les dates de Cars
df_cars 

# Réindexer Cars
df_cars = df_cars.reset_index(drop = True)



st.write("A heatmap colors squares according to their values.")
st.write("Here, we'll calculate the correlation coefficients for all the variables, 2 by 2. Then display them as a heat map; this gives us the graph below")

# titre pour le  heatmap
st.title('Correlation Heatmap of Cars')

plt.figure(figsize=(20, 10))

# Création du heatmap en tenant compte que des valeurs numériques
viz_correlation = sns.heatmap(df_cars.corr(numeric_only = True), 
								center = 0, annot = True,
								cmap = sns.color_palette("icefire", as_cmap=True)
								)

# Affichage du graphe(heatmap)
st.pyplot(viz_correlation.figure)
st.write("“On the diagonal, the squares are all 1: this is logical, as mpg is 100% correlated with itself”")

# --------  2E FIGURE ----------
st.title('Distribution diagram: barplot')

#plott = px.lineplot(data_frame = df_cars, x = "year", y = "cylinders",   color = "continent",
                       #title = "Nombres de cylindres par années"
                   #)

plt.figure(figsize=(20, 10))                

plott = sns.barplot(data = df_cars,  x = "year", y = "cylinders",
            hue = "continent")
   
    


#st.update_layout(title_x = 0.5)
st.pyplot(plott.figure)

#st.pyplot(plott.figure)



## test_-----------------


# Créer un DataFrame exemple
import streamlit as st
import pandas as pd

# Créer un DataFrame exemple


# Titre de la page
st.title('Select and sub-select columns')
st.subheader('Here we can filter the dataset using the selction buttons on the left (Select column(s))' )

# Afficher le DataFrame
st.write('DataFrame original :')
st.write(df_cars)

# Liste des colonnes du DataFrame
colonnes = df_cars.columns.tolist()

# Sélectionner plusieurs colonnes à afficher
colonnes_selectionnees = st.sidebar.multiselect('Select column(s)', colonnes)

# Afficher la sous-sélection pour chaque colonne sélectionnée
resultats = df_cars.copy()  # Copie du DataFrame pour appliquer les filtres

for colonne in colonnes_selectionnees:
    st.subheader(f'Sub_select for {colonne}')
    if colonne:
        sous_selection = st.sidebar.selectbox(f'Sub_select for {colonne}', df_cars[colonne].unique())
        resultats = resultats[resultats[colonne] == sous_selection]  # Filtrer le DataFrame
    
    # Affiche le titre et la table filtrée
    st.write(f'Cars filtred by : {colonne}')
    st.write(resultats)
    
    # Afficher le nombre de lignes et de colonnes après le filtrage
    st.write(f'Number of lines : {resultats.shape[0]}')
    st.write(f'Number of columns : {resultats.shape[1]}')

    # Réinitialiser le DataFrame pour la prochaine colonne
    #resultats = df_cars.copy()
st.subheader('Thank you for your visit')
        
#streamlit run my_streamlit_app.py

