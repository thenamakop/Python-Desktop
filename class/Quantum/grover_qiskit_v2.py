from math import sqrt, pi, floor
from qiskit import QuantumCircuit, transpile


def k_opt(n):
    N = 2 ** n
    return max(1, int(floor((pi / 4) * sqrt(N))))


def oracle_phase_flip(qc: QuantumCircuit, target_bits: str):
    n = len(target_bits)
    for i, b in enumerate(target_bits):
        if b == "0":
            qc.x(i)
    qc.h(n - 1)
    qc.mcx(list(range(n - 1)), n - 1, mode="noancilla")
    qc.h(n - 1)
    for i, b in enumerate(target_bits):
        if b == "0":
            qc.x(i)


def diffusion(qc: QuantumCircuit):
    n = qc.num_qubits
    qc.h(range(n))
    qc.x(range(n))
    qc.h(n - 1)
    qc.mcx(list(range(n - 1)), n - 1, mode="noancilla")
    qc.h(n - 1)
    qc.x(range(n))
    qc.h(range(n))


def grover_v2(n: int = 2, target: str | None = None, iterations: int | None = None):
    if target is None:
        target = "1" * n
    qc = QuantumCircuit(n, n)
    qc.h(range(n))
    if iterations is None:
        iterations = k_opt(n)
    for _ in range(iterations):
        oracle_phase_flip(qc, target)
        diffusion(qc)
    qc.measure(range(n), range(n))
    return qc


if __name__ == "__main__":
    qc = grover_v2(n=2, target="11")
    try:
        from qiskit_aer import AerSimulator
        sim = AerSimulator()
        compiled = transpile(qc, sim)
        result = sim.run(compiled, shots=1024).result()
        counts = result.get_counts()
        print(counts)
    except Exception:
        print(qc.draw())
