from functools import reduce

def range_without(length, to_remove):
    return (i for i in range(length) if i != to_remove)

class PlacementConstraint:
    def __init__(self, bird, index, inverted=False):
        self._bird = bird
        self._index = index
        self._inverted = inverted

    def possible_solutions(self, num_birds):
        solutions = []
        solution_indices = [self._index] if not self._inverted else range_without(num_birds, self._index)
        for i in solution_indices:
            solution = [None] * num_birds
            solution[i] = self._bird
            solutions.append(solution)

        return solutions

class AdjacencyConstraint:
    def __init__(self, bird_a, bird_b, inverted=False):
        self._bird_a = bird_a
        self._bird_b = bird_b
        self._inverted = inverted

    def possible_solutions(self, num_birds):
        solutions = []
        for i in range(num_birds):
            for j in range(num_birds):
                if (i - 1 <= j <= i + 1) != self._inverted and j != i and j in range(num_birds):
                    solution = [None] * num_birds
                    solution[i] = self._bird_a
                    solution[j] = self._bird_b
                    solutions.append(solution)

        return solutions

class OrderConstraint:
    def __init__(self, left_bird, right_bird):
        self._left_bird = left_bird
        self._right_bird = right_bird

    def possible_solutions(self, num_birds):
        solutions = []
        for i in range(num_birds):
            for j in range(i + 1, num_birds):
                solution = [None] * num_birds
                solution[i] = self._left_bird
                solution[j] = self._right_bird
                solutions.append(solution)

        return solutions

class EdgeConstraint:
    def __init__(self, bird, inverted=False):
        self._bird = bird
        self._inverted = inverted

    def possible_solutions(self, num_birds):
        solutions = []
        solution_indices = [0, -1] if not self._inverted else range(1, num_birds - 1)
        for i in solution_indices:
            solution = [None] * num_birds
            solution[i] = self._bird
            solutions.append(solution)

        return solutions

def merge_solutions(a, b, num_birds):
    solution = []
    seen_birds = set()
    for x, y in zip(a, b):
        if (x and y and x != y) or (x and x in seen_birds) or (y and y in seen_birds):
            return None
        seen_birds.update((x, y))
        solution.append(x or y)

    return solution

def fill_solution(solution, birds):
    remaining_birds = set(birds)
    empty_slot = None
    for index, bird in enumerate(solution):
        if bird:
            remaining_birds.remove(bird)
        else:
            assert empty_slot is None
            empty_slot = index

    if not remaining_birds:
        assert empty_slot is None
        return

    assert len(remaining_birds) == 1 and empty_slot is not None
    solution[empty_slot] = list(remaining_birds)[0]

BIRDS = ['y', 'r', 'b', 'p', 'g', 'm']
def solve(num_birds, constraints):
    possible_solutions = [constraint.possible_solutions(num_birds) for constraint in constraints]
    possible_solutions.sort(key=len)

    solutions = reduce(
        lambda merged_solutions, constraint_solutions:
            [
                merged_solution
                    for a in merged_solutions
                        for b in constraint_solutions
                            if (merged_solution := merge_solutions(a, b, num_birds=num_birds))
            ],
        possible_solutions
    )

    assert len(solutions) == 1
    solution = solutions[0]
    fill_solution(solution, BIRDS[:num_birds])
    return solution
