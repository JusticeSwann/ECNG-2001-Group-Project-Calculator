import math

def ak_1(A,k):
    term1 = ((4 * A) / (2 * math.pi * k)) * math.sin(2 * math.pi * k / 4)
    term2 = ((2 * A) / ((2 * math.pi * k) ** 2)) * math.cos(2 * math.pi * k / 8)
    term3 = ((4 * A) / (2 * math.pi * k)) * math.sin(6 * math.pi * k / 8)
    term4 = ((16 * A) / ((2 * math.pi * k) ** 2)) * math.cos(6 * math.pi * k / 8)
    term5 = ((2 * A) / (2 * math.pi * k)) * math.cos(2 * math.pi * k / 8)
    term6 = ((2 * A) / (2 * math.pi * k)) * math.cos(2 * math.pi * k / 2)
    term7 = ((1 * A) / (2 * math.pi * k)) * math.sin(6 * math.pi * k / 4)
    term8 = ((24 * A) / ((2 * math.pi * k) ** 2)) * math.cos(6 * math.pi * k / 4)
    term9 = ((24 * A) / ((2 * math.pi * k) ** 2)) * math.cos(10 * math.pi * k / 8)
    term10 = ((24 * A) / (2 * math.pi * k)) * math.sin(14 * math.pi * k / 8)
    term11 = ((11 * A) / (2 * math.pi * k)) * math.sin(6 * math.pi * k / 4)
    term12 = ((24 * A) / ((2 * math.pi * k) ** 2)) * math.cos(14 * math.pi * k / 8)
    term13 = ((24 * A) / ((2 * math.pi * k) ** 2)) * math.cos(6 * math.pi * k / 4)
    term14 = 0
    term15 = ((2 * A) / (2 * math.pi * k)) * math.sin(14 * math.pi * k / 8)

    result = term1 - term2 - term3 - term4 + term5 - term6 - term7 - term8 + term9 - term10 - term11 + term12 - term13 - term14 + term15
    return result


def bk_1(A,k):
    term1 = ((2 * A) / (2 * math.pi * k)) * math.cos((2* math.pi * k) /8)
    term2 = (2 * A) / (2 * math.pi * k)
    term3 = ((4 * A) / (2 * math.pi * k)) * math.cos(2* math.pi * k / 4)
    term4 = ((2 * A) / (2 * math.pi * k)) * math.cos(2 * math.pi * k / 8)
    term5 = ((16 * A) / ((2 * math.pi * k) ** 2)) * math.sin(2 * math.pi * k / 4)
    term6 = ((16 * A) / ((2 * math.pi * k) ** 2)) * math.sin(2 * math.pi * k / 8)
    term7 = ((2 * A) / (8 * math.pi * k)) * math.cos(2 * math.pi * k / 2)
    term8 = ((4 * A) / (2 * math.pi * k)) * math.cos(6 * math.pi * k / 8)
    term9 = ((16 * A) / ((2 * math.pi * k) ** 2)) * math.sin(2 * math.pi * k / 2)
    term10 = ((16 * A) / ((2 * math.pi * k) ** 2)) * math.sin(2 * math.pi * k / 8)
    term11 = ((2 * A) / (2 * math.pi * k)) * math.cos(10 * math.pi * k / 8)
    term12 = ((2 * A) / (2 * math.pi * k)) * math.cos(2 * math.pi * k / 2)
    term13 = ((7 * A) / (2 * math.pi * k)) * math.cos(6* math.pi * k / 4)
    term14 = ((4 * A) / (2 * math.pi * k)) * math.cos(10 * math.pi * k / 8)
    term15 = ((24 * A) / ((2 * math.pi * k) ** 2)) * math.sin(6 * math.pi * k / 4)
    term16 = ((24 * A) / ((2 * math.pi * k) ** 2)) * math.sin(10 * math.pi * k / 8)
    term17 = ((10 * A) / (2 * math.pi * k)) * math.cos(14 * math.pi * k / 8)
    term18 = ((1 * A) / (2 * math.pi * k)) * math.cos(6 * math.pi * k / 4)
    term19 = ((24 * A) / ((2 * math.pi * k) ** 2)) * math.sin(14 * math.pi * k / 8)
    term20 = ((24 * A) / ((2 * math.pi * k) ** 2)) * math.sin(6 * math.pi * k / 4)
    term21 = ((2 * A) / (2 * math.pi * k)) * math.cos(2 * math.pi * k)
    term22 = ((2* A) / (2 * math.pi * k)) * math.cos(14 * math.pi * k / 8)
    
    result = term1 - term2 - term3 + term4 + term5 + term6 + term7 + term8 - term9 + term10 - term11 + term12 + term13 - term14 + term15 + term16 - term17 + term18 - term19 - term20 + term21 - term22
    return result


def ck_1(A,k):
    ak = ak_1(A,k)
    bk = bk_1(A,k)
    result = math.sqrt((ak) ** 2 + (bk) ** 2)
    return result

def theta_1(A,k):
    ak = ak_1(A,k)
    bk = bk_1(A,k)
    result = math.atan(bk/ak)
    return (result)



