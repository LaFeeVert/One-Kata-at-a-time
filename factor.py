def factor(num):
    solution = []
    if num > 1:
        for divisor in range (2, num+1):
            while num % divisor == 0:
                solution.append(divisor)
                num //= divisor
    return solution

# def factor(num):
#     solution = []
#     if num <= 1:
#         return solution
#     for divisor in range(2, num+1):
#         while num % divisor == 0:
#             solution.append(divisor)
#             num //= divisor
#     return solution

# def factor(num):
#     solution = []
#     if num > 1:
#         divisor = 2
#         while divisor <= num:
#             while num % divisor == 0:
#                 solution.append(divisor)
#                 num //= divisor
#             divisor += 2 if divisor % 2 else 1    
#     return solution