import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Titre de l'application
st.title("Calculateur de Contributions et de Prêt")

# Saisie des données via l'interface Streamlit
total_cost = st.number_input("Coût total du projet en dirhams", value=31_000_000)
population_totale = st.number_input("Nombre total de la population cible", value=4305)
nombre_menages = st.number_input("Nombre de ménages", value=861)

# Saisie des contributions en pourcentage
contribution_etat_pct = st.slider("Pourcentage de la subvention publique", min_value=0.0, max_value=1.0, value=0.3)
contribution_partenariats_pct = st.slider("Pourcentage de l'investissement privé", min_value=0.0, max_value=1.0, value=0.2)
contribution_menages_pct = st.slider("Pourcentage de la contribution de la population", min_value=0.0, max_value=1.0, value=0.4)

# Paramètres du prêt
taux_interet_annuel = st.number_input("Taux d'intérêt annuel (en fraction)", value=0.02)
duree_remboursement = st.number_input("Durée de remboursement en années", value=15)

# Calcul des contributions
contribution_etat = contribution_etat_pct * total_cost  # Contribution de l'État en MAD
contribution_partenariats = contribution_partenariats_pct * total_cost  # Contribution des partenariats public-privé en MAD
contribution_menages = contribution_menages_pct * total_cost  # Contribution totale de la population cible en MAD

# Apport initial et montant du prêt par ménage
apport_initial = 0.1 * contribution_menages
montant_pret_total = 0.9 * contribution_menages
montant_pret_par_menage = montant_pret_total / nombre_menages

# Calcul du nombre de paiements mensuels
nombre_paiements = duree_remboursement * 12

# Calcul de la mensualité par ménage
mensualite = montant_pret_par_menage * (taux_interet_annuel / 12) / (1 - (1 + taux_interet_annuel / 12) ** -nombre_paiements)

# Création d'un DataFrame pour les paiements mensuels
mois = np.arange(1, nombre_paiements + 1)
paiements_mensuels = np.full(nombre_paiements, mensualite)
balance_restant = np.zeros(nombre_paiements)

# Initialisation du solde restant au montant du prêt par ménage
balance_restant[0] = montant_pret_par_menage

# Calcul du solde restant pour chaque mois
for i in range(1, nombre_paiements):
    interet_mensuel = balance_restant[i-1] * (taux_interet_annuel / 12)
    principal_mensuel = mensualite - interet_mensuel
    balance_restant[i] = balance_restant[i-1] - principal_mensuel

# Création du DataFrame pour les paiements mensuels
df_mensuel = pd.DataFrame({
    'Mois': mois,
    'Paiements_Mensuels': paiements_mensuels,
    'Balance_Restante': balance_restant
})

# Calcul des paiements annuels
annees = np.arange(1, duree_remboursement + 1)
solde_initial_annee = np.zeros(duree_remboursement)
paiement_annuel_total = np.zeros(duree_remboursement)
principal_annuel_total = np.zeros(duree_remboursement)
interet_annuel_total = np.zeros(duree_remboursement)
solde_final_annee = np.zeros(duree_remboursement)

for i in range(duree_remboursement):
    solde_initial_annee[i] = balance_restant[i * 12]
    paiement_annuel_total[i] = np.sum(paiements_mensuels[i * 12:(i + 1) * 12])
    interet_annuel_total[i] = np.sum(df_mensuel.loc[i * 12:(i + 1) * 12 - 1, 'Balance_Restante'] * (taux_interet_annuel / 12))
    principal_annuel_total[i] = paiement_annuel_total[i] - interet_annuel_total[i]
    solde_final_annee[i] = solde_initial_annee[i] - principal_annuel_total[i]

# Création du DataFrame pour les paiements annuels
df_annuel = pd.DataFrame({
    'Année': annees,
    'Solde Initial': solde_initial_annee,
    'Paiement Annuel Total': paiement_annuel_total,
    'Principal Annuel Total': principal_annuel_total,
    'Intérêts Annuels': interet_annuel_total,
    'Solde Final': solde_final_annee
})

# Affichage des résultats
st.write(f"**Contribution totale de l'État:** {contribution_etat} MAD")
st.write(f"**Contribution totale des ménages:** {contribution_menages} MAD")
st.write(f"**Contribution totale des partenariats public-privé:** {contribution_partenariats} MAD")
st.write(f"**Montant total du prêt par ménage:** {montant_pret_par_menage:.2f} MAD")
st.write(f"**Mensualité par ménage:** {mensualite:.2f} MAD")
st.write(f"**Coût total du projet:** {total_cost} MAD")

# Affichage du tableau annuel
st.write("### Tableau des paiements annuels :")
st.dataframe(df_annuel)

# Graphique de l'évolution de la balance restante
st.write("### Évolution de la Balance Restante du Prêt")
fig1, ax1 = plt.subplots(figsize=(10, 6))
ax1.plot(df_mensuel['Mois'], df_mensuel['Balance_Restante'], label='Balance Restante')
ax1.set_title('Évolution de la Balance Restante du Prêt')
ax1.set_xlabel('Mois')
ax1.set_ylabel('Balance Restante (MAD)')
ax1.grid(True)
ax1.legend()
st.pyplot(fig1)

# Graphique de la répartition des contributions
st.write("### Répartition des Contributions au Projet")
labels = ['État', 'Ménages', 'Partenariats Public-Privé']
contributions = [contribution_etat, contribution_menages, contribution_partenariats]

fig2, ax2 = plt.subplots(figsize=(8, 8))
ax2.pie(contributions, labels=labels, autopct='%1.1f%%', startangle=140)
ax2.set_title('Répartition des Contributions au Projet')
st.pyplot(fig2)
