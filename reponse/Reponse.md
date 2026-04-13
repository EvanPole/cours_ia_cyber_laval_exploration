

Question 1 :

Le dataset contient 2 494 lignes et 28 colonnes.


Question 2 :

La cible (Census_Region) est déséquilibré :
- East North Central : 758
- West North Central : 358
- Middle Atlantic : 334
- South Atlantic : 248
- Pacific : 243
- Mountain : 190
- West South Central : 172
- East South Central : 97
- New England : 94

La plus grosse classe est 8 fois plus grande que la plus petite. Le dataset est donc déséquilibré.


Question 3 :

Il y a 1 seule feature numérique (RespondentID), mais c'est juste un identifiant donc pas trop utile pour la prédiction.
Les 27 autre colones sont catégorielle (texte) : des questions sur le Midwest, le genre, l'âge, le revenu, l'éducation, etc.


Question 4 :

Avec isnull().sum(), on trouve 0 valeur NaN dans toutes les colonnes.
Mais en regardant les valeurs uniques, on voit que le caractère "?" est utilisé comme valeur manquante :
- Household_Income : 68 fois "?"
- Education : 30 fois "?"

Il y a donc des valeurs manquantes cachées qu'il faudra traiter avant d'entraîner un modèle.


Question 5 :

La réponse la plus fréquent est "Not at all" avec 965 répondants.
- Not at all : 965
- A lot : 697
- Some : 528
- Not much : 304

C'est logique car le dataset couvre tout les États-Unis, pas seulement le Midwest.


Bonus :

- Female : 1 326
- Male : 1 168

Répartition à peu près équilibrer avec un peu plus de femmes.