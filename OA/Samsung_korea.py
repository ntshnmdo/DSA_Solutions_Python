from itertools import permutations

def calculate_distance(spots, gates, fishermen):
    n = len(spots)
    min_distance = float('inf')

    # Generate all permutations of gate orders
    for order in permutations(range(3)):
        visited = [False] * n
        total_distance = 0

        for i in order:
            gate_pos = gates[i]
            num_fishermen = fishermen[i]

            left, right = gate_pos - 1, gate_pos - 1
            count = 0
            temp_distance = 0

            # Place all fishermen from the current gate
            while count < num_fishermen:
                if left >= 0 and not visited[left]:
                    temp_distance += (gate_pos - left)
                    visited[left] = True
                    count += 1
                    if count == num_fishermen:
                        break
                if right < n and not visited[right]:
                    temp_distance += (right - gate_pos)
                    visited[right] = True
                    count += 1
                    if count == num_fishermen:
                        break
                left -= 1
                right += 1

            total_distance += temp_distance

        min_distance = min(min_distance, total_distance)

    return min_distance


# Input values
N = 10  # Total number of fishing spots
gates = [4, 6, 10]  # Gate positions
fishermen = [5, 2, 2]  # Number of fishermen at each gate

# Calculate minimum walking distance
result = calculate_distance([0] * N, gates, fishermen)
print(f"Minimum walking distance: {result}")
