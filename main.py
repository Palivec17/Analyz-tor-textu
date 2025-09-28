texty = [
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

# uživatelé a hesla
uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

import re # načte modul pro regulární výrazy
from collections import Counter # načtu třídu Counter, která slouží k počítání výskytů prvků

# Funkce pro přihlášení uživatele
def prihlaseni():
    uzivatel = input("uživatelské jméno:")
    heslo = input("heslo:")
    if uzivatele.get(uzivatel) == heslo:
        print("----------------------------------------")
        print(f"Vítej v aplikaci {uzivatel}, můžeš pokračovat v analýze textu.")
        print(f"Máme {len(texty)} texty k analýze.")
        print("----------------------------------------")
        return True
    else:
        print("Neplatná kombinace jména a hesla. Program bude ukončen.")
        return False

# Funkce pro výběr čísla analyzovaného textu
def vyber_text(texty):
    volba = input(f"Zadej číslo mezi 1 a {len(texty)} pro výběr textu: ")
    if not volba.isdigit():
        print("Neplatný vstup – očekává se číslo. Program bude ukončen.")
        exit()
    cislo = int(volba)
    if not (1 <= cislo <= len(texty)):
        print("Zadané číslo není v rozsahu dostupných textů. Program bude ukončen.")
        exit()
    return texty[cislo - 1]

def analyzuj_text(text):
    slova = text.split()
    pocet_slov = len(slova)
    velke_pismeno = [w for w in slova if w.istitle()]
    velkymi_pismeny = [w for w in slova if w.isupper() and w.isalpha()]
    malymi_pismeny = [w for w in slova if w.islower()]
    cisla = [int(w) for w in slova if w.isdigit()]
    delky_slov = [len(re.sub(r'\W', '', w)) for w in slova if re.sub(r'\W', '', w)]

    cetnosti = Counter(delky_slov)
    return {
        'pocet_slov': pocet_slov,
        'velke_pismeno': len(velke_pismeno),
        'velkymi_pismeny': len(velkymi_pismeny),
        'malymi_pismeny': len(malymi_pismeny),
        'pocet_cisel': len(cisla),
        'soucet_cisel': sum(cisla),
        'cetnosti_delky': dict(sorted(cetnosti.items()))
    }

def vykresli_graf(cetnosti):
    print("----------------------------------------")
    print("DEL|  VÝSKYTY        |POČET")
    print("----------------------------------------")
    for delka, pocet in cetnosti.items():
        hvezdy = '*' * pocet
        print(f"{delka:>3}|{hvezdy:<20}|{pocet}")





