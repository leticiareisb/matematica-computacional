def implicacao(p, q):
    return not p or q

combinacoes = [
    {'P': True,  'Q': True,  'M': True},
    {'P': True,  'Q': True,  'M': False},
    {'P': True,  'Q': False, 'M': True},
    {'P': True,  'Q': False, 'M': False},
    {'P': False, 'Q': True,  'M': True},
    {'P': False, 'Q': True,  'M': False},
    {'P': False, 'Q': False, 'M': True},
    {'P': False, 'Q': False, 'M': False}
]

print(" P    Q    M    R    P→Q   P∨Q→R ¬P→(M→R)")
for combinacao in combinacoes:
    P = combinacao['P']
    Q = combinacao['Q']
    M = combinacao['M']
    
    P_implica_Q = implicacao(P, Q)
    
    R = P or Q
    P_ou_Q_implica_R = implicacao(P or Q, R)
    
    M_implica_R = implicacao(M, R)
    nao_P_implica_M_implica_R = implicacao(not P, M_implica_R)
    
    print(f"{P}  {Q}  {M}  {R}  {P_implica_Q}  {P_ou_Q_implica_R}  {nao_P_implica_M_implica_R}")
