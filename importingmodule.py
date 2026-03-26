import mymodule

print(mymodule.sum(2,4))
print(mymodule.greet("Annie"))

from mymodule import sum
print(sum(9,78))


from mymodule import *
print(diff(90,8))

import mymodule as md
print(md.prod(9,8))

