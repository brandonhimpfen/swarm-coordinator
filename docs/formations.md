# Formations

The initial release includes three formation helpers.

## Line Formation

`line_formation(anchor, count, spacing_m, axis="x")` returns a centered line of positions around an anchor point.

## Grid Formation

`grid_formation(anchor, count, spacing_m, columns=None)` returns a compact grid of positions.

## V Formation

`v_formation(anchor, count, spacing_m)` returns a leader-centered V formation.

## Assigning Formation Waypoints

Use `assign_formation_waypoints(agents, positions)` to convert formation positions into each agent's next waypoint.
