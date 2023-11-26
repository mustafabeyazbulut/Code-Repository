def str_replace(str1,str2,str3):
    if str2 in str1:
        str1=str1.replace(str2,str3)
    return str1


str1="Nuclear Energy Engineering"
str2="Nuclear Energy"
str3="Mechanical"

print (str_replace(str1,str2,str3))







