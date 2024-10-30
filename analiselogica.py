import itertools

def tabela_verdade():
    combinacoes = list(itertools.product([True, False], repeat=3))
    
    print(f"{'P':<5}{'Q':<5}{'M':<5}{'P → Q':<10}{'P ∨ Q':<10}{'M → R':<10}{'¬P':<10}{'¬P → (M → R)':<15}{'R':<5}")
    
    for P, Q, M in combinacoes:
        P_implica_Q = (not P) or Q
        P_ou_Q = P or Q
        M_implica_R = (not M) or P_ou_Q
        nao_P = not P
        nao_P_implica_M_implica_R = nao_P or M_implica_R
        R = (P or Q) or (nao_P and M_implica_R)
        
        print(f"{P!s:<5}{Q!s:<5}{M!s:<5}{P_implica_Q!s:<10}{P_ou_Q!s:<10}{M_implica_R!s:<10}{nao_P!s:<10}{nao_P_implica_M_implica_R!s:<15}{R!s:<5}")

tabela_verdade()
