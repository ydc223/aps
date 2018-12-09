def largest_time():
  MAXN = int(10e5)
  res = ""
  for i in range(1,MAXN):
    res += '%d %d %d\n'%(i,i+1, MAXN-i)
  
  k, t = MAXN-1, 1
  res += "%d %d\n"%(k, t)
  for i in range(2,k+1):
    res += str(i)+" "
  res += "\n"
  return res

with open('../data/secret/004-secret4.in', 'w+') as fp:
  fp.write(largest_time())