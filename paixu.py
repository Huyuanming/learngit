import pdb                                                           #debug
# class MyList(list):                                                #自带无法链式
#     def append(self, value):
#         super(MyList, self).append(value)
#         return self
#     def extend(self, value):
#         super(MyList, self).extend(value)
#         return self

def paixu(array):
   if len(array)==1 or len(array)==0:
      return array
   leftarray = []#MyList()
   rightarray = []#MyList()
   t = []
   index = array[0]
   for i in range(1,len(array)):
      if array[i]<index:
         leftarray.append(array[i])
      else:
         rightarray.append(array[i])
   t.extend(paixu(leftarray))
   t.append(index)
   t.extend(paixu(rightarray))
   return t#paixu(leftarray).append(index).extend(paixu(rightarray))

if __name__ == '__main__':
   array = [1,2,9,5,6,3,7,8]
   array1 = paixu(array)
   print array1