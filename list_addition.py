user=input("enter elements of list seperated with commas: ").replace("\n","")
user2=input("enter another list of elements seperated with commas: ")
list1=user.split(",")
list2=user2.split(",")
final_list=list1+list2
print(final_list)