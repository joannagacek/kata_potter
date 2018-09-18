from typing import List

# Funkcja do wyliczania kwoty do zapłaty za wypożyczone książki. Książki reprezentowane są przez liczbę całkowitą.
# Szczegóły implementacji https://codingdojo.org/kata/Potter/
def price(book: List[int], discount: List[float]) -> float:

    # Kwota do zapłaty
    price = 0.0

    # Koszyk, który zawiera serie książek w postaci listy list książek(liczb całkowitych)
    basket = []

    # Dla każej zakupionej książki
    for i, b in enumerate(book):
        n = False
        # Dla każdej serii książek w koszyku
        for j, s in enumerate(basket):
            if not (b in basket[j]):
                # Jeżeli ksiażka nie istnieje w tej serii, dodaj tę książkę do tej serii i zacznij od nowa
                basket[j].append(b)
                if 5 == len(s) and j + 1 < len(basket) and len(basket[j + 1]) == 3:
                    # Jeżeli książka jest piatą różną ksiażką w serii a kolejna seria zawiera trzy ksiażki to
                    # przenieś tę ksiażkę, żeby policzyć zniżki dla dwóch serii po cztery książki
                    basket[j + 1].append(basket[j].pop(4))
                n = True
                break
        if not n:
            # Jeżeli nie można dodać książki do istniejącej serii, utwórz nową serię z ta książką
            basket.append([b])

    for k in basket:
        # Dla każdej serii książek, wylicz cenę uwzględniającą zniżkę i dodaj do ceny końcowej
        price += 8 * len(k) * discount[len(k)]

    # Zwróć cenę końcową za wypożyczone książki
    return price
