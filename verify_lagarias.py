from mpmath import mp, euler, log, fadd, fmul, power, floor

# Use 40-digit precision and round-toward -∞
mp.dps = 40
mp.rounding = 'down'

# Hardcoded list of colossally abundant integers < 10^6
ca_numbers = [2, 6, 12, 60, 120, 360, 2520, 5040, 55440, 720720]

def harmonic(n):
    return fadd(euler + log(n), 1 / (2 * n))  # Upper bound for H_n

def F(n):
    H = harmonic(n)
    return fadd(H / n, fmul(power(mp.e, H), log(H)) / n)

def sigma(n):
    # Sum of divisors
    return sum(d for d in range(1, n + 1) if n % d == 0)

if __name__ == "__main__":
    print(" n       sigma(n)/n       F(n)       Gap")
    for n in ca_numbers:
        sigma_ratio = sigma(n) / n
        F_n = F(n)
        gap = F_n - sigma_ratio
        print(f"{n:<8} {sigma_ratio:.6f}     {F_n:.6f}     {gap:.6f}")
