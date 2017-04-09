class Solution(object):
    def __init__(self):
        self.scorebook = {}
        self.scores = {}

    def input(self):
        t = int(raw_input())  # read a line with a single integer
        ins = []
        for i in xrange(1, t + 1):
            n, m = [int(c) for c in raw_input().split(" ")]
            models = []
            for j in range(m):
                c, x, y = raw_input().split(" ")
                models += [(c, int(x) - 1, int(y) - 1)]
            ins += [(n, models)]
        return t, ins

    def output(self, n, s):
        for i in xrange(n):
            print "Case #{}: {}".format(i + 1, str(s[i]))

    def convertToString(self, n, m):
        show = [["."] * n for _ in range(n)]
        for model in m:
            c, x, y = model
            show[x][y] = c
        return "".join(["".join(l) for l in show])

    def convertback(self, n, m, s):
        show = [["."] * n for _ in range(n)]
        for model in m:
            c, x, y = model
            show[x][y] = c
        og = "".join(["".join(l) for l in show])
        res = ""
        diff = 0
        for i in range(n * n):
            if og[i] != s[i]:
                res += "\n" + s[i] + " " + str(i / n) + " " + str(i % n)
                diff += 1
        return diff, res

    def score(self, s):
        if s not in self.scores:
            scr = 0
            dp = {".": 0, "+": 1, "x": 1, "o": 2}
            for i in s:
                scr += dp[i]
            self.scores[s] = scr
        return self.scores[s]

    def putX(self, n, i, j, xmap):
        # add a x to the map
        xmap[i * n + j] |= 3
        for a in range(i) + range(i + 1, n):
            xmap[a * n + j] |= 5
        for a in range(j) + range(j + 1, n):
            xmap[i * n + a] |= 5

    def putP(self, n, i, j, xmap):
        # add a + to the map
        xmap[i * n + j] |= 3
        for a in range(i) + range(i + 1, n):
            b = j - (i - a)
            if 0 <= b < n:
                xmap[a * n + b] |= 6
            b = j + (i - a)
            if 0 <= b < n:
                xmap[a * n + b] |= 6

    def putO(self, n, i, j, xmap):
        # add a o to the map
        self.putX(n, i, j, xmap)
        self.putP(n, i, j, xmap)
        xmap[i * n + j] |= 7

    def add(self, n, model, xmap):
        nmap = xmap[:]
        c, i, j = model
        if c == '+':
            self.putP(n, i, j, nmap)
        if c == 'x':
            self.putX(n, i, j, nmap)
        if c == 'o':
            self.putO(n, i, j, nmap)
        return nmap

    def findMap(self, n, m):
        xmap = [0] * (n * n)
        for model in m:
            xmap = self.add(n, model, xmap)
        return xmap

    def avail(self, n, xmap):
        options = []
        for i in range(n * n):
            if xmap[i] < 7:
                x = xmap[i]
                if x & 0b1 == 0:
                    options += [('x', i / n, i % n)]
                if x & 0b10 == 0:
                    options += [('+', i / n, i % n)]
                if x & 0b100 == 0:
                    options += [('o', i / n, i % n)]
        return options

    def greedy(self, n, xmap):
        options = []
        for i in range(n * n):
            x = xmap[i]
            if x & 0b100 == 0:
                options += [('o', i / n, i % n)]

        for i in range(n * n):
            x = xmap[i]
            if x & 0b10 == 0:
                options += [('+', i / n, i % n)]
            if x & 0b1 == 0:
                options += [('x', i / n, i % n)]

        return options

    def greedySearch(self, n, s, xmap):
        opts = self.greedy(n, xmap)
        while(opts):
            o = opts[0]
            c, i, j = o
            idx = i * n + j
            s = s[:idx] + c + s[idx + 1:]
            # print xmap
            xmap = self.add(n, o, xmap)
            opts = self.greedy(n, xmap)
        return s

    def DFS(self, n, s, xmap):
        if s in self.scorebook:
            return self.scorebook[s]

        opts = self.avail(n, xmap)
        # print s, len(opts), opts
        # raw_input()

        if len(opts) == 0:
            # print s, xmap
            self.scorebook[s] = s
            # print self.score(s)
            # exit()
            return s

        hscore = 0
        hplan = s
        for o in opts:
            c, i, j = o
            idx = i * n + j
            news = s[:idx] + c + s[idx + 1:]
            # print xmap
            nmap = self.add(n, o, xmap)
            # print xmap, nmap, o
            # print news, nmap
            finals = self.DFS(n, news, nmap)
            if self.score(finals) > hscore:
                hscore = self.score(finals)
                hplan = finals
            self.scorebook[s] = hplan
        return hplan

    def solve(self):
        t, ins = self.input()
        res = []
        for i in range(t):
            n, m = ins[i]
            s = self.convertToString(n, m)
            # print s
            # finals = self.DFS(n, s, self.findMap(n, m))
            finals = self.greedySearch(n, s, self.findMap(n, m))
            diff, steps = self.convertback(n, m, finals)
            res += [str(self.score(finals)) + " " + str(diff) + steps]
        self.output(t, res)


def main():
    s = Solution()
    s.solve()


if __name__ == "__main__":
    main()
