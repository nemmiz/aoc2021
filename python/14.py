def insert(template, rules):
    result = []
    for i in range(1, len(template)):
        pair = template[i-1:i+1]
        e = rules[pair]
        if i == 1:
            result.append(pair[0])
        result.append(e)
        result.append(pair[1])
    return ''.join(result)

def merge(c1, c2):
    keys = set()
    keys.update(c1.keys())
    keys.update(c2.keys())
    return {k: c1.get(k, 0) + c2.get(k, 0) for k in keys}

def counts(pair, rules, rem, cnt, cache):
    #print(pair, rem)
    entry = (pair, rem)
    if entry in cache:
        return cache[entry]

    e = rules[pair]
    if rem == 1:
        if pair[0] == e:
            return {e: 2}
        return {
            pair[0]: 1,
            e: 1,
        }
        #cnt[pair[0]] += 1
        #cnt[e] += 1
        #print(pair)
        #return

    c1 = counts(f'{pair[0]}{e}', rules, rem-1, cnt, cache)
    c2 = counts(f'{e}{pair[1]}', rules, rem-1, cnt, cache)

    result = merge(c1, c2)

    cache[entry] = result

    return result

    # keys = set()
    # keys.update(c1.keys())
    # keys.update(c2.keys())
    # return {k: c1.get(k, 0) + c2.get(k, 0) for k in keys}



def counts_all(template, rules, steps):
    #letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #cnt = {c: 0 for c in letters}
    cache = {}
    cnt = {}
    result = {}
    for i in range(1, len(template)):
        tmp = counts(template[i-1:i+1], rules, steps, cnt, cache)
        result = merge(tmp, result)
    result[template[-1]] += 1
    #print(result)
    #print('Cache size:', len(cache))

    vals = sorted(result.values())
    print(vals[-1] - vals[0])

    # cnt[template[-1]] += 1
    # for c in letters:
    #     n = cnt.get(c, 0)
    #     if n > 0:
    #         print(c, n)

def countchars(template):
    uniq = set(template)
    counts = [(template.count(c), c) for c in uniq]
    counts.sort()
    print(counts)

with open('../input/14.txt') as stream:
    lines = [line.strip() for line in stream.readlines()]
    template = lines[0]
    rules = {}
    for line in lines[2:]:
        a, b = line.split(' -> ')
        rules[a] = b

#print(template)
#print(rules)

counts_all(template, rules, 10)
counts_all(template, rules, 40)

# for i in range(15):
#     print(i, template[:4])
#     #print(i, len(template))
#     template = insert(template, rules)
    

# #print(template)

# uniq = set(template)
# counts = [(template.count(c), c) for c in uniq]
# counts.sort()

# print(counts[-1][0] - counts[0][0])