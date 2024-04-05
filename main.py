#danny

import math

name=input('What is the name of your first cousin?')
name=name.swapcase()
name=name[0:3]

num=int(input("How many Galaxies do you think are nearest to ours?"))
num=math.pow(num,2)*math.pi

print('Your new password is:'+name+str(num))
