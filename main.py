def remove_adjacent(nums):
  adj_removed = []
  length = len(nums)
  if not nums:
    return adj_removed
  for idx in range(length):
    if idx == length - 1:
      adj_removed.append(nums[idx])
      #break
    elif nums[idx] != nums[idx+1]:
      adj_removed.append(nums[idx])
  return adj_removed
    

unfixed_list = [1, 2, 2, 2, 6, 2, 3, 3, 4, 5, 6]
empty_list = []
list = remove_adjacent(unfixed_list)
example = remove_adjacent(empty_list)
print(list)
print(example)