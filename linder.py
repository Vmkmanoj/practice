class linersearch:
    def find(self,a,index_to_find):
        for index,i in enumerate(a):
            if i==index_to_find:
                return index
        
a=[1,4,2,6,8] 
index_to_find=6      
liner=linersearch()
liner.find(a,index_to_find)
