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

    def findLastWord(self, s):
        r = ""
        for c in s:
            if r and r[0] > c:
                r = r + c
            else:
                r = c + r
        return r

    def solve(self):
        t, ins = self.input()
        # print nums
        res = []
        for i in range(t):
            res += [self.findLastWord(ins[i])]
        self.output(t, res)


def main():
    s = Solution()
    s.solve()


if __name__ == "__main__":
    main()
