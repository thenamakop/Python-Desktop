# Classical vs Quantum Search

This document consolidates the classical linear search and Grover’s quantum search algorithms, including annotated steps and runnable example programs.

---

## 1. Classical Linear Search

### 1a. Algorithm (with mathematical notation)

Given an input list \( L = [a_0, a_1, \dots, a_{N-1}] \) of integers and a target \( t \in \mathbb{Z} \).

Algorithm:
1. For \( i = 0, 1, \dots, N-1 \):
   - If \( a_i = t \), output \( i \) and halt.
2. If no \( i \) satisfies \( a_i = t \), output "Not Found".

Correctness:
- Halts with index \( i \) iff \( \exists i \in \{0, \dots, N-1\} \) such that \( a_i = t \).
- Otherwise, after examining all elements, reports "Not Found".

Complexity:
- Time: \( O(N) \) comparisons in the worst case.
- Space: \( O(1) \) auxiliary space.

### 1b. Python Program (annotated)

Source: `class/quantum/linear_search.py` (see `class/quantum/linear_search.py:1` for `linear_search` definition)

```python
# Linear search over a list of integers.
# Compares each element a_i against target t and returns the index if found.

def linear_search(arr, t):
    # Iterate through all indices i = 0 .. N-1
    for i in range(len(arr)):
        # Mathematical comparison: a_i == t
        if arr[i] == t:
            return i  # Output index i and halt
    return -1  # If no match, indicate Not Found via -1


if __name__ == "__main__":
    # Example list of integers
    arr = [3, 5, 2, 9, 1, 7, 4]
    try:
        # User input for the target element
        t = int(input("Enter target integer: "))
    except ValueError:
        print("Invalid input")
        raise SystemExit(1)

    # Perform the search
    idx = linear_search(arr, t)
    if idx != -1:
        print(f"Found at index {idx}")
    else:
        print("Not Found")
```

Usage:
- Run: `python class/quantum/linear_search.py`
- Enter an integer when prompted; the program prints the index or "Not Found".

---

## 2. Quantum Search — Grover’s Algorithm

### 2a. Main Steps and Intuition

Goal: Find \( x^* \) such that \( f(x^*) = 1 \) among \( N \) items with \( O(\sqrt{N}) \) queries.

Notation:
- Uniform superposition: \( |s\rangle = \tfrac{1}{\sqrt{N}} \sum_{x=0}^{N-1} |x\rangle \)
- Oracle \( O \): \( O|x\rangle = (-1)^{f(x)} |x\rangle \) (phase flip on marked state)
- Diffusion: \( D = 2|s\rangle\langle s| - I \) (inversion about the mean)

Steps:
1. Initialization into equal superposition
   - Start in \( |0\dots 0\rangle \).
   - Apply Hadamard \( H \) to each qubit: \( |\psi_0\rangle = |s\rangle \).

   Simple diagram (2 qubits): applying `H` on both qubits spreads amplitude over all 4 basis states
   ```
   |00> — H —
   |01> — H —   → { |00>, |01>, |10>, |11> } each with equal amplitude
   |10> — H —
   |11> — H —
   ```

2. Oracle operation (mark the correct element)
   - Selective phase flip on target \( |x^*\rangle \).
   - Effect: amplitude of \( |x^*\rangle \) becomes negative relative to others.

3. Diffusion operator (amplitude amplification)
   - Reflect state about average amplitude: \( D = 2|s\rangle\langle s| - I \).
   - Increases amplitude of the marked state, decreases others.
   - For 2 qubits, one implementation sequence: `H⊗H → X⊗X → CZ → X⊗X → H⊗H`.

4. Measurement of the final state
   - Measure in computational basis.
   - With approximately \( \lfloor \tfrac{\pi}{4}\sqrt{N} \rfloor \) iterations, marked item appears with high probability.

Two-qubit example (\( N = 4 \)):
- Target state: \(|11\rangle\).
- One Grover iteration is typically sufficient; measurement yields `11` with near-unit probability under ideal conditions.

### Complexity Comparison
- Classical search: \( O(N) \)
- Quantum search (Grover): \( O(\sqrt{N}) \)

### 2b. Qiskit Program (annotated, 2 qubits)

Source: `class/quantum/grover_qiskit.py`

```python
from qiskit import QuantumCircuit, transpile


def grover_2_qubits():
    # 2-qubit circuit with 2 classical bits for measurement
    qc = QuantumCircuit(2, 2)

    # 1) Initialization: H on each qubit to create uniform superposition |s>
    qc.h([0, 1])

    # Oracle for target |11>: controlled-Z applies a phase flip only to |11>
    qc.cz(0, 1)

    # 2) Diffusion (amplitude amplification): H, X, CZ, X, H
    qc.h([0, 1])
    qc.x([0, 1])
    qc.cz(0, 1)
    qc.x([0, 1])
    qc.h([0, 1])

    # 3) Measurement in computational basis
    qc.measure([0, 1], [0, 1])
    return qc


if __name__ == "__main__":
    qc = grover_2_qubits()
    try:
        # If Aer is available, simulate and print counts
        from qiskit_aer import AerSimulator
        sim = AerSimulator()
        compiled = transpile(qc, sim)
        result = sim.run(compiled, shots=1024).result()
        counts = result.get_counts()
        print(counts)  # Expect dominant '11'
    except Exception:
        # Fallback: print ASCII diagram of the circuit
        print(qc.draw())
```

How to run:
- Install Qiskit Aer (optional for simulation): `pip install qiskit qiskit-aer`
- Execute: `python class/quantum/grover_qiskit.py`
- Expected result: counts dominated by `'11'` after one Grover iteration.

---

## References (file paths)
- Classical algorithm steps: `class/quantum/linear_search_algorithm.txt`
- Classical Python program: `class/quantum/linear_search.py` (function at `class/quantum/linear_search.py:1`)
- Grover steps: `class/quantum/grover_algorithm_steps.txt`
- Qiskit program: `class/quantum/grover_qiskit.py` (circuit built at `class/quantum/grover_qiskit.py:4`)

---

## Summary
- Demonstrated classical linear search with \( O(N) \) complexity and a simple Python implementation.
- Explained Grover’s algorithm’s four components and provided a 2-qubit Qiskit implementation achieving \( O(\sqrt{N}) \) query complexity.