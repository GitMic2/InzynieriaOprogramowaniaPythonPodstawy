"""
Zadanie 2 - Nawiasy

Opis zadania:
- Zweryfikuj, czy podany ciąg znaków zawiera poprawne nawiasy.
- Każdemu otwartemu nawiasowi '(' powinien odpowiadać nawias zamykający ')'.
- Jeśli nawiasy się zgadzają, funkcja ma zwrócić True, w przeciwnym wypadku False.
- Rozpatrujemy wyłącznie nawiasy okrągłe.

Przykładowe wejścia (True):
    "( if ( zero ? x ) max (/ 1 x ))"
    "I told ( that its not ( yet ) done ). (42)"
Przykładowe wejścia (False):
    ":-)"
    "Czesc (o kurcze, chyba niechcacy zamkne ten nawias dwa razy))"
    "())(("

Wymagania:
- Implementacja funkcji `check_parentheses(s: str) -> bool`.
- Użycie stosu do weryfikacji poprawności nawiasów.
"""

def check_parentheses(s: str) -> bool:
    """
    Sprawdza, czy w ciągu znaków 's' nawiasy okrągłe są poprawnie sparowane.

    Args:
        s (str): Ciąg znaków do analizy.

    Returns:
        bool: True jeśli nawiasy są poprawne, False w przeciwnym wypadku.
    """
    ### TUTAJ PODAJ ROZWIĄZANIE ZADANIA
    def check_parentheses(s: str) -> bool:

        stack = []

        for znak in s:

            if znak == '(':
                stack.append(znak)

            elif znak == ')':

                if len(stack) == 0:
                    return False

                stack.pop()

        return len(stack) == 0

    if __name__ == "__main__":

        tekst = input("Podaj tekst do sprawdzenia nawiasów: ")

        wynik = check_parentheses(tekst)

        if '(' not in tekst and ')' not in tekst:
            print("Brak okrągłych nawiasów w tekście")

        else:
            print(wynik)
    ### return False - powinno być zmienione i zwrócić prawdziwy wynik (zgodny z oczekiwaniami)
    return False

# Przykładowe wywołanie:
if __name__ == "__main__":
    examples = [
        "( if ( zero ? x ) max (/ 1 x ))",
        "I told ( that its not ( yet ) done ). (42)",
        ":-)",
        "Czesc (o kurcze, chyba niechcacy zamkne ten nawias dwa razy))",
        "())(("
    ]
    for example in examples:
        print(f"{example} -> {check_parentheses(example)}")