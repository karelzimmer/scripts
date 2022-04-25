#temperature



def cels2fahr(temp):
    return round(32.0 + temp * 1.8, 1)

def fahr2cels(temp):
    return round((temp - 32.0) / 1.8, 1)


if __name__ == "__main__":
    print(cels2fahr(39))
    print(fahr2cels(83))

