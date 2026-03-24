TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

users = {"bob": "123",
        "ann": "pass123",
        "mike": "password123",
        "liz": "pass123"}

username = input("Uživatelské jméno: ")
password = input("Heslo: ")

if username in users and users[username] == password:
    print("-" * 50)
    print(f"Vítej v aplikaci, {username}.")
elif username in users and users[username] != password:
    print("Špatné heslo, ukončuji program...")
    exit()    
else:
    print("Nezaregistrovaný uživatel, ukončuji program...")
    exit()

pocet_textu = len(TEXTS)

print(f"V aplikaci máme {pocet_textu} textů k analýze.")

print("-" * 50) # část výběr textu

vyber_text = input(f"Zadej číslo od 1 do {pocet_textu} pro výběr daného textu: ")

if not vyber_text.isdigit():
    print("Špatný vstup, ukončuji program...")
    exit()

vyber_text = int(vyber_text)

if vyber_text < 1 or vyber_text > pocet_textu:
    print("Špatný vstup, ukončuji program...")
    exit()

zvoleny_text = TEXTS[vyber_text - 1]

print("-" * 50) #část analyzátor

slova = zvoleny_text.split()
zacina_velke_pismo = 0
velke_pismo = 0
male_pismo = 0
pocet_cisel = 0
soucet_cisel = 0

for slovo in slova:
    ocistene = slovo.strip(",.")
    if ocistene.istitle():
        zacina_velke_pismo += 1
    if ocistene.isupper():
        velke_pismo += 1
    if ocistene.islower():
        male_pismo += 1
    if ocistene.isnumeric():
        pocet_cisel += 1
        soucet_cisel += int(ocistene)

print(f"V textu je {len(slova)} slov.")
print(f"Počet slov začínajících velkým písmenem: {zacina_velke_pismo}")
print(f"Počet slov psaných VELKÝMI písmeny: {velke_pismo}")
print(f"Počet slov psaných malými písmeny: {male_pismo}")
print(f"Počet čísel: {pocet_cisel}")
print(f"Součet všech čísel: {soucet_cisel}")

print("-" * 50) #část nadpisy

print(f"{'DELKA':>5}|{'POCET':<25}|{'CISLO':>5}")

print ("-" * 50) #část sloupcový graf

delka_slova = {}

for slovo in slova:
    ocistene = slovo.strip(",.")
    delka = len(ocistene)
    
    if delka in delka_slova:
        delka_slova[delka] += 1
    else:
        delka_slova[delka] = 1

for delka in sorted(delka_slova):
    pocet = delka_slova[delka]
    print(f"{delka:>5}|{'*' * pocet:<25}|{pocet:>5}")