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

    def flip(self, l, k):
        n = len(l)
        c = 0
        for i in range(n - k + 1):
            if l[i] == 0:
                c += 1
                for j in range(i, i + k):
                    l[j] = 1 - l[j]
        for i in range(n-k+1, n):
            if l[i] == 0:
                return "IMPOSSIBLE"
        return c

    def solve(self):
        n, ins = self.input()
        # print nums
        dp = {"+": 1, "-": 0}
        res = []
        for i in range(n):
            s, k = ins[i].split(" ")
            l = [dp[c] for c in s]
            res += [self.flip(l, int(k))]
        self.output(n, res)


def main():
    s = Solution()
    s.solve()


if __name__ == "__main__":
    main()
