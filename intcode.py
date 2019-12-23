from collections import defaultdict

def parse(input):
    prog = defaultdict(lambda:0)
    for i,v in enumerate(input.split(',')):
        prog[i] = int(v)
    return prog

TRACE = 0
def run(mem):
    i = 0
    rel = 0
    def get(j,m):
        p = i+j
        if m == 0:
            p = mem[p]
        elif m == 2:
            p = mem[p] + rel
        return p
    while 1:
        s = ('0000'+str(mem[i]))[-5:]
        a,b,c,op = int(s[0]), int(s[1]), int(s[2]), int(s[3:])
        if op == 1:
            x = get(1,c)
            y = get(2,b)
            p = get(3,a)
            if TRACE: print(f'{i}: {mem[x]}+{mem[y]}={mem[x] + mem[y]} => {p} ({mem[p]})')
            mem[p] = mem[x] + mem[y]
            i += 4
        elif op == 2:
            x = get(1,c)
            y = get(2,b)
            p = get(3,a)
            if TRACE: print(f'{i}: {mem[x]}*{mem[y]}={mem[x] * mem[y]} => {p} ({mem[p]})')
            mem[p] = mem[x] * mem[y]
            i += 4
        elif op == 3:
            p = get(1,c)
            if TRACE: print(f'{i}: request ? => {p}')
            mem[p] = yield
            if TRACE: print(f'{i}: store {mem[p]} => {p}')
            i += 2
        elif op == 4:
            p = get(1,c)
            if TRACE: print(f'{i}: out {mem[p]} <- {p}')
            yield mem[p]
            i += 2
        elif op == 5:
            x = get(1,c)
            y = get(2,b)
            if TRACE: print(f'{i}: if ({mem[x]} @ {x}) jump {mem[y]} @ {y}')
            if mem[x]:
                i = mem[y]
            else:
                i += 3
        elif op == 6:
            x = get(1,c)
            y = get(2,b)
            if TRACE: print(f'{i}: if not ({mem[x]} @ {x}) jump {mem[y]} @ {y}')
            if not mem[x]:
                i = mem[y]
            else:
                i += 3
        elif op == 7:
            x = get(1,c)
            y = get(2,b)
            p = get(3,a)
            if TRACE: print(f'{i}: {mem[x]} < {mem[y]} => {p}')
            mem[p] = int(mem[x] < mem[y])
            i += 4
        elif op == 8:
            x = get(1,c)
            y = get(2,b)
            p = get(3,a)
            if TRACE: print(f'{i}: {mem[x]} == {mem[y]} => {p}')
            mem[p] = int(mem[x] == mem[y])
            i += 4
        elif op == 9:
            x = get(1,c)
            if TRACE: print(f'{i}: rel = {rel} + {mem[x]}')
            rel += mem[x]
            i += 2
        elif op == 99:
            return
        else:
            raise Exception('Unknown opcode', op)
            break

def readASCII(proc):
    s = ''
    try:
        q = next(proc)
        while q!=None:
            if s==10:
                print(s)
                s = ''
            else:
                s += chr(q)
            q = next(proc)
    except StopIteration:
        print('stopped')
        pass

    if len(s)>0:
        print(s)
        s = ''

    return q

def sendASCII(proc, txt):
    print(txt)
    s = ''
    try:
        for c in txt:
            q = proc.send(ord(c))
        while q!=None:
            if q==10:
                print(s)
                s = ''
            else:
                if q>0x110000:
                    print('got number', q)
                else:
                    s += chr(q)
            q = next(proc)
    except StopIteration:
        print('stopped')
        pass

    if len(s)>0:
        print(s)
        s = ''
    return q
