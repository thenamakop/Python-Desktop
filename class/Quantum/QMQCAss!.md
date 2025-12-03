---
title: Bernstein–Vazirani (BV) Assignment — Viva & Presentation Prep
tags: [quantum, bv, oracle, qiskit]
date: 2025-12-03
---

# 1) Concept

- Goal: Discover a hidden $n$-bit string $s$ using one oracle call.
- Oracle: Returns $f_s(x) = s \cdot x \pmod 2$ (dot product mod 2). It answers “is the parity of the overlap of $x$ and $s$ equal to 1?”
- Trick: Prepare inputs in equal superposition, ask the oracle once, then apply Hadamards to decode all bits of $s$ at the same time.
- Result: Measuring yields $s$ directly, so the entire string is revealed with one query.

# 2) Circuit Construction

- Choose $n$ (example: $n=4$ or $n=6$) and fix $s$ (example: $n=4$, $s=1011$).
- Classical queries needed:
  - For $n=4$: 4 queries (ask each basis vector $e_i$ to read $s_i$).
  - For $n=6$: 6 queries.
- BV circuit (plain steps):

  - Qubits: $n$ input qubits plus 1 ancilla qubit.
  - First $H$ layer: puts inputs in superposition; ancilla prepared in $|1\rangle$ then $H$ to make $| - \rangle$ to record phase.
  - Oracle: CNOTs from input $i$ to ancilla for each $i$ where $s_i = 1$ (implements the parity function).
  - Second $H$ layer: decodes the phase on inputs back into the bits of $s$.
  - Measurement: measure input register → output is $s$.

- ASCII sketch (for $n=4$, $s=1011$):

```
|0> — H —●————— H ———— M   (q0, s0=1)
|0> — H ————●— H ———— M   (q1, s1=0)
|0> — H —●————— H ———— M   (q2, s2=1)
|0> — H —●————— H ———— M   (q3, s3=1)
|1> — H — Xor from marked inputs — H — (ancilla)
```

- Roles explained:
  - Number of qubits: $n$ inputs encode the $n$ bits of $s$; one ancilla stores parity.
  - First $H$ gates: build equal superposition so the oracle acts on all inputs at once; ancilla is set to $| - \rangle$ to capture phase.
  - Ancilla qubit: collects parity via controlled flips; it never needs to be read for the final answer.
  - Oracle/CNOTs: implement $f_s$ by toggling ancilla for each input bit that is 1 in $s$.
  - Second $H$ gates: convert encoded phases back to bit values on inputs.
  - Measurement: reading inputs yields $s$.

# 3) Programming Task

- Steps:

  - Build superposition on $n$ inputs; prepare ancilla in $| - \rangle$.
  - Apply CNOT from each input $i$ with $s_i=1$ onto ancilla.
  - Apply Hadamards to inputs; measure inputs.
  - Simulate with AerSimulator, shots ≥ 2000; most frequent outcome equals $s$.

- Qiskit code (n=4, s=1011):

```python
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

n = 4
s = "1011"
qc = QuantumCircuit(n + 1, n)
qc.h(range(n))
qc.x(n)
qc.h(n)
for i, b in enumerate(s):
    if b == "1":
        qc.cx(i, n)
qc.h(range(n))
qc.measure(range(n), list(range(n))[::-1])
sim = AerSimulator()
counts = sim.run(transpile(qc, sim), shots=4096).result().get_counts()
print(counts)
print("argmax:", max(counts, key=counts.get))
```

- Expected: `argmax` equals `1011`.

# Viva Quick Answers

- Why 1 query? Superposition + Hadamards decode all bits at once.
- How many classical queries? $n$.
- Do you measure ancilla? Not needed; input bits carry the answer.
- What if a bit of $s$ is 0? No CNOT from that input qubit.
- Why two $H$ layers? First builds parallelism; second decodes phase to bits.

# Slide Outline

- Problem: recover hidden $s$.
- Classical vs quantum queries.
- Circuit: inputs, ancilla, oracle, decode, measure.
- Demo result from Aer.
- Takeaway: BV recovers $s$ in one query.
