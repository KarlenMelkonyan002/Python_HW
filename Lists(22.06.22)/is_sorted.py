nums = list(map(int, input().split()))


def list_sorted(list_nums):
    if sorted(list_nums) == list_nums or sorted(list_nums)[::-1] == list_nums:
        return True
    return False


print(list_sorted(nums))
