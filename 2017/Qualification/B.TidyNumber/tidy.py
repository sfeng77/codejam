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

    def findTidy(self, num):
        l = list(str(num))
        n = len(l)
        res = 0
        for i in range(n):
            c = l[i]
            if res + int(c * (n-i)) > num:
                return res + (int(c) - 1) * 10 ** (n-i-1) + int("9" * (n-i-1))
            res += int(c + '0' * (n-i-1))
        return res

    def solve(self):
        t, ins = self.input()
        res = []
        for i in range(t):
            res += [self.findTidy(int(ins[i]))]
        self.output(t, res)


def main():
    s = Solution()
    s.solve()


if __name__ == "__main__":
    main()
