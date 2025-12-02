try:
    from qiskit import QuantumCircuit
except Exception:
    print("Qiskit not installed")
    raise SystemExit(1)

qc = QuantumCircuit(1)
qc.h(0)
qc.z(0)

try:
    fig = qc.draw('mpl')
    import matplotlib.pyplot as plt
    out = 'class/quantum/circuit_hz.png'
    fig.savefig(out, dpi=200, bbox_inches='tight')
    print(out)
except Exception:
    print(qc.draw())
