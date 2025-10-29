# Your Solution:
# Follow the instructions in the #TODO comments in each snippet and insert
# your code to ensure the algorithms run correctly and produce the desired
# outcomes.

# 1. Create your general GHZ algorithm following these steps.

# Write your function here, leave the function name and signature as it
# is, and change the content of the function:


# [[file:EuanMendoza-problem-set-1.org::*Your Solution:][Your Solution::1]]
from classiq import *


@qfunc
def iterative_cx(reg: QArray):
    # X(reg[1]) #TODO: this is a placeholder operation so that the code in the notebook runs! change the contents to your contents!
    repeat(reg.len - 1, lambda i: CX(reg[i], reg[i + 1]))


# Your Solution::1 ends here


# #+RESULTS:

# Implement your =main= function here, declaring and initializing the
# =QArray= variable =reg= with \(8\) qubits, and performing any necessary
# preparation operations before invoking the =iterative_cx= function
# (Note: Your implementation should be general for any number of qubits.
# The =reg= variable is initiated to \(8\) qubits only to verify its
# correctness):


# [[file:EuanMendoza-problem-set-1.org::*Your Solution:][Your Solution::2]]
@qfunc
def main(reg: Output[QArray]):
    allocate(8, reg)  # Allocation

    H(reg[0])
    iterative_cx(reg)


# Creating the model
qmod = create_model(main)

# Synthesizing the model into a quantum program
qprog = synthesize(create_model(main))

# Displaying the circuit using the IDE’s visualization tool
show(qprog)
# Your Solution::2 ends here
