from qiskit import QuantumCircuit, transpile


def make_simple_circuit(n=2):
    qc = QuantumCircuit(n, n)
    qc.h(range(n))
    if n >= 2:
        qc.cx(0, 1)
    qc.measure(range(n), range(n))
    return qc


if __name__ == "__main__":
    qc = make_simple_circuit(2)
    try:
        from qiskit_aer import AerSimulator
        sim = AerSimulator()
        compiled = transpile(qc, sim)
        result = sim.run(compiled, shots=512).result()
        print(result.get_counts())
    except Exception:
        print(qc.draw())
