class Solution(object):
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

    def printshow(self, n, m):
        show = [["."] * n for _ in range(n)]
        for model in m:
            c, x, y = model
            show[x][y] = c
        for line in show:
            print "".join(line)
        print '---------------'

    def score(self, n, m):
        show = [["."] * n for _ in range(n)]
        for model in m:
            c, x, y = model
            show[x][y] = c
        s = 0
        for i in range(n):
            for j in range(n):
                if show[i][j] == 'x' or show[i][j] == '+':
                    s += 1
                if show[i][j] == 'o':
                    s += 2
        return s

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
                    if x & 4 == 0:
                        options += [('o', i, j)]
        return options

    def DFS(self, n, m, xmap):
        opts = self.avail(n, xmap)
        if len(opts) == 0:
            return self.score(n, m), m

        hscore = 0
        hplan = m
        for o in opts:
            nmap = self.add(n, o, xmap)
            s, l = self.DFS(n, m + [o], nmap)
            if s > hscore:
                hscore = s
                hplan = l
        return hscore, hplan

    def solve(self):
        t, ins = self.input()
        res = []
        for i in range(t):
            n, m = ins[i]
            y, l = self.DFS(n, m, self.findMap(n, m))
            l = l[len(m):]
            z = len(l)
            r = str(y) + " " + str(z)
            for m in l:
                r += "\n" + " ".join([str(i) for i in m])
            res += [r]
        self.output(t, res)


def main():
    s = Solution()
    s.solve()


if __name__ == "__main__":
    main()
