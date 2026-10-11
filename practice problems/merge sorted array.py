class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n - 1   
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
def main():
    m, n = map(int, input().split())
    nums1 = list(map(int, input().split()))
    if n > 0:
        nums2 = list(map(int, input().split()))
    else:
        nums2 = []
    sol = Solution()
    sol.merge(nums1, m, nums2, n)
if __name__ == '__main__':
    main()
