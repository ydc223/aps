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
  with open('../data/secret/004-secret4.in', 'w+') as fp:
    fp.write(largest_time(0, 1))

def gen_largest_delay():
  with open("../data/secret/006-secret6.in", "w+") as fp:
    fp.write(largest_time(-1, 1e9))


def random_cases():
  


gen_largest()
gen_largest_delay()


