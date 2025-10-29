# [[file:EuanMendoza-problem-set-6.org::*Your Solution:][Your Solution::1]]
from classiq import *

# 4-qubits to represent 16 states
size = 4

# 16 possible vertices
N = 2**size
N_idx = N - 1


# Code from the lecture
@qfunc
def prepare_minus(aux: Output[QBit]):
    allocate(1, aux)
    X(aux)
    H(aux)


@qfunc
def diffuser_oracle(aux: QNum, x: QNum):
    aux ^= x != 0


@qfunc
def zero_diffuser(x: QNum):
    aux = QBit("aux")
    within_apply(lambda: prepare_minus(aux), lambda: diffuser_oracle(aux, x))


# Newer option to do the oracle and preparation within one line with control and phase
# Your Solution::1 ends here


# [[file:EuanMendoza-problem-set-6.org::*Your Solution:][Your Solution::2]]
@qfunc
def C_operator(vertices: QNum, adjacent_vertices: QNum):
    # 2^4 is 16 possible vertices
    for i in range(N):
        prob = N * [0]
        if i == 0:
            prob[1] = 1
        elif i == N_idx:
            prob[N_idx]
        else:
            prob[i - 1] = 0.5
            prob[i + 1] = 0.5
        print(i)
        print(prob)

        control(
            vertices == i,
            lambda: within_apply(
                lambda: inplace_prepare_state(
                    probabilities=prob, bound=0.01, target=adjacent_vertices
                ),
                lambda: zero_diffuser(adjacent_vertices),
            ),
        )


# Your Solution::2 ends here


# [[file:EuanMendoza-problem-set-6.org::*Your Solution:][Your Solution::3]]
@qfunc
def edge_oracle(res: Output[QBit], vertices: QNum, adjacent_vertices: QNum):
    res |= ((vertices + adjacent_vertices) % 2) == 1


@qfunc
def bitwise_swap(x: QArray[QBit], y: QArray[QBit]):
    for i in range(x.len):
        SWAP(x[i], y[i])


@qfunc
def S_operator(vertices: QNum, adjacent_vertices: QNum):
    res = QNum("res")
    edge_oracle(res, vertices, adjacent_vertices)
    control(res == 1, lambda: bitwise_swap(vertices, adjacent_vertices))
    free(res)


# Your Solution::3 ends here


# [[file:EuanMendoza-problem-set-6.org::*Your Solution:][Your Solution::4]]
@qfunc
def main(vertices: Output[QNum], adjacent_vertices: Output[QNum]):
    allocate(size, vertices)
    prob1 = N * [0]
    prob1[0] = 1
    inplace_prepare_state(probabilities=prob1, bound=0.01, target=vertices)

    prob2 = N * [0]
    prob2[1] = 1
    allocate(size, adjacent_vertices)
    inplace_prepare_state(probabilities=prob2, bound=0.01, target=adjacent_vertices)

    C_operator(vertices, adjacent_vertices)
    S_operator(vertices, adjacent_vertices)


qmod = create_model(main)
qprog = synthesize(qmod)

show(qprog)
# Your Solution::4 ends here
