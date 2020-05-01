def digits_multiplication(number: int) -> int:
    # List Comprehension
    nonzero = [int(i) for i in list(str(number)) if int(i)>0]
    # Recursive Lambda
    mul = lambda pos: nonzero[0] if pos == 0 else nonzero[pos]*mul(pos-1)
    return mul(len(nonzero)-1)

if __name__ == '__main__':
    print('ElectronicStation - main()')
else:
    print('ElectronicStation - loading...')
