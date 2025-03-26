
def merge_lists(list1, list2):
    merged_list = list1 + list2
    merged_list.sort(key=lambda x: x[0])
    
    result = []
    for elem in merged_list:
        if result:
            last = result[-1]
            left_a, right_a = last[0], last[1]
            left_b, right_b = elem[0], elem[1]
            
            overlap = min(right_a, right_b) - max(left_a, left_b)
            length_a = right_a - left_a
            length_b = right_b - left_b
            
            if overlap > length_a / 2 or overlap > length_b / 2:
                last.extend(elem[2:])
                continue
        result.append(elem)
    
    for elem in result:
        print(f"{{ Positions: [{elem[0]}, {elem[1]}], Values: {elem[2:]} }}")

n = int(input("Enter number of elements in first list: "))
list1 = []
print("Enter elements (left_position right_position followed by values):")
for _ in range(n):
    values = list(map(int, input().split()))
    list1.append(values)

m = int(input("Enter number of elements in second list: "))
list2 = []
print("Enter elements (left_position right_position followed by values):")
for _ in range(m):
    values = list(map(int, input().split()))
    list2.append(values)

print("Merged List:")
merge_lists(list1, list2)