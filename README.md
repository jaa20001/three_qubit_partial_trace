# Three-Qubit Partial Trace Simulator

A Python project that implements the partial trace operation for a three-qubit quantum system using NumPy.

The main goal of this project is to understand how reduced density matrices are computed by implementing the partial trace operation directly, rather than relying on Qiskit's built-in `partial_trace()` function.

The project also includes a density matrix validation function to check whether an input matrix satisfies the mathematical conditions required for a valid quantum density matrix.

## 1. Project Overview

This project focuses on three-qubit quantum systems and provides the following functionalities:

- Construct three-qubit quantum states using Qiskit.
- Generate density matrices from statevectors.
- Implement the partial trace operation manually using NumPy.
- Trace out the third qubit (q0) to obtain a two-qubit reduced density matrix.
- Validate density matrices using Hermiticity, normalization, and positive semidefiniteness conditions.
- Reject invalid density matrices before performing the partial trace.

## 2. Mathematical Background

### 2.1 Density Matrix

For a pure quantum state, the density matrix is defined as

$$
\rho = |\psi\rangle\langle\psi|
$$

A three-qubit system has a Hilbert space of dimension

$$
2^3=8
$$

Therefore, its density matrix is an 8×8 complex matrix.

### 2.2 Partial Trace

The partial trace operation is used to obtain the reduced density matrix of a subsystem.

For a three-qubit system ABC, tracing out subsystem C gives

$$
\rho_{AB}=\operatorname{Tr}_C(\rho_{ABC})
$$

In the computational basis, its matrix elements are calculated using

$$
(\rho_{AB})_{ab,a'b'}=
\sum_{c=0}^{1}
(\rho_{ABC})_{abc,a'b'c}
$$

The basis indices are converted into NumPy array indices using

$$
\text{index}=4a+2b+c
$$

The resulting two-qubit density matrix uses

$$
\text{index}_{AB}=2a+b
$$

This project implements these equations using nested Python loops.

In Qiskit's state ordering, A corresponds to q2, B to q1, and C to q0. The implementation traces out q0.

## 3. Implementation

### Partial Trace Function

The function `partial_trace_C_3q(rho_abc)`:

- Accepts an 8×8 NumPy density matrix.
- Uses five nested loops to compute the partial trace over C.
- Returns the 4×4 reduced density matrix of subsystems A and B.

### Density Matrix Validation

The function `validate_density_matrix(rho_abc)` checks:

**1. Matrix Shape**

The input must be an 8×8 matrix.

**2. Hermiticity**

$$
\rho^\dagger=\rho
$$

**3. Normalization**

$$
\operatorname{Tr}(\rho)=1
$$

**4. Positive Semidefiniteness**

$$
\lambda_i\geq0
$$

All eigenvalues must be non-negative, allowing a small numerical tolerance.

The implementation uses `np.linalg.eigvalsh()` only after verifying the Hermiticity condition.

## 4. Test Cases

### Test 1: W State

The normalized three-qubit W state is

$$
|W\rangle=\frac{|001\rangle+|010\rangle+|100\rangle}{\sqrt3}
$$

After tracing out q0, the expected reduced density matrix is

$$
\rho_{AB}=\frac13
\begin{pmatrix}
1&0&0&0\\
0&1&1&0\\
0&1&1&0\\
0&0&0&0
\end{pmatrix}
$$

The density matrix passes validation, and the reduced density matrix is computed successfully.

### Test 2: Non-Normalized State

The following statevector is intentionally not normalized:

$$
|\psi\rangle=|000\rangle+|111\rangle
$$

Its corresponding outer-product matrix has

$$
\operatorname{Tr}(\rho)=2
$$

Therefore, the validation function returns `False`, and the partial trace is skipped.

### Test 3: Non-Hermitian Matrix

A valid density matrix is modified by changing one off-diagonal element without updating its conjugate counterpart.

The resulting matrix does not satisfy

$$
\rho^\dagger=\rho
$$

The validation function correctly rejects this matrix.

## 5. Requirements

- Python 3
- NumPy
- Qiskit

The project was developed using Python in Visual Studio on Windows.

## 6. Installation and Usage

Clone or download this repository and install the required libraries.

```bash
pip install numpy qiskit
```

Run the program:

```bash
python three_qubit_partial_trace.py
```

The program displays the density matrix validation results and the reduced density matrix for valid inputs.

## 7. Limitations

- The partial trace implementation is limited to three-qubit systems.
- Only the third qubit (q0) can be traced out.
- The validation function expects an 8×8 NumPy array.
- The project uses nested loops for educational purposes rather than performance optimization.
- The example script demonstrates selected valid and invalid inputs, but does not include a comprehensive automated test suite.

## 8. Learning Outcomes

Through this project, I practiced:

- Quantum density matrices and reduced quantum states
- Partial trace operations in composite Hilbert spaces
- Multidimensional index calculations
- NumPy array operations and nested loops
- Matrix eigenvalues and density matrix validation
- Function decomposition and basic input validation

This project is part of my ongoing study of quantum computing software engineering, with a focus on understanding and implementing the mathematical operations used in quantum simulation software.
