#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]  # Skriptin adını çıxmaq üçün 1-ci indeksdən başlayırıq
    count = len(argv)

    # Birinci sətir: Arqumentlərin sayı və uyğun sonluq
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))

    # İkinci hissə: Arqumentlərin siyahısı (əgər varsa)
    for i in range(count):
        print("{}: {}".format(i + 1, argv[i]))
