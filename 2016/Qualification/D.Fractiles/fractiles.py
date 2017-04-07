class Solution(object):

    def input(self):
        t = int(raw_input())  # read a line with a single integer
        ins = []
        for i in xrange(1, t + 1):
            ins += [[int(c) for c in raw_input().split(" ")]]
        return t, ins

    def output(self, n, s):
        for i in xrange(n):
            print "Case #{}: {}".format(i + 1, str(s[i]))

    def cleanSmall(self, k):
        return " ".join([str(c) for c in range(1, k + 1)])

    def solve(self):
        t, ins = self.input()
        res = []
        for i in range(t):
            k, c, s = ins[i]
            if s == k:
                res += [self.cleanSmall(k)]
        self.output(t, res)


def main():
    s = Solution()
    s.solve()


if __name__ == "__main__":
    main()
