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
            if TRACE: print(f'{i}: {mem[x]}+{mem[y]}={mem[x] + mem[y]} @ {p}')
            mem[p] = mem[x] + mem[y]
            i += 4
        elif op == 2:
            x = get(1,c)
            y = get(2,b)
            p = get(3,a)
            if TRACE: print(f'{i}: {mem[x]}*{mem[y]}={mem[x] * mem[y]} @ {p}')
            mem[p] = mem[x] * mem[y]
            i += 4
        elif op == 3:
            p = get(1,c)
            mem[p] = yield
            if TRACE: print(f'{i}: input {mem[p]} @ {p}')
            i += 2
        elif op == 4:
            p = get(1,c)
            if TRACE: print(f'{i}: out {mem[p]} @ {p}')
            yield mem[p]
            i += 2
        elif op == 5:
            x = get(1,c)
            y = get(2,b)
            if TRACE: print(f'{i}: if {mem[x]} jump {mem[y]}')
            if mem[x]:
                i = mem[y]
            else:
                i += 3
        elif op == 6:
            x = get(1,c)
            y = get(2,b)
            if TRACE: print(f'{i}: if not {mem[x]} jump {mem[y]}')
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
