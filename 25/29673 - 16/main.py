def f(n):
    """Возвращает  наибольший нетривиальный делитель числа,
    если число имеент ровно три нетривиальных делителя,
    в обратном случае возвращает False."""
    if int(n**0.25) == n**0.25 and is_prime(n**0.25):
        return int(n**0.75)


for n in range(123456789, 223456789+1):
    if f(n): 
        print(n, f(n))

"""
131079601 1225043
141158161 1295029
163047361 1442897
"""