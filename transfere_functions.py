import control as ctl
from sympy import zeros, Matrix, Poly, symbols, expand


def get_G1():
    '''Calcola la funzione di trasferimento G1(s). Return G1(s)'''
    m_s = 2500
    m_u = 320
    k_s = 80000
    k_u = 500000
    c_s = 350
    c_u = 15020

    nump = [(m_s + m_u), c_u, k_u]
    denp = [(m_s * m_u), (m_s * (c_s + c_u)) + (m_u * c_s), (m_s * (k_s + k_u)) + (m_u * k_s) + (c_s * c_u),
            (c_s * k_u) + (c_u * k_s), k_s * k_u]
    return ctl.tf(nump, denp)


def get_G2():
    '''Calcola la funzione di trasferimento G2(s). Return G2(s)'''
    # i parametri del sistema
    m_s = 2500
    m_u = 320
    k_s = 80000
    k_u = 500000
    c_s = 350
    c_u = 15020

    # il numeratore
    num_s = [-(m_s * c_u), -(m_s * k_u), 0, 0]
    # il denumeratore
    den1 = [(m_s * m_u), (m_s * (c_s + c_u)) + (m_u * c_s), (m_s * (k_s + k_u)) + (m_u * k_s) + (c_s * c_u),
            (c_s * k_u) + (c_u * k_s), k_s * k_u]
    return ctl.tf(num_s, den1)


def get_R(G1=get_G1()):
    '''Calcola la funzione di trasferimento del controllore R(s). Risolve l'equazione Diofantina impostata nella forma
    di un sistema lineare. Return R(s)'''
    E_den = Matrix(G1.den[0][0])
    E_num = Matrix(G1.num[0][0])

    # controlla il padding del sistema. Se il padding è < 0 allora il sistema lineare è da contollare manualmente  
    dif_shape = E_den.shape[0] - E_num.shape[0]
    if dif_shape < 0:
        exit()

    # inserire il padding
    E_num = E_num.row_insert(0, zeros(dif_shape, 1))

    # ceare la matrice E dei coefficienti di G1(s)
    E = Matrix([])
    for i in range(4):
        col = zeros(i, 1).col_join(E_den.col_join(zeros(3 - i, 1)))
        E = E.col_insert(i, col)
    for i in range(4):
        col = zeros(i, 1).col_join(E_num.col_join(zeros(3 - i, 1)))
        E = E.col_insert(i + 5, col)

    # recuperare il polinomio prestabilito C(s)
    c_funzione = Poly(get_poly_prestabilito())

    # inserire i coefficienti del polinomio C(s) nel vettore colonna B
    B_vector = Matrix([])
    B_vector = B_vector.col_insert(0, c_funzione.all_coeffs())

    # risolvere il sistema lineare "E W = B"
    W_vector = E.solve(B_vector)

    # estrarre i coefficienti del numeratore e del denumeratore dal vettore W in due vettori separati
    W_list_num = []
    W_list_den = []
    for i in range(4):
        W_list_den.append(float(W_vector[i, 0]))
    for i in range(4):
        W_list_num.append(float(W_vector[4 + i, 0]))

    # creazione della funzione di trasferimento R(s)
    return ctl.tf(W_list_num, W_list_den)


def get_M_s():
    '''Calcola la funzione di trasferimento M(s). Return M(s)'''
    return get_G2() / (1 + get_L_s())


def get_L_s():
    '''Calcola la funzione di trasferimento L(s) dopo aver sintetizzato il controllore R(s) . Return L(s)'''
    G1 = get_G1()
    R = get_R(G1)
    return G1 * R * 15


def get_poly_prestabilito():
    '''Crea il polinomio prestabilito secondo le specifiche di progetto. Return C(s)'''
    s = symbols('s')
    p = 1
    p *= (s + 5) ** 1
    p *= (s + 40) ** 2
    p *= (s + 20) ** 2
    p *= (s + 30) ** 2
    return expand(p)
