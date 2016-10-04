
# coding: utf-8

# In[34]:

class book(object):
    def __init__(self,name,pages,author):
        self.name = name
        self.pages = pages
        self.author = author
        
    def __str__(self):
        return "Author name %s, Book pages %d, Book Author %s" %(self.name, self.pages, self.author)
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print "The obj is gone"


# In[35]:

d = book('Milind',200,'Parab')


# In[36]:

print d 


# In[37]:

len(d)


# In[33]:

del(d)


# In[ ]:



