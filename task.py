import random
import copy


# The original sorting program to be tested
def sorting_program(nums):
    return sorted(nums)


# Metamorphic Relations (MRs)
def MR1(nums):
    nums.append(nums[0])
    return sorting_program(nums)


def MR2(nums):
    return list(reversed(sorting_program(nums)))


# Mutation Operators for the sorting program
# Each mutant introduces a different bug
mutants = [
    lambda nums: list(reversed(sorted(nums))),  # Mutant 1: Reverse the sorted list
    lambda nums: sorted(nums[:-1]) + [nums[-1]],  # Mutant 2: Do not sort the last element
    lambda nums: sorted(nums, reverse=True),  # Mutant 3: Sort in descending order
    lambda nums: nums,  # Mutant 4: Return the original unsorted list
    lambda nums: sorted(nums)[:-1],  # Mutant 5: Remove the last element after sorting
    lambda nums: sorted(nums)[1:],  # Mutant 6: Remove the first element after sorting
    lambda nums: sorted(nums) + [1000],  # Mutant 7: Add a large number at the end
    lambda nums: [-1000] + sorted(nums),  # Mutant 8: Add a small number at the beginning
    lambda nums: sorted(nums[1:]),  # Mutant 9: Do not include the first element in sorting
    lambda nums: sorted(nums[:-1]),  # Mutant 10: Do not include the last element in sorting
    lambda nums: sorted(nums)[::-2],  # Mutant 11: Return every second element after sorting
    lambda nums: sorted(nums)[::2],  # Mutant 12: Skip every second element after sorting
    lambda nums: sorted(nums) + sorted(nums),  # Mutant 13: Duplicate the sorted list
    lambda nums: sorted(nums)[5:],  # Mutant 14: Return the last half after sorting
    lambda nums: sorted(nums)[:5],  # Mutant 15: Return the first half after sorting
    lambda nums: sorted(nums)[2:5],  # Mutant 16: Return a middle slice after sorting
    lambda nums: sorted(nums, key=lambda x: abs(x)),  # Mutant 17: Sort by absolute value
    lambda nums: sorted(nums, key=lambda x: -x),  # Mutant 18: Sort by negative value
    lambda nums: sorted(nums)[1:-1],  # Mutant 19: Remove first and last elements after sorting
    lambda nums: [0] * len(nums)  # Mutant 20: Return a list of zeros with the same length
]


# Testing function using MRs and mutation analysis
def test_program():
    nums = random.sample(range(1, 100), 10)

    mr1_result = MR1(copy.deepcopy(nums))
    mr2_result = MR2(copy.deepcopy(nums))

    print("Original Program with MR1:", mr1_result)
    print("Original Program with MR2:", mr2_result)

    for i, mutant in enumerate(mutants):
        mr1_mutant_result = MR1(mutant(copy.deepcopy(nums)))
        mr2_mutant_result = MR2(mutant(copy.deepcopy(nums)))

        print(f"\nMutant {i+1} Program with MR1:", mr1_mutant_result)
        print(f"Mutant {i+1} Program with MR2:", mr2_mutant_result)


if __name__ == "__main__":
    test_program()
