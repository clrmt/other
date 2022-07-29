def solution(store, customer):
    return ['yes' if x in store else 'no' for x in customer]

store = [2,3,7,8,9]
customer = [7,5,9]
answer = solution(store, customer)
print(answer)