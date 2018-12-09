import sys, re
# exit code 99 = bad input, 42 = good input
def validate():

    line = sys.stdin.readline()
    if re.match('^(0|-?[1-9]\d*)( (0|-?[1-9]\d*))$', line) == None: return 1 # invalid n

    # if last char before newline is a space (i.e. trailing spaces exist)
    if line[-2] == ' ': return 2

    # check if line contains too many or too little spaces
    num_spaces = 0
    for c in line:
        if c == '\t': return 3
        if c == ' ': num_spaces += 1
    if num_spaces != 1: return 4 

    graph_dims = line.split(' ')
    # if number of tokens is not equal to expected amount
    if len(graph_dims) != 2: return 5
    
    # check for leading zeroes in tokens
    for s in graph_dims:
        if s[0] == '0': return 6

    n = int(graph_dims[0])
    # range check
    if(n < 2 or n > 100000): return 7
    m = int(graph_dims[1])
    # range check
    if(m < 1 or m > 200000): return 8

    for i in range(0, m):
        line = sys.stdin.readline()
        if re.match('^(0|-?[1-9]\d*)( (0|-?[1-9]\d*)){2}$', line) == None: return 9 # invalid n

        # if last char before newline is a space (i.e. trailing spaces exist)
        if line[-2] == ' ': return 10
        
        # check if line contains too many or too little spaces
        num_spaces = 0
        for c in line:
            if c == '\t': return 11
            if c == ' ': num_spaces += 1
        if num_spaces != 2: return 12

        edge = line.split(' ')
        # if number of tokens is not equal to expected amount
        if len(edge) != 3: return 13
        
        # check for leading zeroes in tokens
        for s in edge:
            if s[0] == '0': return 14

        n1 = int(edge[0])
        n2 = int(edge[1])
        d = int(edge[2])
        # range check
        if(n1 < 1 or n1 > n): return 15
        # range check
        if(n2 < 1 or n2 > n): return 16
        # if self-loop
        if(n1 == n2): return 17
        # range check
        if(d < 1 or d > 1000000000):
            if(d != -1): return 18

    line = sys.stdin.readline()
    if re.match('^(0|-?[1-9]\d*)( (0|-?[1-9]\d*))$', line) == None: return 19 # invalid n

    # if last char before newline is a space (i.e. trailing spaces exist)
    if line[-2] == ' ': return 20
    
    # check if line contains too many or too little spaces
    num_spaces = 0
    for c in line:
        if c == '\t': return 21
        if c == ' ': num_spaces += 1
    if num_spaces != 1: return 22 

    k_and_t = line.split(' ')
    # if number of tokens is not equal to expected amount
    if len(k_and_t) != 2: return 23

    # check for leading zeroes in tokens
    for s in k_and_t:
        if s[0] == '0': return 24

    k = int(k_and_t[0])
    # range check
    if(k < 1 or k > n-1): return 25
    t = int(k_and_t[1])
    # range check
    if(t < 1 or t > 1000000000): return 26

    line = sys.stdin.readline()
    if re.match('^(0|-?[1-9]\d*)( (0|-?[1-9]\d*)){%d,%d}$' % (k-1, k-1), line) == None: return 27 # invalid n
    
    # if last char before newline is a space (i.e. trailing spaces exist)
    if line[-1] == ' ': return 28
    if line[-1] != '\n': return 29
    
    # check if line contains too many or too little spaces
    num_spaces = 0
    for c in line:
        if c == '\t': return 30
        if c == ' ': num_spaces += 1
    if num_spaces != k-1: return 31

    destinations = line.split(' ')
    # if number of tokens is not equal to expected amount
    if len(destinations) != k: return 32

    # check for leading zeroes in tokens
    for s in destinations:
        if s[0] == '0': return 33

    d_map = {}

    # check if all delivery locations are distinct and not equal 1 and are within range 
    for i in range(0, k):
        if (int(destinations[i]) in d_map) or (int(destinations[i]) == 1) or (int(destinations[i]) > n or int(destinations[i]) < 1): return 34
        d_map[int(destinations[i])] = int(destinations[i])
    
    line = sys.stdin.readline()
    if line != '': return 35

    return 42

if __name__ == "__main__":
    sys.exit(validate())