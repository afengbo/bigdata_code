

def lcs(s1, s2):
    """
    计算最长公共子序列的长度
    :param s1:字符串1
    :param s2:字符串2
    :return:最长公共子序列的长度
    """
    # 计算矩阵长宽（两个数的长度）
    s1_length = len(s1)
    s2_length = len(s2)
    # 求长宽均值：为了
    length_avg = (s1_length+s2_length) / 2.0
    # 画出全0矩阵
    matrix = [[0] * (s2_length+1) for i in range(s1_length + 1)]
    # 在矩阵中填充数字
    # 1. 当i=0或者j=0，c(i, j)=0
    # 2. 当i>0, j>0, Xi=Yj，c(i, j)=c(i-1, j-1)+1
    # 3. 当i>0, j>0, Xi≠Yj，c(i, j)=max{c(i-1, j), c(i, j-1)}
    for i in range(s1_length+1)[1:]:
        for j in range(s2_length+1)[1:]:
            if s1[i-1] == s2[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
    return matrix[-1][-1]
    # 最长公共子序列长度与平均长度的比值
    # return matrix[-1][-1]/length_avg


a = 'ABCBDAB'
b = 'BDCABA'
m = lcs(s1=a, s2=b)
print(m)
