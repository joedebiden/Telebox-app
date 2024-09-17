import csv

# Liste des utilisateurs
users = [
    "invoker_new", "nikolaasrb", "thecloutclub", "redditshopz", "mcguac", 
    "easymoneysniperr0", "Redditaccsforu", "Highrise_management", "grindstar", 
    "theman1234556", "accslarry", "cHeeezus", "fxrouk99", "lucassf", "dg_efm", 
    "surgedrops", "sammknan", "mansory12345", "fast2move2010", "jessetarnowski", 
    "harlow21", "meuffake", "Karmpradhan", "Damien_Escott", "wwanjin", 
    "moonwalker9999", "Prince8in", "jackcreate", "SarahKraft", "n3ofm", 
    "elekrobert4", "Glamauraa", "JustinLT", "davidxmgmt", "Hot_Viki", "KyleLGM", 
    "am0n369", "monsieurzero", "JJJen_23", "Laura_lat", "AlbianBatwa", 
    "Mr1TJ", "thomasslrc", "ddarkyman", "MihaelTMM", "Wilx015", 
    "Eduardo_Vestiti", "leones03", "Nachi_Management", "ryjay1", 
    "costablancacbd", "housstm", "edithw24", "penelopegs", "lucxzz", 
    "FelioseOFM", "OheXwhY123", "ianbandz", "Quennlove56", "AlbandiAL", 
    "Fantaxyherz", "graceful2142", "Bzoneagenc", "kenziskyx", "d1234567890000000", 
    "globalflux", "letstryagainnnn", "chEight88", "redditorX", "AAMarketing7", 
    "rexymedia", "supranxi", "NickPlot", "antuanvera", "franciszek_7", 
    "Ed3n333", "bloodymarvellous", "sosaforeign8", "tonkow9", "losage1", 
    "AdamDjokov", "icey1833", "Dmegatimmy", "Charlyyog", "dikonos", 
    "yuta1656", "bend10001", "exclb", "db_0303", "x_Prometheus_x", 
    "crazyasianboyy", "ZedBam", "mancicvuk", "darcyxov", "s2saint", 
    "GODLIKEENERGY", "Eires12394", "ShinnOFM", "Slyyelias", "dbenwell"
]

# Chemin du fichier CSV
csv_file = "users_100.csv"

# Ouvrir le fichier en mode écriture
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)

    # Écrire les en-têtes
    writer.writerow(["username", "user id", "access hash", "name", "group", "group id"])

    # Écrire les données
    for user in users:
        writer.writerow([user, "", "", "", "", ""])

print(f"Fichier '{csv_file}' créé avec succès.")
