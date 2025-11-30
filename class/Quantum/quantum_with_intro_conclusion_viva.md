---
title: Optimizing Disk Defragmentation Using Quantum Computation — Viva Prep
tags: [quantum, grover, storage, defragmentation, qiskit]
date: 2025-11-30
---

# Overview

- Topic: Using Grover’s algorithm to speed up disk allocation/defragmentation.
- Problem: Filesystem fragmentation slows down reads/writes as blocks get scattered.
- Classical baseline: Best-Fit scans free blocks one-by-one → time $O(N)$.
- Quantum idea: Treat “find the right block” as a search problem; use Grover for $O(\sqrt{N})$.
- Outcome: A clear speedup in theory; practical limits today due to hardware maturity.

# Motivation

- As disks grow (TB → PB → EB), scanning all blocks becomes a bottleneck.
- Best-Fit tries to fit each file into the smallest suitable gap; over time it creates many tiny gaps (“checkerboard” fragmentation).
- Quantum parallelism evaluates all addresses at once and amplifies the best candidate.

# Classical Background (simple)

- Defragmentation: Move file parts to make them contiguous; fewer disk seeks → faster I/O.
- Heuristics:
  - First-Fit: pick the first gap that fits.
  - Best-Fit: pick the smallest gap that fits.
- Limits:
  - Sequential search → time $O(N)$.
  - Best-Fit often increases external fragmentation (many tiny unusable gaps).

# Quantum Approach (low-tech explanation)

- Idea: Put all possible block addresses into a single “cloud of possibilities” (superposition).
- Oracle: A check that flips the “right” address (the one that best fits) without touching the others.
- Diffuser: A mirror around the average; it boosts the flipped address and reduces others.
- After a few rounds, measuring gives the best address with high probability.

# Notation (for viva)

- Uniform superposition: $|s\rangle = \tfrac{1}{\sqrt{N}} \sum_{x=0}^{N-1} |x\rangle$.
- Oracle: $O|x\rangle = (-1)^{f(x)} |x\rangle$ (phase flip on marked item).
- Diffusion: $D = 2|s\rangle\langle s| - I$ (inversion about the mean).
- Grover iteration: $G = D\,O$; repeat about $\tfrac{\pi}{4}\sqrt{N}$ times.

# Circuit Steps (two-qubit example)

- Initialization: start at $|00\rangle$; apply $H$ to each qubit → equal weights over $\{|00\rangle,|01\rangle,|10\rangle,|11\rangle\}$.
- Oracle: for target $|11\rangle$, use `CZ` to flip its phase (others stay the same).
- Diffusion: sequence $H\otimes H \to X\otimes X \to CZ \to X\otimes X \to H\otimes H$.
- Measurement: read out the amplified answer.

# Mapping to Disk Allocation (simple)

- Address register: indices of free blocks, not the data itself.
- Oracle question: “Does this block meet the Best-Fit rule?” (e.g., larger than request, minimal leftover).
- Result: the best block gets its probability boosted; measurement returns that index.

# Simulation (from paper)

- Example map (KB): `[90, 50, 200, 10, 500, 120, 80, 105]`.
- File 1 (110KB): quantum picks block 5 → leftover 10KB.
- File 2 (45KB): noise may cause a wrong pick; retry yields correct block.
- Final map shows expected reductions; measurement distribution shows the amplified target.

# Comparison Snapshot

- Core algorithm: Classical linear scan vs quantum Grover search.
- Time: $O(N)$ vs $O(\sqrt{N})$.
- Fragmentation risk: higher for Best-Fit; lower when the truly optimal block is found.
- Bottlenecks: classical → I/O latency; quantum → hardware maturity (NISQ), qRAM, circuit depth.

# Practical Limits (today)

- NISQ devices: few noisy qubits; deep circuits struggle.
- qRAM: needed to load disk metadata quickly; still a research topic.
- Interface: moving data between OS and quantum hardware adds latency.
- Best use-case: hyperscale data centers where gains outweigh overhead.

# Intuition and Analogies

- Haystack analogy: classical search lifts one straw at a time; quantum briefly “sees” the whole haystack, then amplifies the correct straw.
- Mirror analogy (diffusion): flip around the average so the specially marked straw becomes most visible.

# Viva Q&A (short answers)

- What problem is solved? Faster finding of the right free block during allocation/defragmentation.
- Why is Best-Fit slow? It checks blocks sequentially; that scales linearly with disk size.
- What does Grover change? It reduces search time to $O(\sqrt{N})$ using amplitude amplification.
- What is the oracle? A rule checker that marks the block that best fits the request.
- What is diffusion? A balancing step that boosts the marked option and lowers others.
- Why not in production today? Hardware is noisy, limited in size; qRAM is not ready; software–hardware interface overhead.
- Where does it help? Very large systems where latency saves money and energy.

# Presentation Outline

- Problem framing: fragmentation and linear scans hurt performance.
- Classical heuristics: strengths and weaknesses (esp. Best-Fit).
- Quantum idea: superposition, oracle, diffusion — in plain terms.
- Circuit sketch: 2-qubit example and target $|11\rangle$.
- Simulation highlights: amplified correct block; occasional noise and retry.
- Limits and future: NISQ, qRAM, potential in hyperscale data centers.
- Takeaway: clear theoretical speedup; blueprint for future storage systems.

# Glossary (plain)

- Fragmentation: file pieces stored far apart; many seeks → slow.
- Superposition: a quantum state representing many possibilities at once.
- Oracle: a check that marks the correct option.
- Diffusion: a rebalancing step that boosts the marked option.
- Amplitude: how likely a state is to be measured.

# References (from paper)

- Grover (1996): database search algorithm.
- Preskill (2018): NISQ era discussion.
- qRAM (2008): concept of quantum memory for fast access.
- Filesystem works: Denning (1967), FFS (1984), modern fragmentation surveys.

# Talk Track (2–3 minutes)

- Start with the pain: scanning huge disks is slow and gets worse as they grow.
- Explain Best-Fit simply: it often creates tiny gaps that become unusable.
- Show the quantum shortcut: evaluate all blocks at once and amplify the best one.
- Emphasize the speedup: $O(N)$ → $O(\sqrt{N})$; less time spent searching.
- Acknowledge today’s limits: noisy qubits, missing qRAM; but promising for very large systems.
- Close with the vision: a practical path to smarter, faster storage allocation at scale.

