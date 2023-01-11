list1=str(input("enter first string:"))
list2=str(input("enter second string:"))
slist1=list1.split()
slist2=list2.split()
set1=set(slist1)    
set2=set(slist2)
common_words=set1.intersection(set2)
print("common words are:",common_words)
for i in common_words:
    list1=list1.replace(i,' ')
    list2=list2.replace(i,' ')
    new_string1=list1
    new_string2=list2
print(new_string1)
print(new_string2)
