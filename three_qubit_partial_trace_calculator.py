import numpy as np
from qiskit.quantum_info import Statevector , DensityMatrix, partial_trace

# 3 qubit test

# Test 1: W state
psi1 = Statevector(np.array([0, 1, 1, 0, 1, 0, 0, 0]) / np.sqrt(3))

# Test 2: non-Normalized state
psi2 = Statevector(np.array([1, 0, 0, 0, 0, 0, 0, 1]))

# Test 3: non-Hermitian Matrix
psi = Statevector(np.array([1, 0, 0, 0, 0, 0, 0, 0]))
rho_test = DensityMatrix(psi).data.copy()
rho_test[0, 1] = 0.2 # Deliberately changed to a non-Hermitian matrix


test = {"W_state" : psi1 , "non-Normalized state" : psi2}


def partial_trace_C_3q(rho_abc):
    rho_ab = np.zeros((4,4) , dtype=complex)

    for a in range(2):
        for a_prime in range(2):
            for b in range(2):
                for b_prime in range(2):
                    for c in range(2):
                        row = 4 * a + 2 * b + c
                        col = 4* a_prime + 2 * b_prime + c

                        rho_ab[2 * a + b , 2 * a_prime + b_prime] += rho_abc[row , col]
    return rho_ab



# validate density matrix (1.shape , 2.hermicity , 3.trace ,  4.semipositive of eigenvalues)
def validate_density_matrix(rho_abc, tol=1e-10):

    # check shape of Matrix
    if rho_abc.shape != (8,8):
        raise ValueError("The shape of Densitymatrix must be 8X8, Please Enter the 1X8 Statevector!")

    # Check Hermicity of matrix
    rho_abc_dagger = rho_abc.conj().T
  
    is_hermitian = np.allclose(rho_abc , rho_abc_dagger)

    if is_hermitian:
        # Check semipositive
        eigenvalues = np.linalg.eigvalsh(rho_abc)
        is_positive = np.all(eigenvalues >= -tol )

    else:
        is_positive = False

    # Check Trace is 1
    is_normalized = np.isclose(np.trace(rho_abc) , 1)

    
    is_valid = is_normalized and is_hermitian and is_positive
    
    return is_valid


for name , psi in test.items():
    rho_abc = (DensityMatrix(psi)).data

    is_valid = validate_density_matrix(rho_abc, tol=1e-10)
    
    if not is_valid:
        print("density matrix of" ,name, ": Invalid density matrix")
        continue 
    
    rho_ab = partial_trace_C_3q(rho_abc)

    print("result the Validation of DensityMatrix: " , is_valid)
    print("Partial trace (remove q0): ")
    print(rho_ab , "\n")


# Validation of Test3 DensityMatrix
print("result the Validation of DensityMatrix: " , validate_density_matrix(rho_test , tol=1e-10))
