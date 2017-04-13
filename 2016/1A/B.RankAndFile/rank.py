def solve(lines):
    count = {}
    for l in lines:
        for j in l:
            count[j] = count.get(j, 0) + 1
    # print count
    res = [k for k in count.keys() if count[k] % 2 == 1]
    return sorted(res)


def main():
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        n = int(raw_input())
        lines = []
        for j in xrange(0, 2 * n - 1):
            lines.append([int(c) for c in raw_input().split(" ")])
        sol = solve(lines)
        print "Case #{}: {}".format(i, " ".join([str(k) for k in sol]))


if __name__ == "__main__":
    main()
