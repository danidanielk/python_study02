'''
Created on 2022. 11. 7.

@author: NT731QCJ-K582D
'''

#분석용 데이터 구축
#    -직접: 출/퇴근 시간에 노약자석을 체크 등
#    -구매: 누군가 모아놓은 데이터를 구매. (비쌈)
#    -위 두방법을 못하는경우 : 웹 데이터 가져오기.(XML,Json,HTML)
#    -분석을 사람이 한다면 BIGData 분석 프로젝트
#    -분석을 AI가 한다면 AI 프로젝트
#    결과를 한눈에 알아보기 쉽게 시각화(표,그래프) 등으로 만드는 작업을 할것임.





b=range(10)
for s in b:
    print(s)
    
    
a=[1,2,3,"yosep"]
print(a[3])

c="김요셉"
d=["액션빔",34]

print(c,d)


class yoseb():    
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def attack(self):
        print("액션빔")
    
    def printInfo(self):
        print(self.name,self.age)
        
y=yoseb("김요셉",34)
y.printInfo()
y.attack()

y.attack()
