# A8 orbit 4: four exact bad signatures for the fixed bridge templates

Date: 2026-11-01. ARIS proof-writer draft; independent review pending.

## Claim and status

Consider the residual hole geometry

$$v=0,\quad Z=\{15,23,27,29\},\quad W=\{1,2,4\}.$$

For each of the four cuts below, the fixed bridge template succeeds
unless either its fixed obstruction edge belongs to $F$, or the stated
restricted-edge signature holds. In the latter nonfixed case no choice
of endpoint pairing can make that template succeed.

**PROVABLE AS STATED**, relative to the accepted double/three-bridge
criterion and Q4 T15/T63 classification. This does not assert that some
cut always succeeds for every matching.

## Definitions and dependency map

For a cut bit $b$, put $A=\{x:x\mathbin\&b=0\}$ and $B=Q_5\setminus A$.
The selected bridge vertices in $B$ are $Y$. The possible obstruction
edge has endpoints $p,q$, and put $S=Y\cup\{p,q\}$. Bridge holes in
$A$ are their short mirrors, and are original minority holes.

| cut bit | $Y$ | $p,q$ | local completion |
|---:|---|---|---|
| 2 | $3,6$ | $10,18$ | T15 |
| 4 | $5,6$ | $12,20$ | T15 |
| 8 | $9,10,12$ | $8,24$ | T63 |
| 16 | $17,18,20$ | $16,24$ | T63 |

The two-bridge cuts have original $A$ holes of counts two and two;
consuming two minority holes leaves majority excess two. The three-bridge
cuts have three minority and two majority holes; consuming three minority
holes leaves two majority holes. Thus every target-face GQ4-avoid input
is valid. All bridge mirrors are covered by the residual nonadjacency
condition. The fixed local classifications and bridge criteria were
accepted in `A8_BRIDGE_INPUTS_REVIEW`.

## Exact nonfixed bad signature

When $pq\notin F$, the restricted-edge signature is:

1. Every original crossing edge has its $B$ endpoint in $S$.
2. Every bridge vertex in $Y$ that is internally matched in $B$ has its
   partner in $S$.

There is no restriction on an internal partner of $p$ or $q$ unless
that partner belongs to $Y$. These two conditions depend only on the
original matching, not on an $A$-face cycle or its short-edge choices.

## Proof

Build $G=F_B\cup C\cup\{\text{selected bridges}\}$ and let $T$ be
its $A$ endpoint set. Let $P$ pair the $T$--$T$ path components.
Every other component meeting $T$ has a unique terminal in $B$.
A terminal outside $\{p,q\}$ occurs exactly when either a crossing
port lies outside $S$, or an internally matched bridge has its partner
outside $S$. To justify this equivalence, a nonbridge crossing port
is itself a terminal, while an internal bridge leads through its
required matching edge to its partner unless the partner is another
bridge. The only permitted terminals in $S$ are $p,q$. These alternatives
exhaust every path leaving an endpoint in $T$.

Put $d=|T|/2$ and let $e=1$ if both $p,q$ are rooted terminals, $e=0$
otherwise. The sufficient bridge criterion is $d>|P|+e$.
If a terminal outside $\{p,q\}$ exists, the total number of rooted
terminals is even and exceeds $2e$. Therefore

$$2d-2|P|>2e,$$

which gives the sufficient strict inequality. The criterion constructs
a valid $A-v$ cycle whose compression avoids the classified local
obstruction, completing the required Q5 cycle.

If no such terminal exists, all terminals are contained in $\{p,q\}$.
Their number is zero or two, so $d=|P|+e$. Any endpoint matching from
an $A$ forest either closes a component, or joins the only two terminals
$p,q$ and produces exactly the classified obstruction edge. This is the
topological argument in `A8_TYPED_SPECTRUM_REPORT.md`, and it applies
to two bridges as well as three. Hence this fixed template cannot work.

If $pq\in F_B$, neither endpoint is a bridge vertex, so that fixed
edge remains unchanged by every compression. It is the T15 or T63
obstruction and directly blocks the local-completion template. This
proves the stated classification of the four templates.

## Machine-readable restrictions and remaining scope

`A8_orbit4_four_cut_bad_signatures.py` outputs the exact edge restrictions
in `A8_orbit4_four_cut_bad_signatures.json`. For each cut, it lists all
276 potential edges on the 24 covered vertices, dividing them into 164
allowed edges and 112 forbidden edges for the nonfixed bad signature.
A matching obeys that signature exactly when all its edges are allowed.

This is a compact input for studying joint failure: for every cut one
must have either its fixed obstruction edge or its restricted-edge
signature. The fixed edges $8\,24$ and $16\,24$ are mutually exclusive,
but that fact alone does not exclude joint restricted signatures.
No combined matching enumeration or claim of full orbit closure is
made in this file.
