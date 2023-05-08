def isOldEnough(age, location):
    if age <= 17 and location== "UK":
        return True
    
    if age>=16 and location=="Canada":
        return True
    
    return False


def output_driving_status(age, location, passed_driving_test):
    """outpoot message"""
    old_enough = isOldEnough(age, location)
    if old_enough is False:
        print("you not enought")
        return
    
    if passed_driving_test is False:
        print("you may learning")
    else:
        print("you allowed to drive")


#print(isOldEnough(13, "UK"))
#print(isOldEnough(16, "Canada"))
#print(isOldEnough(16, "UK"))

output_driving_status(16, "Canada", False)
output_driving_status(16, "UK", False)
output_driving_status(17, "UK", True)
output_driving_status(17, "Canada", True)
output_driving_status(15, "Canada", True)