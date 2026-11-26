def display_results(name, result, total_pages):
    hits, faults, frames = result

    hit_percentage = (hits / total_pages) * 100
    fault_percentage = (faults / total_pages) * 100

    print(f"\n========== {name} RESULTS ==========")
    print("Final Frames      :", frames)
    print("Total Page Hits   :", hits)
    print("Total Page Faults :", faults)
    print(f"Hit Percentage    : {hit_percentage:.2f}%")
    print(f"Fault Percentage  : {fault_percentage:.2f}%")


def compare_results(fifo_result, lru_result, optimal_result):

    print("\n" + "=" * 55)
    print("             ALGORITHM COMPARISON")
    print("=" * 55)

    algorithms = {
        "FIFO": fifo_result,
        "LRU": lru_result,
        "OPTIMAL": optimal_result
    }

    print(f"{'Algorithm':<15}{'Hits':<10}{'Faults':<10}{'Hit Rate':<15}")
    print("-" * 55)

    for name, result in algorithms.items():
        hits, faults, frames = result

        total = hits + faults
        hit_rate = (hits / total) * 100

        print(
            f"{name:<15}{hits:<10}{faults:<10}{hit_rate:.2f}%"
        )

    # Find the algorithm with the fewest page faults
    best_algorithm = min(
        algorithms,
        key=lambda name: algorithms[name][1]
    )

    lowest_faults = algorithms[best_algorithm][1]

    print("-" * 55)
    print("BEST PERFORMANCE:", best_algorithm)
    print("LOWEST PAGE FAULTS:", lowest_faults)
    print("=" * 55)
