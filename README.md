# Birds Solver

*This project is finished as it implements all constraints presented in the game and the solver succeeds in all test cases. You are free to create more scenarios or to introduce more constraint types.*

This is a solver for the Puzzle game "Birds" by Yoann Levet and Rémi Leblond.

The game starts by considering the set of all solution sets (possible orderings of n unique birds). A *solution set* thus is a bijective mapping between bird and slot index. Then, this solution set is constrained by given constraints, such that only a single unique solution satisfies all constraints. The aim of the game is to find this unique solution.

The algorithm starts by generating the solution sets that satisfy each constraint **individually**. Then, the unions of all solution sets are taken and inadmissible (non-bijective) solution sets are discarded. The set of remaining solution sets is required to have cardinality = 1 and this unique solution to fully constrain bird ordering. An intermediary solution set need not fully constrain.
