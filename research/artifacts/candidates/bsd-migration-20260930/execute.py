"""Exact BSD candidate regression; standard library only."""
from fractions import Fraction as F
import json,sys
from pathlib import Path
def v2(q):
 def vi(n):
  assert n
  n=abs(n);v=0
  while n%2==0:n//=2;v+=1
  return v
 return vi(q.numerator)-vi(q.denominator)
def double(P,n):
 x,y=P;assert y
 m=(3*x*x-n*n)/(2*y)
 X=m*m-2*x;Y=m*(x-X)-y
 assert X==(x*x+n*n)**2/(4*x*(x*x-n*n))
 assert Y*Y==X**3-n*n*X
 return X,Y


def main():
 P=(F(25,4),F(75,8)); points=[]
 for k in range(6):
  x,y=P;assert y*y==x**3-25*x;assert v2(x)==-2-2*k
  points.append({'k':k,'multiple':2**k,'x':str(x),'y':str(y),'v2_x':v2(x)})
  if k<5:P=double(P,5)
 # Explicit invalid point rejection, rather than silently treating point search as proof.
 bad=(F(25,4),F(74,8));assert bad[1]**2!=bad[0]**3-25*bad[0]
 out={'status':'local_exploratory_candidate_only','points':points,'tests':'all assertions passed','scope':'rank lower bound only; see derivation'}
 Path(__file__).with_name('results.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
 print(json.dumps({'tests':out['tests'],'v2_x':[p['v2_x'] for p in points]}))
if __name__=='__main__':main()
