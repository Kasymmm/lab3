#Write a function that accepts string from user, return a sentence with the words reversed. 
#We are ready -> ready are We

string=input()
def rev(string):
   s=""
   b=string.split(" ")
   new=reversed(b)
   for x in new:
       s+=x
       s+=" "
   print(s)
       
rev(string)