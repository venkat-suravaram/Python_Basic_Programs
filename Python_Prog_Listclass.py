# import os
# print(os.getcwd())
# os.chdir('C:\DE\Python\practice')
# print(os.getcwd())

# Create your own package for all the list function
# Create your own package for all the Tuple function
# Create your own package for all the Dict function
# Create your own package for all the set function
# 	use exception handling
# 	never use print function
# 	use logging , log every activity performed by the code.

import logging
class list_own :
    logging.basicConfig(filename="Python_prog_Listclass.log", level=logging.DEBUG, format='%(asctime)s %(message)s')
    logging.info("Prog: Own list --- Started logging")
    def __init__(self,a):  ## passed value once and performing all of the tasks
        self.a=a


    def list_parser(self):
        logging.info("called function list_parser() ")
        try:
            l=[]
            l=self.a
            #print(type(self.l), self.l)
            if type(l)== list:
                return l
                logging.info("Result of list_parser: ")
            else:
                logging.warning("Provided values are not in list format")

        except Exception as error:
            logging.error(error)

    def list_access(self,p): # p is index position
        logging.info("called function list_access() ")
        try:
            l=[]
            l=self.a
            # print(type(l), l)
            # print(l[p])

            if type(l)== list:
                return l[p]
                logging.info("Result of list_access(): ")
            else:
                logging.warning("Provided values are not in list format")

        except Exception as error:
            logging.error(error)


    def list_append(self,ele): # ele is noe input elements
        logging.info("called function list_append() ")
        try:
            l=[]
            l=self.a
            # print(type(l), l)
            # print(l[p])

            if type(l)== list:
                l.append(ele)
                return l
                logging.info("Result of list_append(): ")
            else:
                logging.warning("Provided values are not in list format")

        except Exception as error:
            logging.error(error)

    def list_clear(self):
        logging.info("called function list_clear() ")
        try:
            l=[]
            l=self.a
            # print(type(l), l)
            # print(l[p])

            if type(l)== list:
                l.clear()
                return l
                logging.info("Result of list_clear(): ")
            else:
                logging.warning("Provided values are not in list format")

        except Exception as error:
            logging.error(error)


    def list_extend(self,li): # p is index position
        logging.info("called function list_extend() ")
        try:
            l=[]
            l=self.a
            # print(type(l), l)
            # print(type(li), li)
            # print(l[p])

            if type(l)== list and type(li) == list :
                l.extend(li)
                return l
                logging.info("Result of list_extend(): ")
            else:
                logging.warning("Provided values are not in list format")

        except Exception as error:
            logging.error(error)



#c=list_own(input("Enter values in list format: "))
#c.list_parser()
#c.list_access(3)
#c.list_append("newelement")
#c.list_clear()
#c.list_extend(input("Enter values in list format: "))

c=list_own([2,3,4,5,6])
print(c.list_parser()) # print list
print(c.list_access(3)) # access l[3] indexed value
print(c.list_append("newelement")) ## added element to list
print(c.list_extend([9,10,11,12]))
print(c.list_clear())


