# 대기시간이 담긴 리스트가 인자로 주어지면 조건을 만족하도록
# 타야하는 대기시간의 순서가 담긴 리스트를 반환하는 함수 neverland()를 작성해봅시다.
def neverland(nums):
    i = nums.pop(2)
    nums.sort()
    nums.insert(0,i)
    return(nums)


# 확인을 위한 코드입니다.
# 대기시간이 담긴 리스트 queue를 자유롭게 수정해보세요!
queue = [30, 10, 20, 50, 40, 60]
print(neverland(queue))
