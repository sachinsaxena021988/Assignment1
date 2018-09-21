
# coding: utf-8

# In[12]:


#define number variable to save the value 
number =''

#loop through the collection range fron 2000 to 3200
for value in range(2000,3201):
    if value % 7 == 0 and value % 5 != 0:
        #convert int to string 
        number +=str(value) +','
else:
    #remove last comma frm the string
    number = number[:-1]
    #print the final output
    print(number)

                
                

