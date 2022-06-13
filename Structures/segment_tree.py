class SegmentTree:
    def __init__(self, array):
        self.a = array
        self.t = 4 * len(self.a) * [0]
        self.build(1, 0, len(self.a) - 1)

    def build(self, v, tl, tr):
        if tl == tr:
            self.t[v] = self.a[tl]
        else:
            tm = (tl + tr) // 2
            self.build(2 * v, tl, tm)
            self.build(2 * v + 1, tm + 1, tr)
            self.t[v] = self.t[2 * v] + self.t[2 * v + 1]

    def sum(self, v, tl, tr, l, r):
        if l > r:
            return 0
        if l == tl and r == tr:
            return self.t[v]
        tm = (tl + tr) // 2
        return self.sum(2 * v, tl, tm, l, min(r, tm)) + self.sum(2 * v + 1, tm + 1, tr, max(l, tm + 1), r)

    def update(self, v, tl, tr, pos, new_val):
        if tl == tr:
            self.t[v] = new_val
        else:
            tm = (tl + tr) // 2
            if pos <= tm:
                self.update(2 * v, tl, tm, pos, new_val)
            else:
                self.update(2 * v + 1, tm + 1, tr, pos, new_val)
            self.t[v] = self.t[2 * v] + self.t[2 * v + 1]


st = SegmentTree([12, 33, 2, 87, 216, 7, 5, 367])
print(st.t)
print(st.sum(1, 0, 7, 3, 6))
st.update(1, 0, 7, 5, 100)
print(st.t)
print(st.sum(1, 0, 7, 3, 6))