# Problem Statement #
# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

# Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

# this is my second  to practice "muscle memory"


def pair_with_targetsum(arr, target_sum):
  if arr == []:
    return []
  leftPtr = 0
  rightPtr = len(arr) - 1
  while leftPtr < rightPtr:
    sum = arr[leftPtr] + arr[rightPtr]
    if sum == target_sum:
      return [leftPtr, rightPtr]
    if sum < target_sum:
      leftPtr += 1
    else:
      rightPtr -= 1
  return

def main():
  print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
  print(pair_with_targetsum([2, 5, 9, 11], 11))
  print(pair_with_targetsum([], 11))
  print(pair_with_targetsum([1, 5, 8, 9], 11))

main()




















# Solution
# -----
#   left, right = 0, len(arr) - 1
#   while(left < right):
#     current_sum = arr[left] + arr[right]
#     if current_sum == target_sum:
#       return [left, right]

#     if target_sum > current_sum:
#       left += 1  # we need a pair with a bigger sum
#     else:
#       right -= 1  # we need a pair with a smaller sum
#   return [-1, -1]