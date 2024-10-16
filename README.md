This project presents a solution to the "Minimum Operations" problem. The task is to determine the minimum number of operations required to reach exactly n 'H' characters in a file, starting with a single 'H'.

Problem Overview:
Initial State: The file begins with one 'H'.
Allowed Operations:
Copy All: Copies all characters in the file.
Paste: Pastes the copied characters.
Objective: Achieve exactly n characters with the fewest operations.
Constraints: If n is less than 2 or can't be achieved using the operations, the function should return 0.
Approach:
The solution involves strategically using the 'Copy All' and 'Paste' operations to minimize the total number of steps. The key is to recognize that the most efficient way to reach n characters is by leveraging the prime factors of n. Each prime factor corresponds to a 'Copy All' operation followed by (factor - 1) 'Paste' operations.

Thus, the algorithm computes the prime factors of n, and the sum of these factors gives the minimum number of operations required. Each factor represents one 'Copy All' and multiple 'Paste' actions.
