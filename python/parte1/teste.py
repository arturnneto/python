def solution(number):
    soma = 0
    counter = 1
    
    while counter < number:
        if counter % 3 == 0 or counter % 5 == 0:
            soma += counter
        counter += 1
        
    return soma

print(solution(20))