class Solution(object):
    def input(self):
        t = int(raw_input())  # read a line with a single integer
        ins = []
        for i in xrange(1, t + 1):
            ins += [raw_input()]
        return t, ins

    def output(self, n, s):
        print "Case #1:"
        print "\n".join(s)

    def interpret(self, m, base):
        val = 0
        for i in range(len(m)):
            val += base ** i * int(m[-(i+1)])
        return val

    def findfactor(self, m):
        if m <= 3:
            return -1

        for i in range(2, min(m ** 0.5, 100)):
            if m % i == 0 and i < m:
                return i

        return -1

    def coin(self, n, j):
        # print l

        c = (0b1 << (n-1)) + 1
        found = 0
        res = []
        while(found < j):
            c += 2
            s = bin(c)[2:]
            if s.count('1') % 6 > 0:
                continue
            f2 = self.findfactor(self.interpret(s, 2))
            if f2 == -1:
                continue
            f6 = self.findfactor(self.interpret(s, 6))
            if f6 == -1:
                continue
            f8 = self.findfactor(self.interpret(s, 8))
            if f8 == -1:
                continue
            f = str(f2) + " 2 3 2 " + str(f6)
            f += " 2 " + str(f8) + " 2 3"
            res += [s + " " + f]
            found += 1
        return res

    def solve(self):
        t, ins = self.input()
        # print nums
        n, j = [int(i) for i in ins[0].split(" ")]
        res = self.coin(n, j)
        self.output(j, res)


def main():
    s = Solution()
    s.solve()


if __name__ == "__main__":
    main()
