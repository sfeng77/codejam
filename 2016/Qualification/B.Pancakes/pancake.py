class Solution(object):
    def input(self):
        t = int(raw_input())  # read a line with a single integer
        ins = []
        for i in xrange(1, t + 1):
            ins += [raw_input()]
        return t, ins

    def output(self, n, s):
        for i in xrange(n):
            print "Case #{}: {}".format(i + 1, str(s[i]))

    def flip(self, l):
        # print l
        n = len(l)
        while n > 0 and l[-1] == 1:
            l.pop()
            n -= 1

        if n == 0:
            return 0

        h = 0

        while(n > 0 and h < n and l[h] == 1):
            h += 1
        # print h
        if n == 0:
            return 1

        newl = [1 - i for i in l[:h:-1]]
        if h == 0:
            return self.flip(newl) + 1
        else:
            return self.flip(newl) + 2

    def solve(self):
        n, nums = self.input()
        # print nums
        dp = {"+": 1, "-": 0}
        res = []
        for i in range(n):
            l = [dp[c] for c in nums[i]]
            res += [self.flip(l)]
        self.output(n, res)


def main():
    s = Solution()
    s.solve()


if __name__ == "__main__":
    main()
