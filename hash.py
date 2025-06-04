#實作Hash基本架構

class HashTable:
    def __init__(self,size):
        self.size =size # define the buckets of the table 
        self.table=[[] for _ in range(size)] #bulid a empty hash table [[],[],[]*size],and list of lists (deal with chain) 
    def hash_function(self,key):
        return hash(key) % self.size 
    
    def insert(self,key,value):
        index=self.hash_function(key)
        # 更新現有的 key，否則加入新值
        for i,(k,v) in enumerate(self.table[index]):
            if k==key:
                self.table[index][i]=(key,value)
                return self.table[index].append((key,value))
        
    
        