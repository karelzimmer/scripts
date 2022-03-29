"""
Controleer ISBN 10 en 13

check_isbn("0-7821-1765-1") -> True/False

ISBN mag '-' of ' ' bevatten, of aaneengeschreven zijn

voorbeelden ISBN-10:
(kan X of x als controlecijfer bevatten)
0-7821-1765-1, 1-55615-877-7, 90-14-04434-8, 90-267-1178-6
3-7466-5517-X, 3-88680-843-2

voorbeelden ISBN-13:
(bevat nooit X als controle-cijfer)
978-3-88680-843-4

http://www.isbn-international.org/
"""

__all__ = ['check_isbn']


def check_isbn(isbn):
    if isbn.startswith("978"):
        return checkISBN13(isbn)
    else:
        return checkISBN10(isbn)


def checkISBN10(isbn):
    if not isbn or len(isbn) < 10:
        return False

    som = 0
    tel = 10
    streepjes = 0
    for ch in isbn[:-1]:
        if ch.isdecimal():
            som += int(ch) * tel
            tel -= 1
        elif ch == ' ' or ch == '-':
            streepjes += 1
        else:
            return False
    if tel != 1 or streepjes > 3:
        return False

    ch = isbn[-1]               #controlegetal kan 0-9 of X zijn...
    if ch.isdecimal():
        som += int(ch)
    elif ch.upper() == 'X':
        som += 10
    else:
        return False
    return som % 11 == 0

def checkISBN13(isbn):
    if not isbn or len(isbn) < 13:
        return False

    som = 0
    tel = 13
    streepjes = 0
    for ch in isbn[:-1]:
        if ch.isdecimal():
            som += int(ch) * (1 if (tel & 1) == 1 else 3)
            tel -= 1
        elif ch == ' ' or ch == '-':
            streepjes += 1
        else:
            return False
    if tel != 1 or streepjes > 4:
        return False

    ch = isbn[-1]               #controlegetal mag niet X zijn...
    if ch.isdecimal():
        som += int(ch)
    else:
        return False
    return som % 10 == 0


if __name__ == "__main__":
    print(check_isbn("0-7821-1765-1"))
    print(check_isbn("978-3-88680-843-4"))

    #print(checkISBN10("0-7821-1765-1"))
    #print(checkISBN13("978-3-88680-843-4"))
    
