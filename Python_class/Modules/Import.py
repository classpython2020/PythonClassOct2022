# Import

#we can use one module functions into another module by using Import function.
#there are three ways to do.

#1. import module name.
    # it will import the function from that module to current module. to use that function in that module.
      # import module name
        # module name.function name.

#2. we can use from keyword as well
    # first we need to import from the module and after that we have to import function from the module.
      #from module name import function name.
        # we can use the function dirctly with out any module name.

#3. we can use all the functions from that module by using *
    #from module name import *
     # it means we can use all the functions from that module.



#1. import module name.

import Moduleex
Moduleex.sum(10,10)

#2. we can use from keyword as well

from Moduleex import sum
sum(10,10)

#3. we can use all the functions from that module by using *
    #by giving * we have to call all the functions from that module.

from Moduleex import *

sum(10,10)
mul(10,10)



