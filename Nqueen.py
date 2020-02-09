import copy

#a new line
def judge(queenLocs):
    """
    判断给定的位置列表下，是否满足皇后共存
    :param queenLocs:  1-N个元素，每个元素为该一个皇后的列坐标
    :return: True or False
    """
    for queen1, loc1 in enumerate(queenLocs[:-1]):
        for queen2, loc2 in enumerate(queenLocs[queen1+1:], queen1+1):
            if loc2 == loc1 or queen2 - queen1 == abs(loc2 - loc1):#位于同列或对角线
                return False
    return True


def display(queenLocs):
    """
    显示皇后位置
    :param queenLocs:皇后位置列表
    :return: None
    """
    for loc in queenLocs:
        line = "___"*loc + " * " + "___"*(len(queenLocs)-loc-1)
        print(line)


def solveNqueen(queenNum, queenLocs = [], results = []):
    """
    利用DPS递归+回溯所有可能的N皇后问题，并返回所有解
    :param queenNum: 皇后数目
    :param queenLocs: 已有皇后位置，默认为空
    :param results: 记录所有解决方案
    :return: None
    """
    for loc in range(queenNum):
        queenLocs.append(loc)                              #在已有皇后位置的基础上，尝试再放置一个皇后
        if judge(queenLocs):                               #新放入的皇后能够共存
            if len(queenLocs) == queenNum:                 #若已放置目标数量的皇后
                results.append(copy.deepcopy(queenLocs))   #记录当前解决方案，并将一份深拷贝加入到结果
            else:                                          #未达到目标数量且当前可以共存，在此基础上
                solveNqueen(queenNum, queenLocs, results)
        queenLocs.pop()

if __name__ == "__main__":
    results = []
    solveNqueen(8, results = results)
    print(len(results))
    display((results[0]))


