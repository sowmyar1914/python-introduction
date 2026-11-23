"""Big O Detective — classification, pair counting, and benchmarks."""

# PART 1 — CLASSIFICATIONS (one-sentence explanations)
# A: O(1) because data[0] accesses one element regardless of input size.
# B: O(n) because the for loop checks each element exactly once.
# C: O(n^2) because the two nested loops each run n times.
# D: O(log n) because n is divided in half during each loop iteration.
# E: O(n log n) because sum(data) is O(n), sorted(data) is O(n log n),
#    and data[0] is O(1), so sorting determines the overall complexity.

import random
import time


def count_pairs_nested(data, target):
    """O(n^2): Compare every pair at different indexes (i < j)."""
    count = 0
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] + data[j] == target:
                count += 1
    return count


def count_pairs_dictionary(data, target):
    """O(n) average time: Count earlier matching complements with a dictionary."""
    seen = {}
    count = 0
    for number in data:
        count += seen.get(target - number, 0)
        seen[number] = seen.get(number, 0) + 1
    return count


def benchmark(func, data, target):
    """Time a function using time.time(), as shown in the guided notes."""
    start = time.time()
    result = func(data, target)
    end = time.time()
    return end - start, result


def main():
    # Both algorithms must count the same pairs, including repeated values.
    assert count_pairs_nested([2, 2, 2], 4) == 3
    assert count_pairs_dictionary([2, 2, 2], 4) == 3

    print('BIG O DETECTIVE — BENCHMARK RESULTS')
    print('Each pair uses two different positions in the list.\n')
    for size in [1000, 5000, 10000]:
        data = list(range(size))
        random.Random(42).shuffle(data)
        target = size - 1

        nested_time, nested_count = benchmark(count_pairs_nested, data, target)
        dictionary_time, dictionary_count = benchmark(count_pairs_dictionary, data, target)
        assert nested_count == dictionary_count
        print(f'n={size:>6} | Nested: {nested_time:.4f}s | '
              f'Dictionary: {dictionary_time:.4f}s | Pairs: {nested_count}')

    print('\nConclusion: Both solutions give the same answer, but the O(n) '
          'dictionary solution is faster for large lists than O(n^2) nested loops.')


if __name__ == '__main__':
    main()

# SAMPLE BENCHMARK OUTPUT: timings vary by computer and by run.
# n=  1000 | Nested: 0.0296s | Dictionary: 0.0002s | Pairs: 500
# n=  5000 | Nested: 0.9360s | Dictionary: 0.0010s | Pairs: 2500
# n= 10000 | Nested: 11.4062s | Dictionary: 0.0055s | Pairs: 5000
"""Big O Detective — classification, pair counting, and benchmarks."""

# PART 1 — CLASSIFICATIONS (one-sentence explanations)
# A: O(1) because data[0] accesses one element regardless of input size.
# B: O(n) because the for loop checks each element exactly once.
# C: O(n^2) because the two nested loops each run n times.
# D: O(log n) because n is divided in half during each loop iteration.
# E: O(n log n) because sum(data) is O(n), sorted(data) is O(n log n),
#    and data[0] is O(1), so sorting determines the overall complexity.

import random
import time


def count_pairs_nested(data, target):
    """O(n^2): Compare every pair at different indexes (i < j)."""
    count = 0
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] + data[j] == target:
                count += 1
    return count


def count_pairs_dictionary(data, target):
    """O(n) average time: Count earlier matching complements with a dictionary."""
    seen = {}
    count = 0
    for number in data:
        count += seen.get(target - number, 0)
        seen[number] = seen.get(number, 0) + 1
    return count


def benchmark(func, data, target):
    """Time a function using time.time(), as shown in the guided notes."""
    start = time.time()
    result = func(data, target)
    end = time.time()
    return end - start, result


def main():
    # Both algorithms must count the same pairs, including repeated values.
    assert count_pairs_nested([2, 2, 2], 4) == 3
    assert count_pairs_dictionary([2, 2, 2], 4) == 3

    print('BIG O DETECTIVE — BENCHMARK RESULTS')
    print('Each pair uses two different positions in the list.\n')
    for size in [1000, 5000, 10000]:
        data = list(range(size))
        random.Random(42).shuffle(data)
        target = size - 1

        nested_time, nested_count = benchmark(count_pairs_nested, data, target)
        dictionary_time, dictionary_count = benchmark(count_pairs_dictionary, data, target)
        assert nested_count == dictionary_count
        print(f'n={size:>6} | Nested: {nested_time:.4f}s | '
              f'Dictionary: {dictionary_time:.4f}s | Pairs: {nested_count}')

    print('\nConclusion: Both solutions give the same answer, but the O(n) '
          'dictionary solution is faster for large lists than O(n^2) nested loops.')


if __name__ == '__main__':
    main()

# SAMPLE BENCHMARK OUTPUT: timings vary by computer and by run.
# n=  1000 | Nested: 0.0296s | Dictionary: 0.0002s | Pairs: 500
# n=  5000 | Nested: 0.9360s | Dictionary: 0.0010s | Pairs: 2500
# n= 10000 | Nested: 11.4062s | Dictionary: 0.0055s | Pairs: 5000