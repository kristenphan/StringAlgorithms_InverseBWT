# python3
import sys


def InverseBWT(bwt):
    '''
    Reconstructs a String from its Burrows-Wheeler Transform (BWT)
    Example:
    input (BWT) = 'TTCCTAACG$A'
    output (string) = 'TACATCACGT$'
    '''

    str = ''
    n = len(bwt)
    # create a dictionary bwt_d to store the indices of letters in bwt including the $ sign (0-based index)
    # and a list bwt_with_order that represents each letter in the bwt with its corresponding index in bwt
    bwt_d = {'A': [], 'C': [], 'G': [], 'T': [], '$': []}
    bwt_with_order = []
    indices = {'A': 0, 'C': 0, 'G': 0, 'T': 0, '$': 0} # keep track of the order of identical letters in the order of their appearance in bwt
    for i in range(n):
        let = bwt[i]
        bwt_d[let].append(i)
        bwt_with_order.append([let, indices[let]])
        indices[let] += 1

    # get the first column of the bwt matrix which is sorted lexicographically
    bwt_first_column = sorted(bwt_with_order)

    # start reconstructing the string using the first-last property of a BWT matrix
    # the start_idx points to the cyclic rotation that starts with the $ sign and ends with the first letter in the string
    # there is only one $ sign in a BWT
    start_idx = bwt_d['$'][0]

    for i in range(n):
        let, let_idx = bwt_first_column[start_idx]
        str += let
        next_let_idx = bwt_d[let][let_idx]
        start_idx = next_let_idx

    return str


# this program reads in the input that contains a string's Burrows-Wheeler Transform (BWT)
# and reconstructs the string
if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))
