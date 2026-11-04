# Matchings of five directions in hypercube extends to Hamilton cycles and paths with prescribed ends

This repository contains supplementary materials for the research paper *Matchings of five directions in hypercube extends to Hamilton cycles and paths with prescribed ends* by Jiřı́ Fink and Vojtěch Hotmar which is currently under review process. The preprint version of the paper is available on arxiv (TODO). More information about this repository is also available in the [master thesis](thesis.pdf) by Vojtěch Hotmar.

All runtimes in this readme were measured on Apple MacBook M3 MAX.

## Prerequisites

### Automatic Installation (Ubuntu 24.10)

```bash
# Install core dependencies
sudo snap install zig --beta --classic             # zig
sudo apt install make                              # make
sudo apt install clang                             # clang
curl https://sh.rustup.rs -sSf | sh                # cargo
```

### Manual Installation

Required tools:

- zig 0.13.0 ([installation guide](https://ziglang.org/learn/getting-started/))
- cargo ([installation guide](https://doc.rust-lang.org/cargo/getting-started/installation.html))

## Building the Project

From the root directory:

```bash
# Setup dependencies
git clone --depth 1 --branch rel-2.1.2 https://github.com/arminbiere/cadical.git

# Build cadical
cd cadical && CXX="zig c++" ./configure && make -j 8 && cd ..

# Build zig components
cd hyper_cube_generation && zig build --release=fast && cd ..

# Build rust components
cd hyper_cube_verification && cargo build --release && cd ..
```

## Usage

### Generating Maximal Matchings

Output format: `n e₁ e₂ ... eₙ`

- `n`: number of edges
- `eᵢ`: edge representation (direction = remainder(eᵢ/dim), endpoints derived from quotient binary representation)

#### SAT Solver Method (6-hour runtime for dimension 5)

```bash
./hyper_cube_generation/zig-out/bin/generate_maximal_matchings -d <dim> [-t <threads>] [-o]
```

Parameters:

- `dim`: dimension (2-5)
- `threads`: number of threads to run on
- `-o`: optional flag to avoid vertex 0

#### Fast Implementation

```bash
./hyper_cube_verification/target/release/hyper_cube_bin generate-maximal-matchings-up-to-isomorphism -d <dim>
```

Parameters:

- `dim`: dimension (2+)

### Conjecture Verification

Output format: `n e₁ e₂ ... eₙ f a₁ b₁ a₂ b₂ ... aₖ bₖ`

- `n`: edges count
- `eᵢ`: edge representations
- `f`: failed terminal vertex pair count
- `aᵢ bᵢ`: failed vertex pairs

#### Zero-Omitting Path Conjecture (n ∈ {2,...,5})

```bash
# Batch verification
for dim in {2..5}; do
    ./hyper_cube_verification/target/release/hyper_cube_bin test-all-matchings-for-simple-hamilton-path -d $dim -o > omit_zero_results_$dim
done

# Matching file verification
cat matchings | ./hyper_cube_verification/target/release/hyper_cube_bin test-all-matchings-for-simple-hamilton-path -d <dim> --stdin
```

Runtime: Under 1 minute

#### General Path Conjecture (n=5)

```bash
# Full verification
./hyper_cube_verification/target/release/hyper_cube_bin test-all-matchings-for-hamilton-path-and-one-vertex-with-at-least-two-possibilities -d 5 > results_5

# Extract failed paths
cat results_5 | awk '{if ($NF != 0) print $0}' > results_5_failed

# Test subsets (by iteratively removing edges from matchings that have still vertex pair that can't be extended)
cat results_5_failed | ./hyper_cube_verification/target/release/hyper_cube_bin test-matchings-for-first-subset-allowing-all -d 5
```

Runtime: ~3 minutes for verification, ~20 minutes for subset testing
