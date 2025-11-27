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