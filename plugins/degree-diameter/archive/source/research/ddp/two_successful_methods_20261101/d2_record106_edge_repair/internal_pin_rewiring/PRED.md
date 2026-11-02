# Joint pin selection and internal old-edge repair

The minimal four-matching rule and all252 specified one-repair anchors have
failed for their recorded structural reasons. Change the actual generation
rule, rather than extending either enumeration. Use the same106-vertex
public max11,D2 source. Choose10 or11 pins S, append z adjacent exactly S,
and allow arbitrary deletion/addition ONLY inside the old induced graphG[S].
Keep every old edge with an endpoint outsideS unchanged.

Prediction: some such S and internal graph permit a full107-vertex max11,D2
graph. This is a falsifiable feasibility question, not a bad-pair objective.
For selected pins, both the newpoint coverage and old two-step paths must
hold simultaneously. Existing source validity is inherited, not rerun.

Binary x_v selectsS. Binary y_uv, constrained by y_uv<=x_u,x_v, gives final
internal adjacency. Closed domination is x_u+sum_{w in N_G(u)}x_w>=1:
selected degree10 source points are not incorrectly forced to have a pin
neighbor. Selected old degrees are

    deg_G(v)-sum_{w in N_G(v)}x_w+sum_w y_vw+1 <=11.

For every ordered old nonedge(v,u), impose

    (1-x_v)+x_u+sum_{w in N_G(v) intersect N_G(u)}(1-x_w)
        +sum_{w in N_G(u)}y_vw >=1.

Only v selected/u outside is substantive: an outside old common neighbor
retains its original route; an inside common neighbor must be joined to v
by its chosen internal edge. Both-selected pairs have common neighbor z,
and both-outside pairs retain every old two-step route. Closed domination
gives z-to-outside coverage because every cross edge is unchanged. Thus
the conditions are exact for this defined construction rule, not for all
possible107-vertex graphs or all source rewiring.

The local Moore count1+11*d implies every vertex in any107-point max11,D2
graph has degree>=10. Add this necessary lower-degree facet, as well as
10<=|S|<=11. Minimize the actual number of deleted plus added old edges:
with t_uv=x_u*x_v on the582 original edges, the objective is
sum_E t_uv-sum_E y_uv+sum_nonE y_uv. No other weighted score is used.

One new finite model/one solver call. Whole record106 case remains within
20CPU seconds including source acquisition, minimal4, one-repair anchors,
preparation and this run; use one thread, solver wall limit10 seconds and
hard process CPU19 seconds. No timer/seed restart. SAT returns the actual
pin set and internal edits, then one direct complete107 common-neighbor
and degree check. UNKNOWN is retained as unknown, not a family exclusion.
Only an actual valid graph may proceed to independent acceptance; counts
remain152/43/Lean45 until that happens.
