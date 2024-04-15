def get_bin_values(n):
    bin_values = []
    for i in range(2**n):
        bin_values.append(format(i, f'0{n}b'))
    return bin_values

def get_minterms(n):
    minterms = []
    while True:
        minterm = input("Enter a minterm in binary (or 'done' to finish): ")
        if minterm.lower() == 'done':
            break
        minterms.append(minterm)
    return minterms

def karnaugh_minimization(n, minterms):
    # Generate all possible binary values for n variables
    bin_values = get_bin_values(n)
    
    # Create a Karnaugh map
    k_map = {}
    for value in bin_values:
        k_map[value] = 0 if value in minterms else 1
    
    # Find groups of 1s in the Karnaugh map
    groups = []
    for i in range(n):
        group = []
        for value, bit in k_map.items():
            if value.count('1') == i+1 and bit == 1:
                group.append(value)
        if group:
            groups.append(group)
    
    # Perform grouping and find essential prime implicants
    prime_implicants = []
    for group in groups:
        for value in group:
            if k_map[value] == 1:
                prime_implicants.append(value)
                for i in range(n):
                    value_list = list(value)
                    if value_list[i] == '1':
                        value_list[i] = '-'
                        neighbor = ''.join(value_list)
                        if neighbor in k_map:
                            k_map[neighbor] = 0
    
    return prime_implicants

def main():
    n = int(input("Enter the number of variables in the logical function: "))
    minterms = get_minterms(n)
    
    prime_implicants = karnaugh_minimization(n, minterms)
    
    print("Minimized logical function:")
    print(" + ".join(prime_implicants))

if __name__ == "__main__":
    main()
