import math, operator
EPS = 1e-6
def cmp(x): return -1 if x < -EPS else int(x > EPS)

def polar_cmp(a, b):
    if cmp(a.y) * cmp(b.y) <= 0:
        if cmp(a.y) > 0 or cmp(b.y) > 0: return cmp(a.y - b.y)
        if cmp(a.y) == 0 and cmp(b.y) == 0: return cmp(a.x - b.x)
    return cmp(a.cross(b)) 

class Point:
    def __init__(self, *args):
        if len(args) == 1:
            args = args[0]
        self.__v = list(args)
        
    def __len__(self):
        return len(self.__v)

    def __str__(self):
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


def get_area(p1, p0, p2):
    return (p1 - p0).cross(p2 - p0)

n = int(input())
polygon = []
for i in range(n):
    polygon.append(Point(map(int, input().split())))

S = 0 # 2 times polygon area
p0 = polygon[0]
for p1, p2 in zip(polygon[1:], polygon[2:]):
    S += get_area(p1, p0, p2)

r, area = 1, 0, 
ans = math.inf
A, r, ans = 0, 1, math.inf
for l in range(n):
    ans = min(ans, abs(S - 4 * A))
    if l:
        A -= get_area(polygon[l-1], polygon[r%n], polygon[l])
        ans = min(ans, abs(S - 4 * A))
    while 4 * A <= S:
        A += get_area(polygon[r%n], polygon[l], polygon[(r+1)%n])
        ans = min(ans, abs(S - 4 * A))
        r += 1

print(ans)
