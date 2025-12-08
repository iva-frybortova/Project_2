import random

zadani_oddelovac = "-"
zadani_oddelovac_pocet = 47
zadani_povolene_prvky = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
zadani_pocet_prvku = 4
zadani_omezeni = {"pozice": 0, "hodnota": "0"}
zadani_gratulace = "Correct, you've guessed the right number"
pozdrav_text = "Hi there!"
popisek_text = """I've generated a random 4 digit number for you.
    Let's play a bulls and cows game."""
vyzva_text = "Enter a number: "

def napis_oddelovac(oddelovac: str, n: int) -> str:
    '''Vrátí řetězec, který se skládá z n oddělovačů'''
    return oddelovac*n

print(pozdrav_text)
print(napis_oddelovac(zadani_oddelovac, zadani_oddelovac_pocet))
print(popisek_text)
print(napis_oddelovac(zadani_oddelovac, zadani_oddelovac_pocet))


def vygeneruj_mnozinu(povolene_prvky: list, pocet_prvku: int) -> list:
    '''Vrátí list obsahující náhodně vygenerované prvky z povolene_prvky, počet těchto prvků je pocet_prvku'''
    mnozina = []
    for prvek in range(pocet_prvku):
        prvek = random.choice(povolene_prvky)
        mnozina.append(str(prvek))
    return mnozina


def zkontroluj_mnozinu(mnozina: list, povolene_prvky: list, pocet_prvku: int, omezeni: dict) -> bool:
    '''
    Kontroluje množinu, jestli splňuje zadané podmínky: pocet_prvku, unikátní hodnoty, omezeni, povolene_prvky. 
    Vrátí True/False.
    ''' 
    # mnozina má upožadovaný pocet_prvku
    podminka_1 = len(mnozina) == pocet_prvku

    # mnozina má unikátní hodnoty
    podminka_2 = len(set(mnozina)) == pocet_prvku

    # na definované pozici slovniku omezeni není definovaná hodnota
    podminka_3 = mnozina[omezeni.get("pozice")] != omezeni.get("hodnota")

    # všechny prvky z mnozina jsou přítomny v povolene_prvky
    podminka_4 = set(mnozina) <= set([str(prvek) for prvek in povolene_prvky]) 
   
    return podminka_1 and podminka_2 and podminka_3 and podminka_4


def hledej_byky(vstup_uzivatel: list, vstup_program: list, pocet_prvku: int) -> int:
    '''Prochází množinu vstup_uzivatel, porovnává ji s vstup_program. 
    Pokud je nějaký prvek z vstup_uzivatel na stejné pozici jako v množině vstup_program, započítá jej jako býka
    '''
    pocet_byku = 0
    for i in range(pocet_prvku):
        if vstup_uzivatel[i] == vstup_program[i]:
            pocet_byku += 1
    return pocet_byku


def hledej_kravy(vstup_uzivatel: list, vstup_program: list, pocet_prvku: int) -> int:
    '''Prochází množinu vstup_uzivatel, porovnává ji s vstup_program. 
    Pokud je nějaký prvek z vstup_uzivatel přítomen v množině vstup_program, započítá jej jako krávu
    '''
    pocet_krav = 0
    for i in range(pocet_prvku):
        if vstup_uzivatel[i] in vstup_program:
            pocet_krav += 1
    return pocet_krav


# Spustí se smyčka, ve které se generuje číslo a probíhá kontrola. Jakmile číslo splní podmínky, smyčka se ukončí.
while True:
    vygenerovane_cislo = vygeneruj_mnozinu(zadani_povolene_prvky, zadani_pocet_prvku)    

    if zkontroluj_mnozinu(vygenerovane_cislo, zadani_povolene_prvky, zadani_pocet_prvku, zadani_omezeni):  
        break

print(vyzva_text)
print(napis_oddelovac(zadani_oddelovac, zadani_oddelovac_pocet))

pocet_pokusu = 0    
tvuj_pocet_byku = 0

# Spustí se smyčka, ve které je uživatel vyzván k napsání vstupu ve správném formátu. Smyčka běží tak dlouho, dokud uživatel nezíská potřebný počet býků.
while tvuj_pocet_byku < zadani_pocet_prvku:    
    # uživatelský vstup se vloží do proměnné hadane_cislo jako list
    hadane_cislo = list(input())
    pocet_pokusu +=1

    # probíhá kontrola formátu vstupu
    if zkontroluj_mnozinu(hadane_cislo, zadani_povolene_prvky, zadani_pocet_prvku, zadani_omezeni):
        
        # spustí se fce hledající býky     
        tvuj_pocet_byku = hledej_byky(hadane_cislo, vygenerovane_cislo, zadani_pocet_prvku)
        if tvuj_pocet_byku == zadani_pocet_prvku:
            break        
        elif tvuj_pocet_byku == 1:
            format_byci = "bull"            
        else:
            format_byci = "bulls"            

        # spustí se fce hledající krávy, od výsledného počtu se odečte počet býků        
        tvuj_pocet_krav = hledej_kravy(hadane_cislo, vygenerovane_cislo, zadani_pocet_prvku) - tvuj_pocet_byku
        if tvuj_pocet_krav == 1:
            format_kravy = "cow"
        else:
            format_kravy = "cows"

        # naformátuje se odpověď
        print(f"{tvuj_pocet_byku} {format_byci}, {tvuj_pocet_krav} {format_kravy}")        
        print(napis_oddelovac(zadani_oddelovac, zadani_oddelovac_pocet))                       
        
    else:
        # uživatelův vstup není ve správném formátu
        omezeni_pozice, omezeni_hodnota = zadani_omezeni.get("pozice")+1, zadani_omezeni.get("hodnota")
        print(f"Your input should contain {zadani_pocet_prvku} unique characters \nout of this list: {zadani_povolene_prvky}. \n{omezeni_hodnota} is not allowed at position {omezeni_pozice}.")
        print(napis_oddelovac(zadani_oddelovac, zadani_oddelovac_pocet))

# uživatel uhodl generovaný vstup
print(zadani_gratulace)
if pocet_pokusu == 1:
    format_pokus = "guess"
else:
    format_pokus = "guesses"

# naformátuje se odpověď
print(f"in {pocet_pokusu} {format_pokus}!")
print(napis_oddelovac(zadani_oddelovac, zadani_oddelovac_pocet))
print("That's amazing!")