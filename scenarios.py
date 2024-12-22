from collections import namedtuple
from birds_solver import PlacementConstraint, AdjacencyConstraint, OrderConstraint, EdgeConstraint, solve

Scenario = namedtuple("Scenario", ['id', 'constraints', 'solution'])

scenarios = [
    Scenario(
        id=1,
        constraints=[
            PlacementConstraint('y', index=1),
            PlacementConstraint('r', index=0),
        ],
        solution=['r', 'y', 'b']
    ),
    Scenario(
        id=2,
        constraints=[
            PlacementConstraint('y', index=0),
            PlacementConstraint('r', index=2, inverted=True),
        ],
        solution=['y', 'r', 'b']
    ),
    Scenario(
        id=3,
        constraints=[
            PlacementConstraint('y', index=2),
            AdjacencyConstraint('y', 'r'),
        ],
        solution=['b', 'r', 'y']
    ),
    Scenario(
        id=4,
        constraints=[
            PlacementConstraint('b', index=0, inverted=True),
            AdjacencyConstraint('y', 'b', inverted=True),
        ],
        solution=['y', 'r', 'b']
    ),
    Scenario(
        id=5,
        constraints=[
            OrderConstraint('y', 'r'),
            PlacementConstraint('b', index=1),
        ],
        solution=['y', 'b', 'r']
    ),
    Scenario(
        id=6,
        constraints=[
            OrderConstraint('y', 'r'),
            PlacementConstraint('y', index=0, inverted=True),
        ],
        solution=['b', 'y', 'r']
    ),
    Scenario(
        id=7,
        constraints=[
            EdgeConstraint('y'),
            PlacementConstraint('r', index=2)
        ],
        solution=['y', 'b', 'r']
    ),
    Scenario(
        id=8,
        constraints=[
            EdgeConstraint('y', inverted=True),
            OrderConstraint('r', 'y')
        ],
        solution=['r', 'y', 'b']
    ),
    Scenario(
        id=9,
        constraints=[
            PlacementConstraint('b', index=0, inverted=True),
            EdgeConstraint('r', inverted=True)
        ],
        solution=['y', 'r', 'b']
    ),
    Scenario(
        id=10,
        constraints=[
            OrderConstraint('y', 'b'),
            OrderConstraint('r', 'y')
        ],
        solution=['r', 'y', 'b']
    ),
    Scenario(
        id=11,
        constraints=[
            OrderConstraint('b', 'r'),
            EdgeConstraint('y'),
            EdgeConstraint('b')
        ],
        solution=['b', 'r', 'y']
    ),
    Scenario(
        id=12,
        constraints=[
            EdgeConstraint('r'),
            PlacementConstraint('r', index=2, inverted=True),
            PlacementConstraint('b', index=1, inverted=True),
        ],
        solution=['r', 'y', 'b']
    ),
    Scenario(
        id=13,
        constraints=[
            OrderConstraint('b', 'y'),
            AdjacencyConstraint('y', 'r'),
            PlacementConstraint('y', index=1, inverted=True),
        ],
        solution=['b', 'r', 'y']
    ),
    Scenario(
        id=14,
        constraints=[
            EdgeConstraint('b'),
            PlacementConstraint('r', index=0, inverted=True),
            AdjacencyConstraint('b', 'y'),
        ],
        solution=['b', 'y', 'r']
    ),
    Scenario(
        id=15,
        constraints=[
            PlacementConstraint('y', index=2, inverted=True),
            AdjacencyConstraint('b', 'r'),
            AdjacencyConstraint('r', 'y'),
        ],
        solution=['y', 'r', 'b']
    ),
    Scenario(
        id=16,
        constraints=[
            AdjacencyConstraint('y', 'b'),
            AdjacencyConstraint('p', 'b', inverted=True),
            PlacementConstraint('p', index=2),
        ],
        solution=['b', 'y', 'p', 'r']
    ),
    Scenario(
        id=17,
        constraints=[
            PlacementConstraint('b', index=2),
            OrderConstraint('r', 'p'),
            EdgeConstraint('r', inverted=True),
        ],
        solution=['y', 'r', 'b', 'p']
    ),
    Scenario(
        id=18,
        constraints=[
            AdjacencyConstraint('r', 'p'),
            OrderConstraint('r', 'b'),
            PlacementConstraint('p', index=2)
        ],
        solution=['y', 'r', 'p', 'b']
    ),
    Scenario(
        id=60,
        constraints=[
            PlacementConstraint('b', index=0),
            AdjacencyConstraint('p', 'g'),
            AdjacencyConstraint('m', 'y', inverted=True),
            PlacementConstraint('y', index=1, inverted=True),
            OrderConstraint('r', 'm'),
            OrderConstraint('p', 'g'),
            EdgeConstraint('y', inverted=True),
            AdjacencyConstraint('p', 'y', inverted=True),
        ],
        solution=['b', 'p', 'g', 'y', 'r', 'm']
    ),
]

def main():
    success = True
    for scenario in scenarios:
        if (received := solve(num_birds=len(scenario.solution), constraints=scenario.constraints)) != scenario.solution:
            success = False
            print(f"SCENARIO {scenario.id} FAILED\n    Received: {received}\n    Expected: {scenario.solution}")

    if success:
        print("All scenarios succeeded")

if __name__ == '__main__':
    main()