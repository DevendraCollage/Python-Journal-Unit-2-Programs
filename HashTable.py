# Hash Table Demo In Python
# Accessing Values of Dictionary

def hash_key(key, i):
    return key % i


i = 7
print(f'The Hash value for 3 is{hash_key(3,1)}')
print(f'The Hash value for 2 is{hash_key(2,1)}')
print(f'The Hash value for 9 is{hash_key(9,1)}')
print(f'The Hash value for 11 is{hash_key(11,1)}')
print(f'The Hash value for 7 is{hash_key(7,1)}')


"""
Output :
The hash value For 3 is 3
The hash value For 2 is 2
The hash value For 9 is 2
The hash value For 11 is 4
The hash value For 7 is 0
"""
