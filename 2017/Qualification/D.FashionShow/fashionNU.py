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

    def score(self, s):
        if s not in self.scores:
            scr = 0
            dp = {".": 0, "+": 1, "x": 1, "o": 2}
            for i in s:
                scr += dp[i]
            self.scores[s] = scr
        return self.scores[s]

    def putX(self, n, i, j, xmap):
        xmap[i][j] |= 3
        for a in range(i) + range(i+1, n):
            xmap[a][j] |= 5
        for a in range(j) + range(j+1, n):
            xmap[i][a] |= 5

    def putP(self, n, i, j, xmap):
        xmap[i][j] |= 3
        for a in range(i) + range(i+1, n):
            b = j - (i - a)
            if 0 <= b < n:
                xmap[a][b] |= 6
            b = j + (i - a)
            if 0 <= b < n:
                xmap[a][b] |= 6

    def putO(self, n, i, j, xmap):
        self.putX(n, i, j, xmap)
        self.putP(n, i, j, xmap)
        xmap[i][j] |= 4

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
        xmap = [[0] * n for _ in range(n)]
        for model in m:
            self.add(n, model, xmap)
        return xmap

    def avail(self, n, xmap):
        options = []
        for i in range(n):
            for j in range(n):
                if xmap[i][j] < 7:
                    x = xmap[i][j]
                    if x & 1 == 0:
                        options += [('x', i, j)]
                    if x & 2 == 0:
                        options += [('+', i, j)]
#                    if x & 4 == 0:
#                        options += [('o', i, j)]
        return options

    def DFS(self, n, s, xmap):
        if s in self.scorebook:
            return self.scorebook[s]

        opts = self.avail(n, xmap)
        if len(opts) == 0:
            self.scorebook[s] = s
            return s

        # print len(opts)
        hscore = 0
        hplan = s
        for o in opts:
            c, i, j = o
            idx = i * n + j
            news = s[:idx] + c + s[idx+1:]
            nmap = self.add(n, o, xmap)
            finals = self.DFS(n, news, nmap)
            if self.score(finals) > hscore:
                hscore = self.score(finals)
                hplan = finals
            self.scorebook[s] = finals
        return hplan

    def solve(self):
        t, ins = self.input()
        # res = []
        for i in range(t):
            n, m = ins[i]
            s = self.convertToString(n, m)
            finals = self.DFS(n, s, self.findMap(n, m))
            print self.score(finals), finals


def main():
    s = Solution()
    s.solve()


if __name__ == "__main__":
    main()
