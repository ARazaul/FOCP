no_of_PCs=24
total_no_of_students=int(input("enter no of students: "))
fully_grouped=total_no_of_students // no_of_PCs
left_over=total_no_of_students%no_of_PCs
print("Total No of Fully Grouped is: "+str(fully_grouped))
print("Total No of smaller 'left over' group is: "+str(left_over))