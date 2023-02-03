def compute_pi(pat):
    M = len(pat)
    pi = [None] * M
    pi[0] = 0
    i = 1
    j = 0 #pat
    while i < M:
        if pat[i] == pat[j]:
            j += 1
            pi[i] = j
            i+=1
        else:
            if j != 0:
                j = pi[j-1]
            else:
                pi[i] = 0
                i += 1
            
    return pi

def kmp(txt, pat):
    # txt pointer
    i = 0
    # pat pointer
    j = 0
    n = len(txt)
    m = len(pat)
    pi = compute_pi(pat)
    while i < n:
        if txt[i] == pat[j]:
            i += 1
            j += 1
            if j == m:
                print(f"Pattern matched at i={i - j}")
                j = pi[j-1]
        else:
            if j!= 0:
                j = pi[j-1]
            else:
                i += 1
            
kmp("ABCDEABABAEDBABAA", "ABA")