# # 비밀번호를 만들어주는 함수 yoonHa()를 만들어봅시다.
# yoonDict = {"4":"love", "8":"smile", "6":"kiss"}
# def yoonHa(nums):
#     password = ""
#     for i in str(nums):
#         password = password + yoonDict[i]
#     return password


# # 채점을 위한 코드입니다. 이를 수정하지 마세요!
# nums = input()
# print(yoonHa(nums))




#숫자로 하게되면 in 으로 처리할 수 없고 
# range로 하게될 경우 한자리를 처리하는게 아니라 
# 1부터 num까지 처리하게 됩니다.

# 비밀번호를 만들어주는 함수 yoonHa()를 만들어봅시다.
str1 = ""
interp = {"4":"love", "8":"smile", "6":"kiss"}
def yoonHa(ip):
    global str1
    for i in ip:
        var1 = interp[i]
        str1 = str1 + var1
    return str1

# 채점을 위한 코드입니다. 이를 수정하지 마세요!
nums = input()
print(yoonHa(nums))