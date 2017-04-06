class CountSheep(object):
    def input(self):
        t = int(raw_input())  # read a line with a single integer
        ins = []
        for i in xrange(1, t + 1):
            ins += [int(s) for s in raw_input().split(" ")]
        return t, ins

    def output(self, n, s):
        for i in xrange(n):
            print "Case #{}: {}".format(i + 1, s[i])

    def count(self, n):
        seen = 0
        i = 0
        while seen != 0b1111111111:
            i += 1
            m = n * i
            while(m):
                r = m % 10
                m = m / 10
                seen |= 0b1 << r
            if i > 100:
                # print "time exceeded!", n
                return "INSOMNIA"
        return str(n * i)

    def solve(self):
        n, nums = self.input()
        # print nums
        res = []
        for i in range(n):
            res += [self.count(nums[i])]
        self.output(n, res)


def main():
    s = CountSheep()
    s.solve()


if __name__ == "__main__":
    main()
