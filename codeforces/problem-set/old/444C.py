import collections, math, bisect, heapq, random, functools, itertools, copy, typing
import platform; LOCAL = (platform.uname().node == 'AMO')


import sys; input = lambda: sys.stdin.readline().rstrip("\r\n")
inp = lambda f=int: list(map(f, input().split()))

def make_arr(*args):
    def func(x):
        if len(args) == 1: return [x() for _ in range(args[0])]
        return [make_arr(*args[1:])(x) for _ in range(args[0])]
    return func

def debug(*args):
    if LOCAL:
        print('\033[92m', end='')
        printf(*args)
        print('\033[0m', end='')

def printf(*args):
    if LOCAL:
        print('>>>: ', end='')
    for arg in args:
        if isinstance(arg, typing.Iterable) and \
                not isinstance(arg, str) and \
                not isinstance(arg, dict):
            print(' '.join(map(str, arg)), end=' ')
        else:
            print(arg, end=' ')
    print()

class SortedList:
    def __init__(self, iterable=[], _load=200):
        """Initialize sorted list instance."""
        values = sorted(iterable)
        self._len = _len = len(values)
        self._load = _load
        self._lists = _lists = [values[i:i + _load] for i in range(0, _len, _load)]
        self._list_lens = [len(_list) for _list in _lists]
        self._mins = [_list[0] for _list in _lists]
        self._fen_tree = []
        self._rebuild = True

    def _fen_build(self):
        """Build a fenwick tree instance."""
        self._fen_tree[:] = self._list_lens
        _fen_tree = self._fen_tree
        for i in range(len(_fen_tree)):
            if i | i + 1 < len(_fen_tree):
                _fen_tree[i | i + 1] += _fen_tree[i]
        self._rebuild = False

    def _fen_update(self, index, value):
        """Update `fen_tree[index] += value`."""
        if not self._rebuild:
            _fen_tree = self._fen_tree
            while index < len(_fen_tree):
                _fen_tree[index] += value
                index |= index + 1

    def _fen_query(self, end):
        """Return `sum(_fen_tree[:end])`."""
        if self._rebuild:
            self._fen_build()

        _fen_tree = self._fen_tree
        x = 0
        while end:
            x += _fen_tree[end - 1]
            end &= end - 1
        return x

    def _fen_findkth(self, k):
        """Return a pair of (the largest `idx` such that `sum(_fen_tree[:idx]) <= k`, `k - sum(_fen_tree[:idx])`)."""
        _list_lens = self._list_lens
        if k < _list_lens[0]:
            return 0, k
        if k >= self._len - _list_lens[-1]:
            return len(_list_lens) - 1, k + _list_lens[-1] - self._len
        if self._rebuild:
            self._fen_build()

        _fen_tree = self._fen_tree
        idx = -1
        for d in reversed(range(len(_fen_tree).bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < len(_fen_tree) and k >= _fen_tree[right_idx]:
                idx = right_idx
                k -= _fen_tree[idx]
        return idx + 1, k

    def _delete(self, pos, idx):
        """Delete value at the given `(pos, idx)`."""
        _lists = self._lists
        _mins = self._mins
        _list_lens = self._list_lens

        self._len -= 1
        self._fen_update(pos, -1)
        del _lists[pos][idx]
        _list_lens[pos] -= 1

        if _list_lens[pos]:
            _mins[pos] = _lists[pos][0]
        else:
            del _lists[pos]
            del _list_lens[pos]
            del _mins[pos]
            self._rebuild = True

    def _loc_left(self, value):
        """Return an index pair that corresponds to the first position of `value` in the sorted list."""
        if not self._len:
            return 0, 0

        _lists = self._lists
        _mins = self._mins

        lo, pos = -1, len(_lists) - 1
        while lo + 1 < pos:
            mi = (lo + pos) >> 1
            if value <= _mins[mi]:
                pos = mi
            else:
                lo = mi

        if pos and value <= _lists[pos - 1][-1]:
            pos -= 1

        _list = _lists[pos]
        lo, idx = -1, len(_list)
        while lo + 1 < idx:
            mi = (lo + idx) >> 1
            if value <= _list[mi]:
                idx = mi
            else:
                lo = mi

        return pos, idx

    def _loc_right(self, value):
        """Return an index pair that corresponds to the last position of `value` in the sorted list."""
        if not self._len:
            return 0, 0

        _lists = self._lists
        _mins = self._mins

        pos, hi = 0, len(_lists)
        while pos + 1 < hi:
            mi = (pos + hi) >> 1
            if value < _mins[mi]:
                hi = mi
            else:
                pos = mi

        _list = _lists[pos]
        lo, idx = -1, len(_list)
        while lo + 1 < idx:
            mi = (lo + idx) >> 1
            if value < _list[mi]:
                idx = mi
            else:
                lo = mi

        return pos, idx

    def add(self, value):
        """Add `value` to sorted list."""
        _load = self._load
        _lists = self._lists
        _mins = self._mins
        _list_lens = self._list_lens

        self._len += 1
        if _lists:
            pos, idx = self._loc_right(value)
            self._fen_update(pos, 1)
            _list = _lists[pos]
            _list.insert(idx, value)
            _list_lens[pos] += 1
            _mins[pos] = _list[0]
            if _load + _load < len(_list):
                _lists.insert(pos + 1, _list[_load:])
                _list_lens.insert(pos + 1, len(_list) - _load)
                _mins.insert(pos + 1, _list[_load])
                _list_lens[pos] = _load
                del _list[_load:]
                self._rebuild = True
        else:
            _lists.append([value])
            _mins.append(value)
            _list_lens.append(1)
            pos = self._len
            self._rebuild = True
        return pos

    def discard(self, value):
        """Remove `value` from sorted list if it is a member."""
        _lists = self._lists
        if _lists:
            pos, idx = self._loc_right(value)
            if idx and _lists[pos][idx - 1] == value:
                self._delete(pos, idx - 1)

    def remove(self, value):
        """Remove `value` from sorted list; `value` must be a member."""
        _len = self._len
        self.discard(value)
        if _len == self._len:
            raise ValueError('{0!r} not in list'.format(value))

    def pop(self, index=-1):
        """Remove and return value at `index` in sorted list."""
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        value = self._lists[pos][idx]
        self._delete(pos, idx)
        return value

    def bisect_left(self, value):
        """Return the first index to insert `value` in the sorted list."""
        pos, idx = self._loc_left(value)
        return self._fen_query(pos) + idx

    def bisect_right(self, value):
        """Return the last index to insert `value` in the sorted list."""
        pos, idx = self._loc_right(value)
        return self._fen_query(pos) + idx

    def count(self, value):
        """Return number of occurrences of `value` in the sorted list."""
        return self.bisect_right(value) - self.bisect_left(value)

    def __len__(self):
        """Return the size of the sorted list."""
        return self._len

    def __getitem__(self, index):
        """Lookup value at `index` in sorted list."""
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        return self._lists[pos][idx]

    def __delitem__(self, index):
        """Remove value at `index` from sorted list."""
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        self._delete(pos, idx)

    def __contains__(self, value):
        """Return true if `value` is an element of the sorted list."""
        _lists = self._lists
        if _lists:
            pos, idx = self._loc_left(value)
            return idx < len(_lists[pos]) and _lists[pos][idx] == value
        return False

    def __iter__(self):
        """Return an iterator over the sorted list."""
        return (value for _list in self._lists for value in _list)

    def __reversed__(self):
        """Return a reverse iterator over the sorted list."""
        return (value for _list in reversed(self._lists) for value in reversed(_list))

    def __repr__(self):
        """Return string representation of sorted list."""
        return 'SortedList({0})'.format(list(self))

class LazySegmentTree:
    def __init__(self, size):
        self.size = size
        self.tree = make_arr(self.size << 1)(Node)
    
    def build(self, handler):
        self.traverse_all(handler)

    def get_id(self, l, r):
        return l + r | (l != r)
    
    def get_node(self, l, r):
        return self.tree[self.get_id(l, r)]
    

    def traverse_all(self, handler, l=0, r=None):
        if r == None: r = self.size - 1
        if l == r:
            handler(l, r, self.get_node(l, r))
            return
        m = (l+r) >> 1
        lr, lm, mr = self.get_node(l, r), self.get_node(l, m), self.get_node(m+1, r)
        self.down(l, m, r, lr, lm, mr)
        self.traverse_all(handler, l, m)
        self.traverse_all(handler, m+1, r)
        self.up(l, m, r, lr, lm, mr)
    
    def traverse(self, handler, L, R, l=0, r=None):
        if r == None: r = self.size - 1
        if R < l or r < L or L > R: return
        if L <= l and r <= R:
            handler(l, r, self.get_node(l, r))
            return
        m = (l+r) >> 1
        lr, lm, mr = self.get_node(l, r), self.get_node(l, m), self.get_node(m+1, r)
        self.down(l, m, r, lr, lm, mr)
        self.traverse(handler, L, R, l, m)
        self.traverse(handler, L, R, m+1, r)
        self.up(l, m, r, lr, lm, mr)
        
    def query_all(self):
        return self.get_node(0, self.size-1).m

    def query(self, L, R):
        self.ret = Monoid(True)
        def handler(l, r, u):
            self.ret *= u.m
        self.traverse(handler, L, R)
        return self.ret

    def up(self, l, m, r, u, lu, ru):
        u.m = lu.m * ru.m

    def update(self, L, R, dt):
        def handler(l, r, u):
            u.update(l, r, dt)
        self.traverse(handler, L, R)
    
    def down(self, l, m, r, u, lu, ru):
        if u.tag > 0:
            # TODO how to pass value down
            lu.update(l, m, u.tag)
            ru.update(m+1, r, u.tag)
            u.tag = 0
    

class Monoid:
    def __init__(self, id_ = False, val = 0):
        self.id_ = id_
        # TODO how to set value
        self.val = val
    
    def identity(self):
        return Monoid(True)

    def is_identity(self):
        return self.id_

    def __mul__(self, other):
        if self.is_identity(): return other
        if other.is_identity(): return self
        # TODO how to merge two monoids
        # example sum: Monoid(False, self.val + other.val)
        # example min: Monoid(False, min(self, val, other.val))
        return Monoid(False, self.val + other.val)
    
    def __repr__(self):
        return f'{self.val}'
    
    def __str__(self):
        return f'Monoid::{self.id_} {self.val}'
    
class Node:
    def __init__(self):
        self.m = Monoid()
        self.tag = 0
    
    def update(self, l, r, dt):
        # TODO how to update nodes
        self.m.val += dt * (r-l+1)
        self.tag += dt
    
    def __repr__(self):
        return f'{self.m.val}'


def solve(cas):
    n, m = inp()
    segs = LazySegmentTree(n+1)
    st = SortedList()
    for i in range(n):
        st.add((i, i))
    st.add((n, 0))
    # debug(st)

    for _ in range(m):
        a = inp(lambda x: int(x)-1)
        if a[0] == 0:
            it = st.bisect_left((a[1], -1))
            L, z = st[it]
            if a[2] < L:
                z = st[it-1][1]
                st.add((a[2], z))
            if a[1] < L:
                z = st[it-1][1]
                # debug(a[1], L-1, a[3], z)
                segs.update(a[1], L-1, abs(a[3]-z))
            while st[it][0] <= a[2]:
                L, z = st[it]
                # debug(L, z)
                st.remove((L, z))
                R = st[it][0]
                # debug(st[it])
                if a[2]+1 < R:
                    it = st.add((a[2]+1, a[3]))
                    R = a[2]+1
                # debug(L, R-1, a[3], z)
                segs.update(L, R-1, abs(a[3]-z))
            st.add((a[1], a[3]))
            # debug(st)
        else:
            print(segs.query(a[1], a[2]).val)
            

cas = 1
for _ in range(cas):
    solve(_)

