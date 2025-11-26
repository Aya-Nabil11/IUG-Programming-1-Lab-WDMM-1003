a = 3   #011
b = 5  # 101
        #------
        #001

# a = a & b
a &= b

# Output
print(a)


a = 3  #011
b = 5  #101
    #-------------
    #111

# a = a | b
a |= b

# Output
print(a)