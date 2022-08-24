from typing import List


class SuperList(List):
    def __len__(self):
        return 1000


super_list1 = SuperList()
for i in range(0, 5):
    super_list1.append(i)

print(len(super_list1))
print(super_list1[3])
print(issubclass(SuperList, list))
