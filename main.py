from collections import Counter
from pprint import pprint

# 1) Sortir le compte des lettres de chaque initiale du CAC40

# Merci wikipedia pour la liste des sociétés du CAC40
cac40 = ["Air Liquide", "Airbus", "Alstom", "ArcelorMittal", "AXA", "BNP Paribas", "Bouygues", "Capgemini", "Carrefour", "Crédit Agricole", "Danone", "Dassault Systèmes", "Engie", "EssilorLuxottica", "Eurofins Scientific", "Hermès", "Kering", "L'Oréal", "Legrand", "LVMH", "Michelin", "Orange", "Pernod Ricard", "Publicis", "Renault", "Safran", "Saint-Gobain", "Sanofi", "Schneider Electric", "Société Générale", "Stellantis", "STMicroelectronics", "Teleperformance", "Thales", "TotalEnergies", "Unibail-Rodamco-Westfield", "Veolia", "Vinci", "Vivendi", "Worldline"]
# On sort le nombre de chaque lettres
cac40_letter_count = Counter([c[0].lower() for c in cac40])
# On doit bien avoir 40 initiales
assert(sum(cac40_letter_count.values()) == 40)
pprint(cac40_letter_count)

# 2) Filtrer les mots francais de longueur >= 6
MIN_WORD_LENGTH = 6
# On sort la liste des mots de plus de MIN_WORD_LENGTH lettres
# dictionnaire pris chez le jeu SUTOM
french_words = [w.rstrip() for w in open("mots.txt").readlines() if len(w) > MIN_WORD_LENGTH]
# 438401 de longueur > 6 dans le dictionnaire

# 3) Trouver les mots que l’on peut former avec les contraintes CAC40

# Chacune des lettres qui les constituent sont présente au moins autant
# de fois dans les initiales du CAC40
possible_words = []
for word in french_words:
	letter_count = Counter(word)
	if all([letter_count[c] <= cac40_letter_count[c] for c in word]):
		possible_words.append(word)


# 11215 mots sont possibles avec le CAC40

# 4) Supprimer les mots similaires

# On veut éliminer les mots ayant une racine commune
# pour ne garder que les plus longs
# Pour ça, on extrait la racine via traitement du langage naturel
from nltk.stem.snowball import SnowballStemmer
from collections import defaultdict
stemmer = SnowballStemmer("french")
stems_and_words = defaultdict(list)

for w in possible_words:
    stems_and_words[stemmer.stem(w)].append(w)

longest = [max(stems_and_words[k], key=len) for k in stems_and_words.keys()]

# 5) Affichage
pprint(longest)
print(f"{len(french_words)} de longueur > {MIN_WORD_LENGTH} dans le dictionnaire")
print(f"{len(possible_words)} mots possibles avec le CAC40")
print(f"{len(longest)} mots en filtrant par racine commune")

# Avec les initiales du CAC40, on peut former 3656 mots de plus de 6 lettres
# tel que (au hasard ^^):

# carpettes
# cartels
# caveau
# chevretasses
# cradots
# crapauds
# daurades
# kleptocrates
# lavabos
# leadeurs
# maboules
# maladresses
# sucettes
# thermostables
# waterballasts