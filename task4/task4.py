import sys

nums_file = sys.argv[1]
nums = []
with open(nums_file) as file:
    for line in file:
        line = line.split()
        nums = nums + line
nums = list(map(int, nums))
nums.sort()
lenght = len(nums)
mid = lenght // 2
if lenght % 2 == 0:
    mediana = (nums[mid - 1] + nums[mid]) / 2
else:
    mediana = nums[mid]
move = 0
for numb in nums:
    if numb > mediana:
        move = move + (numb - mediana)
    elif numb < mediana:
        move = move + (mediana - numb)
    elif numb == mediana:
        continue
if move > 20:
    print("Для приведения массива к единому числу требуется больше 20 ходов")
else:
    print(int(move))


