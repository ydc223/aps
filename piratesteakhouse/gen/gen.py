import random

MAXN = int(1e5)
def largest_time(delay, time):
  res = "%d %d\n"%(MAXN, MAXN-1)
  for i in range(1,MAXN):
    if (delay == -1):
      res += '%d %d %d\n'%(i,i+1, -1)
    else:
      res += '%d %d %d\n'%(i,i+1, MAXN-i)
  
  k, t = MAXN-1, time
  res += "%d %d\n"%(k, t)
  for i in range(2,MAXN+1):
    res += str(i)+" "

  res = res.strip()
  res += "\n"
  return res

def gen_largest():
  with open('../data/secret/001-secret1.in', 'w+') as fp:
    fp.write(largest_time(0, 1))

def gen_largest_delay():
  with open("../data/secret/006-secret6.in", "w+") as fp:
    fp.write(largest_time(-1, 1e9))


def random_cases_connected():
  n = random.randint(2e4, MAXN+1)
  all_vertices = set(i for i in range(2, n+1))
  used_vertices = set()
  random_vertex = 1
  res = "" 
  m = 0
  while len(all_vertices) > 0:
    end_vertex = random.sample(all_vertices, 1)[0]
    if end_vertex in used_vertices or end_vertex == random_vertex: 
      continue
    m += 1
    if m > 2*MAXN: break
    rand_delay = random.randint(1,1e9)
    rand_chance = random.random()
    if rand_chance < 0.5:
      rand_delay = -1
    res += "%d %d %d\n"%(random_vertex, end_vertex, rand_delay)
    used_vertices.add(end_vertex)
    all_vertices.remove(end_vertex)
    random_vertex = end_vertex

  output = "%d %d\n"%(n, m)
  output += res

  k = random.randint(1,n)
  t = random.randint(1,1e9+1)
  output += "%d %d\n"%(k, t)
  vertices = list(used_vertices)
  for i in random.sample(vertices, k):
    output += "%d "%i
  output.strip()
  output += "\n"
  return output


def gen_random_cases():
  with open('../data/secret/007-secret7.in', 'w+') as fp:
    fp.write(random_cases_connected())

gen_largest()
gen_largest_delay()
gen_random_cases()


