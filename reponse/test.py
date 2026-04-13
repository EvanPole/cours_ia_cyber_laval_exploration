import matplotlib.pyplot as plt
from skrub.datasets import fetch_midwest_survey

dataset = fetch_midwest_survey()

X = dataset.X
y = dataset.y

#  Question 1: 
print("  Question 1 :  ")
print("Nombre de lignes et colonnes :")
print(X.shape)
print("\nPremières lignes :")
print(X.head())

#  Question 2: 
print("\n  Question 2 : ")
print("Distribution de la cible :")
print(y.value_counts())

y.value_counts().plot.barh()
plt.title("Distribution de la région de recensement")
plt.xlabel("Nombre")
plt.tight_layout()
plt.show()

#  Question 3: 
print("\n  Question 3 :  ")
print("Noms des colonnes :")
print(X.columns.tolist())
print("\nTypes de données :")
print(X.dtypes)
print(f"\nFeatures numériques : {X.select_dtypes(include='number').shape[1]}")
print(f"Features catégorielles : {X.select_dtypes(include='object').shape[1]}")

#  Question 4: 
print("\n  Question 4 : ")
print("Valeurs manquantes (NaN) par colonne :")
print(X.isnull().sum())

print("\nValeurs uniques pour Household_Income :")
print(X["Household_Income"].value_counts())

print("\nValeurs uniques pour Education :")
print(X["Education"].value_counts())

#  Question 5: 
print("\n  Question 5 : ")
col = "How_much_do_you_personally_identify_as_a_Midwesterner"
print("Réponses les plus fréquentes :")
print(X[col].value_counts())

X[col].value_counts().plot.barh()
plt.title("Identification en tant que Midwesterner")
plt.xlabel("Nombre")
plt.tight_layout()
plt.show()

#  Bonus: 
print("\n  Bonus : ")
print("Distribution du genre :")
print(X["Gender"].value_counts())

X["Gender"].value_counts().plot.barh()
plt.title("Distribution du genre")
plt.xlabel("Nombre")
plt.tight_layout()
plt.show()