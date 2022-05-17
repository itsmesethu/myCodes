from math import floor, trunc
class Solution:
   def solve(self, s):
      s = list(s[::-1])

      def get_value():
         sign = 1
         if s and s[-1] == "-":
            s.pop()
            sign = -1
         value = 0
         while s and s[-1].isdigit():
            value *= 10
            value += int(s.pop())
         return sign * value

      def get_term():
         term = get_value()
         while s and s[-1] in "*/":
            op = s.pop()
            value = get_value()
            if op == "*":
               term *= value
            else:
               term = floor(1.0 * term / value)
         return term

      ans = get_term()
      while s:
         op, term = s.pop(), get_term()
         if op == "+":
            ans += term
         else:
            ans -= term
      return ans
   
s=list(map(str,input().strip()))
f=1
while f==1:
    i=0
    while i<len(s):
        if s[i]=='(':
            p=i
        if s[i]==')':
            q=i
            i=len(s)-1
        i=i+1
    ob = Solution()
    a=ob.solve(s[p+1:q])
    u=[]
    a=str(a)
    u.append(a)  
    s=s[0:p]+u+s[q+1:]
    if '(' not in s:
        f=0
S="".join(s)
ob = Solution()
print(ob.solve(S))
