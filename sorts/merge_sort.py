def mergesort(numbers):
    if len(numbers) < 2:
        return numbers
    else:
        center, result = len(numbers) // 2, []
        left, right = numbers[:center], numbers[center:]
        f, s = mergesort(left), mergesort(right)
        i, j = 0, 0
        while i < len(f) and j < len(s):
            if f[i] <= s[j]:
                result.append(f[i])
                i += 1
            else:
                result.append(s[j])
                j += 1
        result.extend(f[i:])
        result.extend(s[j:])
        return result


print(mergesort([12, 33, 2, 87, 216, 7, 5, 367]))