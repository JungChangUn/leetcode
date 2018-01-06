class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        step1 = step2 = 0
        l = len(nums1)

        while m > step1 and n > step2:
            # if nums1[step1] == nums2[step2]:
            #     step2 += 1
            #     step1 += 1
            if nums1[step1] < nums2[step2]:
                step1 += 1
                # print("<")
            else:
                nums1.insert(step1,nums2[step2])
                step2 += 1
                step1 += 1
                m += 1
                l += 1
                # print("=")

        for _ in range(l - m):
            nums1.pop()

        nums1 += nums2[step2:n]
        # print (nums1)

        # print(str(step1) + " : " + str(step2))
        # print (nums1)

nums1 = [4,0,0,0,0,0]
m = 1
nums2 = [1,2,3,5,6]
n = 5

Solution().merge(nums1, m, nums2, n)
print (nums1)