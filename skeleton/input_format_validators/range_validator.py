import sys, re
# exit code 99 = bad input, 42 = good input
def validate():

    line = sys.stdin.readline()
    if re.match('^(0|-?[1-9]\d*)( (0|-?[1-9]\d*))$', line) == None: return 99 # invalid n

    # if last char before newline is a space (i.e. trailing spaces exist)
    if line[-2] == ' ': return 99

    # check if line contains too many or too little spaces
    num_spaces = 0
    for c in line:
        if c == '\t': return 99
        if c == ' ': num_spaces += 1
    if num_spaces != 1: return 99 

    graph_dims = line.split(' ')
    # if number of tokens is not equal to expected amount
    if len(graph_dims) != 2: return 99
    
    # check for leading zeroes in tokens
    for s in graph_dims:
        if s[0] == '0': return 99

    n = int(graph_dims[0])
    # range check
    if(n < 2 or n > 100000): return 99
    m = int(graph_dims[1])
    # range check
    if(m < 1 or m > 200000): return 99

    for i in range(0, m):
        line = sys.stdin.readline()
        if re.match('^(0|-?[1-9]\d*)( (0|-?[1-9]\d*)){2}$', line) == None: return 99 # invalid n

        # if last char before newline is a space (i.e. trailing spaces exist)
        if line[-2] == ' ': return 99
        
        # check if line contains too many or too little spaces
        num_spaces = 0
        for c in line:
            if c == '\t': return 99
            if c == ' ': num_spaces += 1
        if num_spaces != 2: return 99

        edge = line.split(' ')
        # if number of tokens is not equal to expected amount
        if len(edge) != 3: return 99
        
        # check for leading zeroes in tokens
        for s in edge:
            if s[0] == '0': return 99

        n1 = int(edge[0])
        n2 = int(edge[1])
        d = int(edge[2])
        # range check
        if(n1 < 1 or n1 > n): return 99
        # range check
        if(n2 < 1 or n2 > n): return 99
        # if self-loop
        if(n1 == n2): return 99
        # range check
        if(d < 1 or d > 1000000000):
            if(d != -1): return 99

    line = sys.stdin.readline()
    if re.match('^(0|-?[1-9]\d*)( (0|-?[1-9]\d*))$', line) == None: return 99 # invalid n

    # if last char before newline is a space (i.e. trailing spaces exist)
    if line[-2] == ' ': return 99
    
    # check if line contains too many or too little spaces
    num_spaces = 0
    for c in line:
        if c == '\t': return 99
        if c == ' ': num_spaces += 1
    if num_spaces != 1: return 99 

    k_and_t = line.split(' ')
    # if number of tokens is not equal to expected amount
    if len(k_and_t) != 2: return 99

    # check for leading zeroes in tokens
    for s in k_and_t:
        if s[0] == '0': return 99

    k = int(k_and_t[0])
    # range check
    if(k < 1 or k > n-1): return 99
    t = int(k_and_t[1])
    # range check
    if(t < 1 or t > 1000000000): return 99

    line = sys.stdin.readline()
    if re.match('^(0|-?[1-9]\d*)( (0|-?[1-9]\d*)){%d,%d}$' % (k-1, k-1), line) == None: return 99 # invalid n
    
    # if last char before newline is a space (i.e. trailing spaces exist)
    if line[-1] == ' ': return 99
    if line[-1] != '\n': return 99
    
    # check if line contains too many or too little spaces
    num_spaces = 0
    for c in line:
        if c == '\t': return 99
        if c == ' ': num_spaces += 1
    if num_spaces != k-1: return 99

    destinations = line.split(' ')
    # if number of tokens is not equal to expected amount
    if len(destinations) != k: return 99

    # check for leading zeroes in tokens
    for s in destinations:
        if s[0] == '0': return 99

    d_map = {}

    # check if all delivery locations are distinct and not equal 1 and are within range 
    for i in range(0, k):
        if (int(destinations[i]) in d_map) or (int(destinations[i]) == 1) or (int(destinations[i]) > n or int(destinations[i]) < 1): return 99
        d_map[int(destinations[i])] = int(destinations[i])
    
    line = sys.stdin.readline()
    if line != '': return 99

    return 42

if __name__ == "__main__":
    sys.exit(validate())