from math import sqrt, pi, floor
from qiskit import QuantumCircuit, transpile


def k_opt_from_n(n):
    N = 2 ** n
    return max(1, int(floor((pi / 4) * sqrt(N))))


def apply_oracle_two_qubits(qc, target):
    if target == "11":
        qc.cz(0, 1)
        return
    if target == "00":
        qc.x([0, 1])
        qc.cz(0, 1)
        qc.x([0, 1])
        return
    if target == "01":
        qc.x(0)
        qc.cz(0, 1)
        qc.x(0)
        return
    if target == "10":
        qc.x(1)
        qc.cz(0, 1)
        qc.x(1)
        return
    raise ValueError("target must be one of '00','01','10','11'")


def apply_diffusion_two_qubits(qc):
    qc.h([0, 1])
    qc.x([0, 1])
    qc.cz(0, 1)
    qc.x([0, 1])
    qc.h([0, 1])


def grover_two_qubits(target="11", iterations=None):
    qc = QuantumCircuit(2, 2)
    qc.h([0, 1])
    if iterations is None:
        iterations = k_opt_from_n(2)
    for _ in range(iterations):
        apply_oracle_two_qubits(qc, target)
        apply_diffusion_two_qubits(qc)
    qc.measure([0, 1], [0, 1])
    return qc


if __name__ == "__main__":
    qc = grover_two_qubits(target="11")
    try:
        from qiskit_aer import AerSimulator
        sim = AerSimulator()
        compiled = transpile(qc, sim)
        result = sim.run(compiled, shots=1024).result()
        print(result.get_counts())
    except Exception:
        print(qc.draw())
