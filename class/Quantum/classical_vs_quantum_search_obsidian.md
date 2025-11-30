---
title: Classical vs Quantum Search — Obsidian View
tags: [quantum, algorithms, grover, linear-search]
date: 2025-11-30
---

# Classical vs Quantum Search: Assignment Solutions

**Objective**

- Understand how classical and quantum algorithms solve the same search problem
- Compare their steps and computational complexity
- Provide simple, school-style algorithms and runnable programs

**1. Classical Linear Search**

**1a. Algorithm (with mathematical notation)**

- Input: a list $L = [a_0, a_1, \dots, a_{N-1}]$ of integers and a target $t \in \mathbb{Z}$
- Steps (school-style):
  1. Set $i \leftarrow 0$.
  2. While $i < N$:
     - Compare $a_i$ with $t$.
     - If $a_i = t$, output the index $i$ and stop.
     - Otherwise, set $i \leftarrow i + 1$ and continue.
  3. If the loop finishes without finding $t$, output "Not Found".
- Correctness: the algorithm outputs an index $i$ iff there exists $i \in \{0,\dots,N-1\}$ with $a_i = t$; else it reports "Not Found".
- Complexity: time $O(N)$, space $O(1)$.

**Mathematical Representation**

$$
\text{Problem: Given } L=(a_0,\dots,a_{N-1})\in\mathbb{Z}^N,\; t\in\mathbb{Z}.\\
\text{Goal: find } i^* \text{ s.t. } a_{i^*}=t \text{ or report } \bot.\\
i^* = \min\{ i\in[0,N-1]: a_i=t\}\;\text{ if set nonempty, else }\;\bot.\\
\text{Worst-case comparisons: } C(N)=N,\; \text{time } O(N),\; \text{space } O(1).
$$

**1b. Python Program**

```python
def linear_search(arr, t):
    for i in range(len(arr)):
        if arr[i] == t:
            return i
    return -1


if __name__ == "__main__":
    arr = [3, 5, 2, 9, 1, 7, 4]
    try:
        t = int(input("Enter target integer: "))
    except ValueError:
        print("Invalid input")
        raise SystemExit(1)

    idx = linear_search(arr, t)
    if idx != -1:
        print(f"Found at index {idx}")
    else:
        print("Not Found")
```

**2. Quantum Search — Grover’s Algorithm**

- Classical search complexity: $O(N)$
- Quantum search complexity: $O(\sqrt{N})$

**2a. Main Steps (simple, school-style)**

- Notation:
  - Uniform superposition $|s\rangle = \tfrac{1}{\sqrt{N}} \sum_{x=0}^{N-1} |x\rangle$
  - Oracle $O$: $O|x\rangle = (-1)^{f(x)} |x\rangle$ (phase flip on the marked item)
  - Diffusion $D = 2|s\rangle\langle s| - I$ (inversion about the mean)
- Steps:
  1. Initialization into equal superposition
     - Start from $|00\dots 0\rangle$ and apply Hadamard $H$ on each qubit so all basis states have equal amplitude.
  2. Oracle operation to mark the correct element
     - Apply a selective phase flip to the basis state $|x^*\rangle$ that encodes the target.
  3. Diffusion operator (amplitude amplification)
     - Reflect the amplitudes about their average to increase the marked state’s amplitude.
     - For 2 qubits: $H \otimes H \to X \otimes X \to CZ \to X \otimes X \to H \otimes H$.
  4. Measurement of the final state
     - Measure in the computational basis; the marked item appears with high probability after ≈ $\tfrac{\pi}{4}\sqrt{N}$ iterations.
- Two-qubit example ($N = 4$): target $|11\rangle$
  - Oracle: $CZ$ applies a $-1$ phase to $|11\rangle$.
- Diffusion: $H\otimes H, X\otimes X, CZ, X\otimes X, H\otimes H$.

**Mathematical Representation**

$$
|s\rangle = \tfrac{1}{\sqrt{N}}\sum_{x=0}^{N-1}|x\rangle,\quad O = I - 2|x^*\rangle\langle x^*|,\quad D = 2|s\rangle\langle s| - I,\quad G = D\,O.\\
\sin\theta = \tfrac{1}{\sqrt{N}},\quad G^k|s\rangle = \sin((2k+1)\theta)|x^*\rangle + \cos((2k+1)\theta)|x_\perp\rangle.\\
k_\text{opt} \approx \left\lfloor \tfrac{\pi}{4\theta} - \tfrac{1}{2} \right\rfloor \approx \left\lfloor \tfrac{\pi}{4}\sqrt{N} \right\rfloor,\; \text{queries } O(\sqrt{N}).\\
N=4 \Rightarrow \theta=\pi/6,\; k_\text{opt}=1.
$$

```mermaid
flowchart TD
    A[Start |00...0⟩] --> B[Apply H to each qubit \n Equal superposition]
    B --> C[Oracle: phase flip on |x*⟩]
    C --> D[Diffusion: invert about mean]
    D --> E[Measure]
```

**2b. Qiskit Program (2 qubits → 4 items)**

```python
from qiskit import QuantumCircuit, transpile


def grover_2_qubits():
    qc = QuantumCircuit(2, 2)
    qc.h([0, 1])
    qc.cz(0, 1)
    qc.h([0, 1])
    qc.x([0, 1])
    qc.cz(0, 1)
    qc.x([0, 1])
    qc.h([0, 1])
    qc.measure([0, 1], [0, 1])
    return qc


if __name__ == "__main__":
    qc = grover_2_qubits()
    try:
        from qiskit_aer import AerSimulator
        sim = AerSimulator()
        compiled = transpile(qc, sim)
        result = sim.run(compiled, shots=1024).result()
        counts = result.get_counts()
        print(counts)
    except Exception:
        print(qc.draw())
```

**References to Existing Materials**

- Classical algorithm notes: `class/quantum/linear_search_algorithm.txt`
- Grover steps notes: `class/quantum/grover_algorithm_steps.txt`
- Python scripts used: `class/quantum/linear_search.py`, `class/quantum/grover_qiskit.py`
