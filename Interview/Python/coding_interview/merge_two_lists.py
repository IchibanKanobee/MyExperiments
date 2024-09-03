class Solution:
    def mergeTwoListst(self, list1, list2):
        mergedList = []

        ind1 = 0
        ind2 = 0
        mergedInd = 0

        len1 = len(list1)
        len2 = len(list2)

        while (True):
            if list1[ind1] < list2[ind2]:
                mergedList.append(list1[ind1])
                ind1 += 1
                mergedInd += 1
            elif list1[ind1] > list2[ind2]:
                mergedList.append(list2[ind2])
                ind2 += 1
                mergedInd += 1
            else:
                mergedList.append(list1[ind1])
                ind1 += 1
                mergedList.append(list2[ind2])
                ind2 += 1
                mergedInd += 2

            if mergedInd >= (len2 + len1):
                break

        return mergedList

s = Solution()

list1 = [1, 2, 4]
list2 = [1, 3, 4]

merged = s.mergeTwoListst(list1, list2)
print(merged)
