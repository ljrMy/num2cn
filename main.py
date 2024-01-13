NUMBER=[
    "零",
    "一",
    "二",
    "三",
    "四",
    "五",
    "六",
    "七",
    "八",
    "九",
    "十"
]
BASIC_UNIT=[
    "",
    "十",
    "百",
    "千"
]
UNIT=[
    "",
    "万",
    "亿",
    "兆",
    "京",
    "垓",
    "秭",
    "穰",
    "沟",
    "涧",
    "正",
    "载",
    "极",
    "恒河沙",
    "阿僧祇",
    "那由他",
    "不可思议",
    "无量",
    "大数",
    "全仕翔",
    "无边",
    "无数",
    "无知",
    "无想",
    "无觉",
    "古戈尔"
]
def chinese(number:int|float)->str:
    n=number
    if number>=1e104:
        return None
    if number<0:
        number*=-1
    if number%1!=0:
        number=int(number)
    global NUMBER,UNIT,BASIC_UNIT
    digit=[]
    container=[]
    result=""
    while(number!=0):
        digit.append(number%10000) #四位一级
        number//=10000
    digit.reverse()
    for i in digit:
        arr=[i//1000,i%1000//100,i%100//10,i%10]
        content=""
        for j in range(4):
            if arr[j]!=0:
                content+=NUMBER[arr[j]]+BASIC_UNIT[-1-j]
            elif arr[j]==0 and j==0:
                content+=NUMBER[0] #处理0的读法
            elif arr[j]==0 and arr[j-1]!=0:
                content+=NUMBER[0] #处理0的读法
        content=content.rstrip(NUMBER[0])
        container.append(content)
    print(container)
    for i in range(len(container)):
        result+=container[i]
        if container[i]!=NUMBER[0]:
            result+=UNIT[len(container)-i-1]
    result=result.lstrip(NUMBER[0])

    #空字符串直接返回“零”
    if not result and n%1==0:
        return NUMBER[0]
    if n<0:
        result="负"+result
    if n%1!=0:
        decimal=map(lambda arg:NUMBER[int(arg)],list(str(n).split(".")[1]))
        decimal=list(decimal)
        result=result+"点"+"".join(decimal)
    return result

print(
    chinese(2345),
    chinese(4005),
    chinese(10102),
    chinese(111363618263800272018200018),
    chinese(-50046),
    chinese(89.9996),
    sep="\n"
)
