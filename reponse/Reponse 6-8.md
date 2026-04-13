Réponses — Comparaison des modèles


Question 6 : Quel modèle a le meilleur recall ?

- Logistic Regression : recall = 0.00 
- Random Forest : recall = 0.92
- Gradient Boosting : recall = 0.99

Le Gradient Boosting a le meilleur recall. Il détecte 99% des répondants "North Central".
La Logistic Regression a un recall de 0 : elle prédit tout le monde comme "other".


Question 7 : Quel modèle a la meilleure application pratique ?

Avec les coûts : FP = -10, FN = -1, TP = +5, TN = +2

- Logistic Regression : gain = 981 (TP=0, FN=669, FP=0, TN=825)
- Random Forest : gain = 4293 (TP=618, FN=51, FP=33, TN=792)
- Gradient Boosting : gain = 4641 (TP=662, FN=7, FP=26, TN=799)

Le Gradient Boosting a le meilleur gain pratique (4641). Il fait très peu d'erreurs des deux types.


Question 8 : Quel modèle généralise le mieux ?

Scores en cross-validation (5 folds) :

- Logistic Regression : train = 0.5525, test = 0.5525, écart = 0.0000
- Random Forest : train = 1.0000, test = 0.9339, écart = 0.0661
- Gradient Boosting : train = 1.0000, test = 0.9178, écart = 0.0822

Le Random Forest généralise le mieux parmi les modèles utiles (écart de 0.066).
La Logistic Regression a un écart de 0 mais elle ne fait rien d'utile (score de 0.55 = prédit toujours la même classe).
Le Gradient Boosting est le plus performant en test car il est plus polivalent sur nos resultat.

