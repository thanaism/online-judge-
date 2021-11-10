#####segfunc#####
def segfunc(x, y):
    return max(x, y)


#################

#####ide_ele#####
ide_ele = 0
#################


class SegTree:
    """
    init(init_val, ide_ele): 配列init_valで初期化 O(N)
    update(k, x): k番目の値をxに更新 O(logN)
    query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
    """

    def __init__(self, init_val, segfunc, ide_ele):
        """
        init_val: 配列の初期値
        segfunc: 区間にしたい操作
        ide_ele: 単位元
        n: 要素数
        num: n以上の最小の2のべき乗
        tree: セグメント木(1-index)
        """
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        # 配列の値を葉にセット
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        # 構築していく
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, k, x):
        """
        k番目の値をxに更新
        k: index(0-index)
        x: update value
        """
        k += self.num
        self.tree[k] = x
        while k > 1:
            self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
            k >>= 1

    def query(self, l, r):
        """
        [l, r)のsegfuncしたものを得る
        l: index(0-index)
        r: index(0-index)
        """
        res = self.ide_ele

        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res


n = int(input())
p = [*map(int, input().split())]
for i in range(n):
    p[i] -= 1
a, b, c = [], [], []
for _ in range(n):
    i, j, k = map(int, input().split())
    a.append(i)
    b.append(min(i, j))
    c.append(min(i, k))
l, r = [], []
for i, j, k in zip(a, b, c):
    l.append(i - j)
    r.append(i - k)
q = [0] * n
for i in range(n):
    q[p[i]] = i

base = sum(a)
ans = 0
sl = 0
sr = sum(r)
dp = SegTree([0] * n, segfunc, ide_ele)

for i in range(n):
    now = dp.query(0, q[i]) + a[i]
    now = max(now, sl + a[i])
    sr -= r[i]
    ans = max(ans, now + sr)
    sl += l[i]
    dp.update(q[i], now)

ans = base - ans
print(ans)
