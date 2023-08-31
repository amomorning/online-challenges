import collections, math, bisect, heapq, random, functools, itertools, copy, typing
import platform; LOCAL = (platform.uname().node == 'AMO')


import sys; input = lambda: sys.stdin.readline().rstrip("\r\n")
inp = lambda : list(map(int, input().split()))

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

EPS = 1e-6
INF = 1e100
def cmp(x): return -1 if x < -EPS else int(x > EPS)

def polar_cmp(a, b):
    if cmp(a.y) * cmp(b.y) <= 0:
        if cmp(a.y) > 0 or cmp(b.y) > 0: return cmp(a.y - b.y)
        if cmp(a.y) == 0 and cmp(b.y) == 0: return cmp(a.x - b.x)
    return cmp(a.cross(b)) 

def find_points_in_aabb(xs, ys, aabb, boundary=True):
    """ pts: Sorted Points in [(x, y, id), ...]
        aabb: [[minx, miny], [maxx, maxy]]
        Returns: index list
    """
    if boundary:
        xl = bisect.bisect_right(xs, (aabb[0][0]-EPS, -1))
        xr = bisect.bisect_left(xs, (aabb[1][0]+EPS, -1))

        yl = bisect.bisect_right(ys, (aabb[0][1]-EPS, -1))
        yr = bisect.bisect_left(ys, (aabb[1][1]+EPS, -1))
    
    else:
        xl = bisect.bisect_left(xs, (aabb[0][0]+EPS, -1))
        xr = bisect.bisect_right(xs, (aabb[1][0]-EPS, -1))

        yl = bisect.bisect_left(ys, (aabb[0][1]+EPS, -1))
        yr = bisect.bisect_right(ys, (aabb[1][1]-EPS, -1))
    idx = set([x[1] for x in xs[xl:xr]])
    idy = set([y[1] for y in ys[yl:yr]])
    return idx & idy

class Point:
    def __init__(self, *args):
        if len(args) == 1:
            args = args[0]
        self.__v = list(args)
        
    def __len__(self):
        return len(self.__v)

    def __str__(self):
        return 'Point' + str(tuple(self.__v))

    def __repr__(self):
        return 'Point' + str(tuple(self.__v))

    def print(self):
        return ' '.join(map(str, self.__v))
    
    def __hash__(self):
        return hash(tuple(self.__v))
        
    def __getitem__(self, key):
        if type(key) is int or slice:
            return self.__v[key]

    def __getattr__(self, key):
        if key == 'x':
            return self.__v[0]
        if key == 'y':
            return self.__v[1]
        if key == 'z':
            return self.__v[2]
        if key == 'w':
            return self.__v[3]
        raise KeyError('Invalid key: %s' % key)
    
    def __setitem__(self, key, value):
        if type(key) is int and key < len(self.__v):
            self.__v[key] = value
        if key == 'x':
            self.__v[0] = value
        if key == 'y':
            self.__v[1] = value
        if key == 'z':
            self.__v[2] = value
        if key == 'w':
            self.__v[3] = value        
        raise KeyError('Invalid key: %s' % key)
        
    def __neg__(self):
        ret = []
        for x in self:
            ret.append(-x)
        return Point(ret)
    
    def __eq__(self, rhs):
        if type(rhs) != Point: rhs = Point(rhs)
        assert len(rhs) == len(self)

        for i in range(len(self)):
            if cmp(self[i] - rhs[i]) != 0:
                return False
        return True
        
    def __le__(self, rhs):
        if type(rhs) != Point: rhs = Point(rhs)
        assert len(rhs) == len(self)

        for i in range(len(self)):
            if cmp(self[i] - rhs[i]) < 0:
                return True
            if cmp(self[i] - rhs[i]) > 0:
                return False
        return True
        
    def __lt__(self, rhs):
        if type(rhs) != Point: rhs = Point(rhs)
        assert len(rhs) == len(self)

        for i in range(len(self)):
            if cmp(self[i] - rhs[i]) < 0:
                return True
            if cmp(self[i] - rhs[i]) > 0:
                return False
        return False
    
    def __add__(self, rhs):
        if type(rhs) != Point: rhs = Point(rhs)
        ret = []        
        for i in range(len(self)):
            ret.append(self[i] + rhs[i])
        return Point(ret)

    def __sub__(self, rhs):
        return self + (-rhs)
    
    def __mul__(self, scale):
        ret = []
        for x in self:
            ret.append(x * scale)
        return Point(ret)

    def __rmul__(self, scale):
        return self * scale
    
    def __truediv__(self, scale):
        return self * (1.0/scale)
    
    def __floordiv__(self, scale):
        ret = []
        for x in self:
            ret.append(x // scale)
        return Point(ret)
    
    def __matmul__(self, rhs):
        if type(rhs) != Point: rhs = Point(rhs)
        ret = []
        for i in range(len(rhs)):
            ret.append(self[i] * rhs[i])
        return Point(ret)
    
    def __pow__(self, scale):
        tot = 0
        for x in self:
            tot += x ** scale
        return tot
    
    def __abs__(self):
        return (self ** 2) ** 0.5
    
    @property
    def polar(self):
        assert len(self) == 2
        return self.norm(), 

    
    def norm(self, v = 2, maxd = 50):
        return (self ** v) ** (1.0/v) if v <= maxd else max(self)
    
    def normalized(self):
        return self / self.norm() 
    
    def dot(self, rhs):
        if type(rhs) != Point: rhs = Point(rhs)
        return sum(self @ rhs)
    
    def cross(self, rhs):
        if type(rhs) != Point: rhs = Point(rhs)
        if len(self.__v) == 3:
            a, b, c = self
            x, y, z = rhs
            return Point(-c*y + b*z, c*x - a*z, -b*x + a*y)
        elif len(self.__v) == 2:
            return self.x * rhs.y - self.y * rhs.x
        raise ValueError("Invalid coordinates")

        
    def proj(self, rhs):
        if type(rhs) != Point: rhs = Point(rhs)
        return rhs * self.dot(rhs) / rhs.dot(rhs)
    
    def select(self, dim):
        assert len(dim) > 1
        return Point([self[d] for d in dim])
    
    # Quaternion
    def conj(self):
        ret = [self[0]]
        for i in range(1, len(self)):
            ret.append(-self[i])
        return Point(ret)
    
    def inv(self):
        l2 = self.dot(self)
        return self.conj() / l2

    def mulq(self, rhs):
        assert len(self.__v)  == 4
        if type(rhs) != Point: rhs = Point(rhs)

        q0, q1, q2, q3 = self
        p0, p1, p2, p3 = rhs

        return Point(q0*p0 - q1*p1 - q2*p2 - q3*p3, \
                     q0*p1 + q1*p0 + q2*p3 - q3*p2, \
                     q0*p2 - q1*p3 + q2*p0 + q3*p1, \
                     q0*p3 + q1*p2 - q2*p1 + q3*p0)

    # rotate
    def rotate(self, angle):
        assert len(self.__v) == 2
        c, s = math.cos(angle), math.sin(angle)
        return Point(self.x * c - self.y * s, self.x * s + self.y * c)
        
    def rotate_90(self):
        assert len(self.__v) == 2
        return Point(-self.y, self.x)
    
    def rotate_x(self, angle):
        assert len(self.__v)  == 3
        c, s = math.cos(angle), math.sin(angle)
        x, y, z = self
        return Point(x, y * c - z * s, y * s + z * c)
    
    def rotate_y(self, angle):
        assert len(self.__v)  == 3
        c, s = math.cos(angle), math.sin(angle)
        x, y, z = self
        return Point(x * c + z * s, y, -x * s + z * c)

    def rotate_z(self, angle):
        assert len(self.__v)  == 3
        c, s = math.cos(angle), math.sin(angle)
        x, y, z = self
        return Point(x * c - y * s, x * s + y * c, z)
    
    def rotate_by(self, axis, angle):
        assert len(self.__v)  == 3
        if type(axis) != Point: axis = Point(axis)
        
        c, s = math.cos(angle), math.sin(angle)
        x, y, z = self
        ux, uy, uz = axis.normalized()

        return Point((c+ux*ux*(1-c))*x + (ux*uy*(1-c)-uz*s)*y + (ux*uz*(1-c)+uy*s)*z, \
                     (uy*ux*(1-c)+uz*s)*x + (c+uy*uy*(1-c))*y + (uy*uz*(1-c)-ux*s)*z, \
                     (uz*ux*(1-c)-uy*s)*x + (uz*uy*(1-c)+ux*s)*y + (c+uz*uz*(1-c))*z)

    def rotate_by_quaternion(self, axis, angle): 
        assert len(self.__v) == 3
        if type(axis) != Point: axis = Point(axis)
        axis = axis.normalized() * math.sin(angle*0.5)
        q = Point(math.cos(angle*0.5), axis.x, axis.y, axis.z)
        return self.apply_quaternion(q)

    def apply_quaternion(self, q):
        p = Point(1.0, self.x, self.y, self.z)
        return Point(q.mulq(p).mulq(q.inv())[1:])

    def apply_matrix(self, m):
        """ row major matrix 
        """
        n = len(self)

        ret = []
        for i in range(n):
            tot = 0
            for j in range(n):
                tot += self[j] * m[i][j]
            ret.append(tot)

        return Point(ret)
class Plane:
    def __init__(self, base, normal):
        self.base = base
        self.normal = normal
        self.normal.normalized()
    
    def project_point(self, point):
        vector = point - self.base
        return vector - vector.proj(self.normal)
    
    def project_segment(self, segment):
        a = self.project_point(segment.a)
        b = self.project_point(segment.b)
        return Segment(a, b)
    
    def to_plane(self, plane):
        move = self.base - plane.base

class Segment:
    def __init__(self, a, b):
        self.a = Point(a)
        self.b = Point(b)

    def __getitem__(self, item):
        if item == 0: return self.a
        if item == 1: return self.b
        raise KeyError('Invalid item: %s' % item)

    def __str__(self) -> str:
        return 'Line: [' + str(self.a) + ', ' + str(self.b) + ']'

    def __repr__(self):
        return 'Line: [' + str(self.a) + ', ' + str(self.b) + ']'

    @property
    def length(self):
        return abs(self.a - self.b)

    @property
    def length_square(self):
        return (self.a - self.b) ** 2

    def on_point(self, point):
        if type(point) != Point: point = Point(point)
        u, v = self.a - point, self.b - point
        return cmp(u.cross(v)) == 0 and cmp(u.dot(v)) <= 0

    def lerp(self, t):
        return (1 - t) * self.a + t * self.b

    def project_on(self, dim):
        return Segment(self.a.select(dim), self.b.select(dim))

    def is_proper_intersect(self, line):
        assert len(self.a) == 2
        c1 = (self.b - self.a).cross(line.a - self.a)
        c2 = (self.b - self.a).cross(line.b - self.a)
        c3 = (line.b - line.a).cross(self.a - line.a)
        c4 = (line.b - line.a).cross(self.b - self.a)
        return c1 * c2 < 0 and c3 * c4 < 0

    def is_intersect(self, line):
        if self.is_proper_intersect(line):
            return True
        return self.on_point(line.a) or self.on_point(line.b) or \
               line.on_point(self.a) or line.on_point(self.b)

    def intersection(self, line):
        if len(line.a) == 3:
            return self.intersection_3d(line)

        if not self.is_intersect(line):
            return None
        u, v, w = line.a - self.a, self.b - self.a, line.b - line.a
        if cmp(v.cross(w)) == 0:
            if line.on_point(self.a):
                return self.a
            if line.on_point(self.b):
                return self.b
            return None
        t = w.cross(u) / w.cross(v)
        # debug(t)
        return self.lerp(t)

    def intersection_3d(self, line):
        assert len(self.a) == 3

        x_p = self.project_on((1, 2)).intersection(line.project_on((1, 2)))
        y_p = self.project_on((0, 2)).intersection(line.project_on((0, 2)))
        z_p = self.project_on((0, 1)).intersection(line.project_on((0, 1)))

        if x_p is None or y_p is None or z_p is None:
            return None

        for x in [y_p.x, z_p.x]:
            for y in [x_p.x, z_p.y]:
                for z in [x_p.y, y_p.y]:
                    pt = Point(x, y, z)
                    if self.on_point(pt) and line.on_point(pt):
                        return pt
        return None

    def project_point(self, point):
        u, v = point - self.a, self.b - self.a
        return self.a + u.proj(v)

    def divide_by_distance(self, distance):
        n = math.ceil(self.length / distance)
        pts = []
        for i in range(n):
            t = i * distance / self.length
            if cmp(t - 1) <= 0:
                pts.append(self.lerp(t))
        return pts

    def divide_by_num(self, num):
        distance = self.length / num
        return self.divide_by_distance(distance-EPS)

    def distance(self, rhs):
        if type(rhs) == Point:
            u, v, w = self.b - self.a, rhs - self.a, rhs - self.b
            if cmp(u.dot(v)) < 0:
                return abs(v)
            elif cmp(u.dot(w)) > 0:
                return abs(w)
            else:
                return abs(u.cross(v)) / abs(u)

        if type(rhs) == Segment:
            if self.intersection(rhs) != None:
                return 0
            ret = min(self.distance(rhs.a), self.distance(rhs.b))
            ret = min(ret, min(rhs.distance(self.a), rhs.distance(self.b)))

            if len(self.a) == 3:
                """ Reference
                    for line line distance
                    [1] https://mathworld.wolfram.com/Line-LineDistance.html
                
                    # a, b, c = self.b - self.a, rhs.b - rhs.a, rhs.a - self.a
                    # return abs(a.cross(b).dot(c)) / abs(a.cross(b))

                    but here we should calculate the distance between two segments
                    [2] https://zalo.github.io/blog/closest-point-between-segments/
                """
                p = Plane(self.a, self.b - self.a)
                line = p.project_segment(rhs)
                closest = line.project_point(self.a)
                if line.on_point(closest):
                    ret = min(ret, line.distance(self.a))

            return ret

        raise NotImplementedError("distance is not implemented for type %s" % type(rhs))


class Triangle:
    def __init__(self, a, b, c):
        self.a = Point(a)
        self.b = Point(b)
        self.c = Point(c)
    
    def __getitem__(self, key):
        if key == 0:
            return self.a
        if key == 1:
            return self.b
        if key == 2:
            return self.c
        raise KeyError('Invalid item: %s' % key)
    
    def __str__(self) -> str:
        return 'Triangle: [' + str(self.a) + ', ' + str(self.b) + ', ' + str(self.c) + ']'

    @property
    def normal(self):
        assert len(self.a) == 3
        b, c = self.b - self.a, self.c - self.a
        return b.cross(c).normalized()

    @property
    def aabb(self):
        d = len(self.a)
        mn = [math.inf] * d
        mx = [-math.inf] * d
        for i in range(3):
            for j in range(d):
                mn[j] = min(mn[j], self[i][j])
                mx[j] = max(mx[j], self[i][j])
        return mn, mx
    
    @property
    def centroid(self):
        return (self.a + self.b + self.c) / 3.0
    
    def area(self, doubled = False):
        b, c = self.b - self.a, self.c - self.a
        self.A = b.cross(c)
        if not doubled: self.A /= 2
        return self.A
    
    def incircle(self):
        """ Reference
            [1] Heron's formula: https://en.wikipedia.org/wiki/Heron%27s_formula
        """
        a = abs(self.b - self.c)
        b = abs(self.a - self.c)
        c = abs(self.a - self.b)
        s = (a + b + c)/2
        r = math.sqrt((s-a)*(s-b)*(s-c)/s)
        return (a*self.a + b*self.b + c*self.c)/(a+b+c), r
    
    def circumcircle(self):
        """ Reference
            [1] https://en.wikipedia.org/wiki/Circumscribed_circle#Cartesian_coordinates_from_cross-_and_dot-products
        """
        a = self.b - self.c # p2-p3
        b = self.c - self.a # p3-p1
        c = self.a - self.b # p1-p2
        r = abs(a)*abs(b)*abs(c)/(abs(b.cross(a) + EPS) * 2)

        tmp = - c.cross(a)**2 * 2
        alpha = a**2 * c.dot(b) 
        beta = b**2 * c.dot(a) 
        gamma = c**2 * b.dot(a) 
        return (alpha*self.a + beta*self.b + gamma*self.c) / tmp, r

    def inside_point(self, p):
        assert len(p) == len(self.a)
        if len(p) == 2:
            p, b, c = p - self.a, self.b - self.a, self.c - self.a
            if b.cross(c) < 0:
                b, c = c, b
            if b.cross(p) < 0 or p.cross(c) < 0 or (c-b).cross(p-b) < 0:
                return False
            return True
        if len(p) == 3:
            p, b, c = p - self.a, self.b - self.a, self.c - self.a
            def is_zero(v):
                if cmp(abs(v)) == 0: return True
                if cmp(abs(v.normalized()-self.normal)) == 0: return True
                return False            

            if is_zero(b.cross(p)) and is_zero(p.cross(c)) and is_zero((c-b).cross(p-b)):
                return True
            return False
        raise NotImplementedError("Higher dimensions are not supported")
            

    def uniform_sample(self, num):
        """ Reference: 
            [1] https://math.stackexchange.com/questions/18686/uniform-random-point-in-triangle-in-3d
        """
        ret = []
        for i in range(num):
            r1 = random.uniform(0, 1)
            r2 = random.uniform(0, 1)
            p = self.a * (1-math.sqrt(r1)) + self.b * math.sqrt(r1)*(1-r2)\
                + self.c * math.sqrt(r1)*r2
            ret.append(p)
            
        return ret
    
    def uniform_sample_parallelogram(self, num):
        b, c = self.b - self.a, self.c - self.a
        ret = []
        for _ in range(num):
            p = b * random.uniform(0, 1) + c * random.uniform(0, 1)

            if not self.inside_point(p+self.a):
                p = b + c - p
            ret.append(p+self.a)
        return ret
    
    def uniform_sample_rectangle(self, num):
        mn, mx = self.aabb
        ret = []
        for _ in range(num):
            x = random.uniform(mn[0], mx[0])
            y = random.uniform(mn[1], mx[1])
            while not self.inside_point(Point(x, y)):
                x = random.uniform(mn[0], mx[0])
                y = random.uniform(mn[1], mx[1])
            ret.append(Point(x, y))
        return ret


class Polygon:
    """ 2D Polygon Implementation
    """

    def __init__(self, *args) -> None:
        if len(args) == 1:
            args = args[0]
        self.points = [Point(pt[0], pt[1]) for pt in args]
        self.__center = None
        self.__convex = None
        self.__area = None
        self.A = None

    def __getitem__(self, key):
        return self.points[key]

    def __setitem__(self, key, value):
        self.points[key] = Point(value)

    def __str__(self):
        return 'Polygon[%s]' % ', '.join(map(str, self.points))

    def __len__(self):
        return len(self.points)

    def __iter__(self):
        return iter(self.points)

    @property
    def is_convex(self):
        if self.__convex is not None:
            return self.__convex

        self.__convex = True
        for p0, p1, p2 in zip(self.points, self.points[1:]+self.points[:1], self.points[2:]+self.points[:2]):
            if (p1 - p0).cross(p2 - p0) < 0:
                self.__convex = False
                return self.__convex
        return self.__convex

    @property
    def angles(self):
        angles = []
        for p1, p0, p2 in zip(self.points[-1:]+self.points[:-1], self.points, self.points[1:]+self.points[:1]):
            a, b, c = p1 - p0, p2 - p0, p1 - p2
            tmp = (a ** 2 + b ** 2 - c ** 2) / abs(a) / abs(b) / 2
            # print(abs(a), abs(b))
            # print(tmp)
            if tmp > 1:
                tmp -= EPS
            elif tmp < -1:
                tmp += EPS
            # print(tmp, a, b, c)

            angle = math.acos(tmp)
            if b.cross(a) < 0:
                angle = math.pi * 2 - angle
            angles.append(angle)
        return angles

    @property
    def segments(self):
        return [Segment(p0, p1) for p0, p1 in zip(self.points, self.points[1:]+self.points[:1])]

    @property
    def triangles(self):
        tris = []
        if self.is_convex:
            p0 = self.points[0]
            for p1, p2 in zip(self.points[1:], self.points[2:]):
                tris.append(Triangle(p0, p1, p2))
        else:
            trids = self.earcut()
            for a, b, c in trids:
                tris.append(Triangle(self.points[a], self.points[b], self.points[c]))
        return tris

    @property
    def length(self):
        return sum([seg.length for seg in self.segments])

    def signed_area(self, double=True):
        A = 0
        p0 = self.points[0]
        for p1, p2 in zip(self.points[1:], self.points[2:]):
            A += (p1 - p0).cross(p2 - p0)
        return A

    def area(self, doubled=False):
        self.A = 0
        for tri in self.triangles:
            self.A += tri.area(True)
        if not doubled: self.A /= 2
        return self.A

    def centroid(self):
        self.__center = Point(0.0, 0.0)
        for tri in self.triangles:
            self.__center += tri.area() * tri.centroid
        return self.__center / self.area()

    def remove_inline_points(self, eps=1e-6):
        if len(self.points) <= 3:
            return self.points
        pts = []
        l = self.points[-1]
        for m, r in zip(self.points, self.points[1:]+self.points[:1]):
            if abs(r - m) < eps:
                continue
            if abs((l - m).cross(r - m)) < eps:
                continue
            pts.append(m)
            l = m
        self.points = pts
        return pts

    def earcut(self):
        """ Reference
            [1] https://www.geometrictools.com/Documentation/TriangulationByEarClipping.pdf
        """
        n, p = len(self.points), self.points
        prev_ = [n - 1] + list(range(n - 1))
        next_ = list(range(1, n)) + [0]
        convex, refvex = [], set()
        for i in range(n):
            if (p[prev_[i]] - p[i]).cross(p[next_[i]] - p[i]) < 0:
                convex.append(i)
            elif (p[prev_[i]] - p[i]).cross(p[next_[i]] - p[i]) > 0:
                refvex.add(i)
        vis, res = [0] * n, []
        xs = sorted([(p[i].x, i) for i in range(n)])
        ys = sorted([(p[i].y, i) for i in range(n)])
        while convex:
            m = convex.pop()
            if vis[m] == 1 or n - len(res) < 3:
                continue
            l, r = prev_[m], next_[m]

            tri = Triangle(p[l], p[m], p[r])
            ids = find_points_in_aabb(xs, ys, tri.aabb, False) & refvex
            is_ear = True
            for i in ids:
                if i == l or i == r: continue
                is_ear &= (not tri.inside_point(p[i]))
                if not is_ear: break
            # debug(l, m, r, is_ear)
            if is_ear:
                res.append((l, m, r))
                vis[m] = 1
                next_[l] = r
                prev_[r] = l
                for i in [l, r]:
                    if (p[prev_[i]] - p[i]).cross(p[next_[i]] - p[i]) <= 0:
                        convex.append(i)
                        refvex.discard(i)
        return res

    def inside_point(self, p, boundary=True):
        t = 0
        for seg in self.segments:
            if seg.on_point(p):
                return boundary
            a, b = seg[0], seg[1]
            if cmp(a.y - b.y) > 0: a, b = b, a
            if cmp((a - p).cross(b - p)) < 0 and cmp(a.y - p.y) < 0 and cmp(p.y - b.y) <= 0:
                t += 1
        return bool(t & 1)

    def divide_by_distance(self, distance):
        remain = 0
        pts = []
        for seg in self.segments:
            remain += seg.length
            while cmp(remain - distance) >= 0:
                remain -= distance
                t = (seg.length - remain) / seg.length
                pts.append(seg.lerp(t))
        return pts

    def divide_by_ray(self, n, center=None):
        if center is None: center = self.centroid()
        radius = 0
        pts = []
        for p in self.points:
            radius = max(radius, (p - center).norm())
        for i in range(n):
            angle = 2 * i * math.pi / n
            x, y = radius * math.cos(angle), radius * math.sin(angle)
            ray = Segment(center, center + Point(x, y))
            mn = math.inf
            for seg in self.segments:
                p = seg.intersection(ray)
                if p is None: continue
                if (p - center).norm() < mn:
                    mn = (p - center).norm()
                    mnp = p
            pts.append(mnp)
        return pts

    def offset(self, distance):
        n = len(self.points)
        pts = []
        for i in range(n):
            p0, p1, p2 = self.points[i], self.points[(i - 1) % n], self.points[(i + 1) % n]
            p, q = (p1 - p0) / abs(p1 - p0), (p2 - p0) / abs(p2 - p0)

            r = distance / math.sin(self.angles[i] / 2)
            if q.cross(p) < 0:
                r = -r
            d = -(p + q).normalized() * r
            pts.append(p0 + d)
        return Polygon(pts)

class ConvexHull:
    def __init__(self, points):
        self.points = list(map(Point, points))
        self.build()

    def add_point(self, point):
        self.points.append(point)
        self.build()
    
    def build(self):
        pts = sorted(self.points)
        n, k = len(pts), 0
        convex = [None] * (n*2)
        for p in pts:
            while k > 1 and cmp((convex[k-1] - p).cross(convex[k-2] - p)) <= 0:
                k -= 1
            convex[k] = p
            k += 1
        t = k
        for p in pts[-2::-1]:
            while k > t and cmp((convex[k-1] - p).cross(convex[k-2] - p)) <= 0:
                k -= 1
            convex[k] = p
            k += 1
        
        self.points = convex[:min(n,k-1)]
        self.polygon = Polygon(self.points)
    

    def diameter(self, squared=False):
        j, d = 0, 0
        n = len(self.points)

        if n <= 1: return 0, []
        if n == 2: return (self.points[0] - self.points[1])**2, [self.points[0], self.points[1]]
        next_ = lambda i: 0 if i+1==n else i+1

        for i in range(n):
            p, q = self.points[i], self.points[next_(i)]
            while cmp((self.points[j] - self.points[next_(j)]).cross(q-p)) <= 0:
                j = next_(j)
            u = self.points[j]
            for v in [p, q]:
                tmp = (u-v)**2
                if tmp > d:
                    d, pts = tmp, [u, v]
        return d, pts if squared else math.sqrt(d), pts


    def smallest_enclosing_box(self):
        n = len(self.points)

        area = 0x3f3f3f3f
        next_ = lambda i: 0 if i+1==n else i+1

        j, l, r = 0, 0, 0

        for i in range(n):
            p, q = self.points[i], self.points[next_(i)]
            while cmp((self.points[j] - self.points[next_(j)]).cross(q-p)) <= 0:
                j = next_(j)
            m = self.points[j]
            while cmp((self.points[r] - self.points[next_(r)]).dot(q-p)) <= 0:
                r = next_(r)
            if i == 0: l = r
            while cmp((self.points[l] - self.points[next_(l)]).dot(p-q)) <= 0:
                l = next_(l)
            seg = self.polygon.segments[i]

            u, v = seg.project_point(self.points[l]), seg.project_point(self.points[r])
            tmp = (u-v).norm() * seg.distance(m)

            if tmp <= area:
                area = tmp
                d = Segment(m, m + q-p)
                uu, vv = d.project_point(self.points[l]), d.project_point(self.points[r])
                pts = [u, v, vv, uu]
            if (pts[1] - pts[2]).cross(pts[0]):
                pts.reverse()
        return area, pts


B = 10**5 + 10
def dijkstra(starts):
    q = []
    for s in starts:
        heapq.heappush(q, d[s] * B + s)

    while q:
        tmp = heapq.heappop(q)
        du, u = tmp//B, tmp%B
        if d[u] < du:
            continue
        # debug(du, u)
        for v, w in G[u]:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                heapq.heappush(q, d[v] * B + v)
            

n, m, k = inp() 
G = [[] for _ in range(n)]
d = [math.inf] * n
d[0] = 0
for i in range(m):
    u, v, w = inp()
    u -= 1; v -= 1
    G[u].append((v, w))
    G[v].append((u, w))
    
starts = [0]
for _ in range(k):
    dijkstra(starts)
    pts = []
    for u in range(n):
        pts.append((-2 * u, u * u + d[u]))
    convex = ConvexHull(pts)
    p = [None] * n
    next_ = lambda i: 0 if i+1==len(convex.points) else i+1

    for i in range(len(convex.points)):
        if convex.points[i].y == 0:
            l = i

    starts = []
    for v in range(n):
        q = Point(v, 1)
        while convex.points[l].dot(q) > convex.points[next_(l)].dot(q):
            # debug(l)
            l = next_(l)
        
        p[v] = min(d[v], convex.points[l].dot(q) + v * v)
        if p[v] < d[v]:
            starts.append(v)
        # debug(v, l, convex.points[l].dot(Point(v, 1)) + v * v)
    d = p

dijkstra(starts)

print(' '.join(map(str, d)))

