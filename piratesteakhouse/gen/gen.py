def largest_time():
  MAXN = int(1e5)
  res = "%d %d\n"%(MAXN, MAXN-1)
  for i in range(1,MAXN):
    res += '%d %d %d\n'%(i,i+1, MAXN-i)
  
  k, t = MAXN-1, 1
  res += "%d %d\n"%(k, t)
  for i in range(2,MAXN+1):
    res += str(i)+" "

  res = res.strip()
  res += "\n"
  return res

with open('../data/secret/004-secret4.in', 'w+') as fp:
  fp.write(largest_time())