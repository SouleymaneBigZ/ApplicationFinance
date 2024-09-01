# ApplicationFinance
Voici une description que vous pouvez utiliser pour documenter le code dans un dépôt GitHub :

---

# Calculateur de Contributions et de Prêt

## Description

Cette application Streamlit permet de calculer les contributions financières des différentes parties prenantes (État, ménages, partenariats public-privé) à un projet, ainsi que les paramètres de financement pour les ménages. L'application propose deux modes de calcul :

1. **Mode Classique** : Permet de calculer la mensualité nécessaire pour rembourser un prêt sur une durée fixe.
2. **Mode Optimisé** : Permet d'optimiser soit la durée du prêt en fonction d'une mensualité souhaitée, soit de calculer le montant du prêt pour une durée donnée.

## Fonctionnalités

- **Calcul des Contributions** : Répartition du coût total du projet entre l'État, les ménages et les partenariats public-privé.
- **Calcul de la Mensualité** : En fonction de la contribution des ménages, du taux d'intérêt et de la durée du prêt.
- **Optimisation du Prêt** :
  - **Optimisation de la Durée** : Calcule la durée de remboursement pour une mensualité fixe.
  - **Optimisation du Montant du Prêt** : Calcule le montant du prêt pour une durée donnée et une mensualité souhaitée.
- **Affichage des Résultats** :
  - Tableau des paiements annuels, montrant les soldes initiaux et finaux, les intérêts et les principaux payés chaque année.
  - Graphique de l'évolution de la balance restante du prêt.
  - Graphique de la répartition des contributions au projet.

## Utilisation

1. **Installation** : Assurez-vous d'avoir [Python](https://www.python.org/downloads/) et [Streamlit](https://streamlit.io/) installés sur votre machine. Clonez ce dépôt puis installez les dépendances requises.

    ```bash
    pip install -r requirements.txt
    ```

2. **Exécution de l'application** :

    Lancez l'application Streamlit à l'aide de la commande suivante :

    ```bash
    streamlit run app.py
    ```

3. **Interagir avec l'interface** :

    - Sélectionnez le mode de calcul (Classique ou Optimisé).
    - Entrez les données requises, telles que le coût total du projet, le nombre de ménages, les taux d'intérêt, etc.
    - Visualisez les résultats sous forme de tableaux et de graphiques directement dans l'interface Streamlit.

## Exemple

L'application est particulièrement utile pour les projets nécessitant une planification financière complexe, où il est important de comprendre l'impact des contributions et des prêts sur la population cible. Par exemple, elle peut être utilisée pour planifier des projets d'infrastructure financés par plusieurs sources et nécessitant des contributions de la population locale.

## Contributions

Les contributions sont les bienvenues ! Si vous souhaitez améliorer cette application, n'hésitez pas à créer une branche, ajouter vos fonctionnalités et soumettre une pull request.

## Licence

Ce projet est sous licence OZS. Veuillez consulter le fichier `LICENSE` pour plus de détails.

---

Cette description fournit un aperçu complet de ce que fait le code, comment l'utiliser, et comment y contribuer, ce qui est essentiel pour un dépôt GitHub.
