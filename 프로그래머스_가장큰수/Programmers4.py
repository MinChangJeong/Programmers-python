def solution(numbers):
    answer = ""

    check = False
    for num in numbers:
        if num != 0:
            check = True
    if not check:
        return "0"

    numbers = merge_sort(numbers)

    for num in numbers:
        answer += str(num)

    return answer


def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = int(len(arr)/2)
    left = arr[:mid]
    right = arr[mid:]

    left1 = merge_sort(left)
    right1 = merge_sort(right)

    return merge(left1, right1)


def merge(left, right):
    l = 0
    r = 0

    sorted_list = []

    while(l < len(left) and r < len(right)):
        num1 = str(left[l])+str(right[r])
        num2 = str(right[r])+str(left[l])

        if int(num1) > int(num2):
            sorted_list.append(left[l])
            l += 1
        else:
            sorted_list.append(right[r])
            r += 1

    while l < len(left):
        sorted_list.append(left[l])
        l += 1

    while r < len(right):
        sorted_list.append(right[r])
        r += 1

    return sorted_list
