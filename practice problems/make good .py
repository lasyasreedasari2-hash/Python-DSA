class Solution:
    def makeGood(self, s: str) -> str:
        # start your solution
        stack = []
        for char in s:
            if stack and stack[-1].lower() == char.lower() and stack[-1] != char:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
        # end your solution

def main():
    s = input().strip()
    sol = Solution()
    result = sol.makeGood(s)
    print(result)

if __name__ == "__main__":
    main()
