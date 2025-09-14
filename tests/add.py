import json

# Chemin vers ton fichier JSON
fichier_json = "data/qa.json"

# Nouvelles entrées à ajouter
nouvelles_entrees = [
    {
        "Q": "Comment puis-je cultiver des tomates avec succès ?",
        "A": [
            "Choisis une variété adaptée à ton climat et plante-les dans un sol bien drainé et riche en nutriments.",
            "Assure-toi qu'elles reçoivent beaucoup de soleil (au moins 6 heures par jour) et arrose-les régulièrement à la base pour éviter les maladies."
        ]
    },
    {
        "Q": "Comment utiliser efficacement les raccourcis clavier sur Windows ou macOS ?",
        "A": [
            "Apprends les raccourcis de base comme 'Ctrl+C' (copier) et 'Ctrl+V' (coller) sur Windows, ou 'Cmd+C' et 'Cmd+V' sur macOS.",
            "Pour aller plus loin, utilise des raccourcis comme 'Ctrl+Z' (annuler) ou 'Cmd+Z' pour gagner du temps."
        ]
    },
    {
        "Q": "Comment puis-je me débarrasser des fourmis dans ma maison ?",
        "A": [
            "Suis leur trace pour trouver l'endroit où elles entrent et bouche les fissures et les trous.",
            "Tu peux utiliser un mélange de vinaigre blanc et d'eau pour nettoyer les surfaces ou des remèdes naturels comme la cannelle ou la menthe poivrée qui repoussent les fourmis."
        ]
    },
    {
        "Q": "Comment puis-je améliorer ma posture au bureau ?",
        "A": [
            "Assure-toi que ton dos est droit, tes pieds sont à plat sur le sol et que l'écran est à la hauteur de tes yeux.",
            "Prends des pauses régulières pour t'étirer et bouger afin d'éviter les tensions."
        ]
    },
    {
        "Q": "Comment lire un pneu de voiture ?",
        "A": [
            "Reconnais les informations clés : la largeur, le rapport d'aspect et le diamètre de la jante se trouvent sur le flanc du pneu (par exemple, 205/55 R16).",
            "La date de fabrication (semaine et année) et l'indice de vitesse sont également inscrits et importants pour ta sécurité."
        ]
    },
    {
        "Q": "Comment économiser de l'eau à la maison ?",
        "A": [
            "Installe des aérateurs sur les robinets et prends des douches plus courtes au lieu de bains.",
            "Ne laisse pas l'eau couler quand tu te brosses les dents et répare rapidement les fuites."
        ]
    },
    {
        "Q": "Comment faire un bon plan de repas pour la semaine ?",
        "A": [
            "Commence par choisir une ou deux recettes faciles que tu aimes et construis ton plan autour de ces plats.",
            "Utilise les ingrédients restants de la veille et fais une liste de courses claire pour éviter d'acheter des choses inutiles."
        ]
    },
    {
        "Q": "Comment puis-je me protéger du vol d'identité ?",
        "A": [
            "Déchire ou détruis les documents importants contenant des informations personnelles avant de les jeter.",
            "Vérifie régulièrement tes relevés bancaires et ton rapport de crédit pour repérer toute activité suspecte."
        ]
    },
    {
        "Q": "Comment photographier un ciel étoilé ?",
        "A": [
            "Utilise un appareil photo avec un mode manuel, un trépied pour plus de stabilité et une télécommande ou un retardateur pour éviter les flous de bougé.",
            "Règle ton appareil avec une longue exposition (15 à 30 secondes), une grande ouverture (f/2.8 ou plus bas) et une sensibilité ISO élevée."
        ]
    },
    {
        "Q": "Comment me préparer pour un rendez-vous chez le médecin ?",
        "A": [
            "Prépare une liste de tes symptômes et de toutes les questions que tu as pour le médecin.",
            "Apporte tous les médicaments que tu prends et les résultats d'examens récents."
        ]
    },
    {
        "Q": "Comment détartrer une bouilloire électrique ?",
        "A": [
            "Remplis la bouilloire avec un mélange moitié eau, moitié vinaigre blanc et fais bouillir.",
            "Laisse reposer le mélange pendant 30 minutes, puis vide et rince plusieurs fois pour enlever l'odeur de vinaigre."
        ]
    },
    {
        "Q": "Comment puis-je rendre ma maison plus écologique ?",
        "A": [
            "Réduis ta consommation de plastique en utilisant des sacs réutilisables et des gourdes.",
            "Passe à des ampoules LED et choisis des appareils électroménagers avec une bonne note énergétique."
        ]
    },
    {
        "Q": "Comment puis-je m'améliorer en dessin ?",
        "A": [
            "Commence par les bases : pratique la perspective, les proportions et les ombres.",
            "Dessine régulièrement et inspire-toi d'artistes que tu aimes pour trouver ton propre style."
        ]
    },
    {
        "Q": "Comment changer la roue d'une voiture ?",
        "A": [
            "Gare-toi sur une surface plane et sécurisée, active le frein à main et enclenche une vitesse.",
            "Dessers les écrous de roue avant de soulever la voiture avec le cric, puis enlève l'écrou, remplace le pneu et serre à nouveau."
        ]
    },
    {
        "Q": "Comment conserver les légumes racines pour l'hiver ?",
        "A": [
            "Nettoie et sèche-les bien, puis stocke-les dans une caisse avec du sable ou de la sciure dans un endroit frais et sombre.",
            "Vérifie-les régulièrement pour enlever ceux qui commencent à pourrir."
        ]
    },
    {
        "Q": "Comment puis-je gérer mes finances et mon épargne ?",
        "A": [
            "Fixe-toi des objectifs financiers clairs (acheter une maison, voyager) et mets de l'argent de côté chaque mois.",
            "Automatise tes épargnes pour que ce soit plus simple et réduis les dépenses inutiles."
        ]
    },
    {
        "Q": "Comment décongeler un pare-brise rapidement ?",
        "A": [
            "Utilise un dégivreur en aérosol ou un mélange d'eau et d'alcool isopropylique.",
            "Ne verse jamais d'eau chaude, car le choc thermique pourrait fissurer le pare-brise."
        ]
    },
    {
        "Q": "Comment puis-je augmenter la durée de vie de mes vêtements ?",
        "A": [
            "Lis attentivement les étiquettes pour connaître les instructions de lavage et de séchage.",
            "Lave tes vêtements à l'eau froide pour éviter qu'ils ne rétrécissent ou que les couleurs ne déteignent."
        ]
    },
    {
        "Q": "Comment choisir une bonne bouteille de vin au supermarché ?",
        "A": [
            "Ne te fie pas uniquement à l'étiquette, vérifie l'année de récolte et le nom de la région pour t'assurer de la qualité.",
            "Si tu ne connais pas, choisis un vin d'une région connue pour la production de cette variété de cépage."
        ]
    },
    {
        "Q": "Comment puis-je me préparer pour une randonnée en montagne ?",
        "A": [
            "Vérifie la météo avant de partir et informe un proche de ton itinéraire et de l'heure de ton retour.",
            "Emporte de l'eau, de la nourriture, un kit de premiers secours et des vêtements adaptés, même en été."
        ]
    }
]







# 1. Charger le JSON existant
try:
    with open(fichier_json, "r", encoding="utf-8") as f:
        data = json.load(f)
except FileNotFoundError:
    # Si le fichier n'existe pas, on crée une liste vide
    data = []

# 2. Ajouter les nouvelles entrées à la liste
data.extend(nouvelles_entrees)

# 3. Sauvegarder à nouveau le JSON
with open(fichier_json, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print(f"{len(nouvelles_entrees)} entrées ajoutées au fichier JSON.")
