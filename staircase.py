import numpy as np

'''
k # minimum number of shared needed to decode
z # number of colluding workers, z<k
m # number of rows of the matrix
l # number of columns of the matrix
h
n # number of workers


encoding:
- Divide the rows of A into b(k-z) blocks, each of dimension m/(b(k-z))
- Encode these blocks into n shares of dimension m/(k-z)
- d_i, where d_1=n, d_2=n-1, d_h=k is the number of workers contacted.
- b_i=d_i-z
- The data matrices are arranged in the matrix S.
- Secrecy is ensured via the zb R_1, ..., R_zb matrices, whose elements are random.
- R_1, ..., R_zb are partitioned into h matrices.

'''

class Model(object):
    def __init__(self, m, l, k, n, z):
        self.m = m
        self.l = l
        self.k = k
        self.n = n
        self.z = z
        return

    @property
    def h(self):
        return self.n-self.k+1

    @property
    def b(self):
        start = self.k-self.z+1
        stop = self.n-self.z
        step = 1
        if start > stop:
            step = -1
        l = np.arange(start, stop+step, step)
        return lcm_iter(l)

    def __repr__(self):
        return str(self.asdict())

    def asdict(self):
        return {
            "m": self.m,
            "l": self.l,
            "k": self.k,
            "n": self.n,
            "z": self.z,
            "h": self.h,
            "b": self.b,
        }

def alphad(M, d):
    return (M.k-M.z) / (d-M.z)

def d_i(M, i):
    assert 1 <= i <= M.h
    return M.n-i+1

def b_i(M, i):
    if i == 0:
        return 1
    return d_i(M, i) - M.z

def num_submatrices(M):
    return M.b*(M.k-M.z)

def num_random(M):
    return M.z*M.b

def lcm_iter(l, i=0, v=1):
    '''least common multiple of all elements in l'''
    assert len(l) > 0, "lcm needs at least 1 element"
    if i == len(l):
        return v
    v = lcm(v, l[i])
    return lcm_iter(l, i+1, v)

def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return int(a * b / gcd(a, b))

def S_size(M):
    b1 = b_i(M, 1)
    b = M.b
    rows = b1*M.m / (M.k-M.z) / b
    cols = M.l*(M.k-M.z)*b/b1
    return rows, cols

def R_size(M):
    b = M.b
    rows = M.m/(b*(M.k-M.z))
    cols = M.l
    return rows, cols

def Rr_size(M, i):
    b = M.b
    rows = M.z*M.m/(b*(M.k-M.z))
    cols = M.l*(M.k-M.z)*b/(b_i(M, i)*b_i(M, i-1))
    return rows, cols

# m = 20
# l = 10
# k = 6
# n = 9
# z = 1

# typo on page 8. should be LCM{k-z+1, ..., n-z}

def main():
    m = 1
    l = m

    n, k, z = 3, 2, 1
    # n, k, z = 20, 10, 2

    M = Model(m, l, k, n, z)
    print("parameters:")
    print(M)
    d = k
    print("submatrices:", num_submatrices(M))
    print("random matrices:", num_random(M))
    print("size of S:", S_size(M))
    print("size of R:", R_size(M))

    for i in range(1, M.h+1):
        print("Size of R_{}:".format(i), Rr_size(M, i))

if __name__ == '__main__':
    main()
