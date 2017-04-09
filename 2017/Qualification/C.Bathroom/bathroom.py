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

    def findstall(self, n, k):
        import heapq
        hp = [(- n, 0, n + 1)]
        while(k > 1):
            d, l, r = heapq.heappop(hp)
            print - d
            m = (l + r) / 2
            # print l, m ,r
            heapq.heappush(hp, (l-m+1, l, m))
            heapq.heappush(hp, (m-r+1, m, r))
            k -= 1
            # print hp
        d, l, r = heapq.heappop(hp)
        m = (l + r) / 2
        l = m - l - 1
        r = r - m - 1
        return str(max(l, r)) + " " + str(min(l, r))

    def findfast(self, n, k):
        spots = [n]
        r = 0
        l = 1
        v = (n - 1) / 2
        for i in range(0, k):
            if i >= 2 ** l - 1:
                spots += [v + 1] * r
                spots += [v] * (2 ** l - r)
                l += 1
                v = (v - 1) / 2
                r = 0
            t = spots[i] - 1
            r += t - v * 2

        v = spots[k - 1] - 1
        return str(v-v/2) + " " + str(v/2)

    def findlog(self, n, k):
        r = 0
        l = 1
        v = n - 1
        while(2 ** (l) - 1 < k):
            r = (v - (v / 2) * 2) * (2 ** (l-1)) + r
            v = v / 2 - 1
            l += 1

        k -= 2 ** (l-1) - 1
        v = v + (r >= k)
        return str(v - v/2) + " " + str(v/2)

    def solve(self):
        t, ins = self.input()
        res = []
        for i in range(t):
            n, k = ins[i]
            res += [self.findlog(n, k)]
        self.output(t, res)


def main():
    s = Solution()
    s.solve()


if __name__ == "__main__":
    main()
