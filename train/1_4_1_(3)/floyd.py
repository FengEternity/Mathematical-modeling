# 弗洛伊德算法
class Graph(object):
    def __init__(self, length: int, matrix: [], vertex: []):
        """
        :param length: 大小
        :param matrix: 邻接矩阵
        :param vertex: 顶点数组
        """
        # 保存，从各个顶点出发到其它顶点的距离，最后的结果，也保留在该数组
        self.dis = matrix
        # 保存到达目标顶点的前驱顶点
        self.pre = [[0 for col in range(length)] for row in range(length)]
        self.vertex = vertex
        # 对 pre数组进行初始化，存放的是前驱顶点的下标
        for i in range(length):
            for j in range(length):
                self.pre[i][j] = i

    # 显示pre数组和dis数组
    def show_graph(self):
        # excel_path = 'tes.xlsx'
        # wb = Workbook(excel_path)
        # wb.save(excel_path)
        #
        # wb = load_workbook(excel_path)
        # wb.create_sheet("铁路最短路径")
        # ws = wb.active
        for k in range(len(self.dis)):
            # 先将pre数组输出的一行
            # for i in range(len(self.dis)):
                # print(self.pre[k][i], end=" ")
                # print(self.vertex[self.pre[k][i]], end=" ")
            # 输出dis数组的一行数据
            # print()
            # for row in range(1,25):
            #     for col in range(1,25):
                    for i in range(len(self.dis)):
                        # print('({}到{}的最短路径是{})'.format(self.vertex[k], self.vertex[i], self.dis[k][i]), end=" ")
                        print(self.dis[k][i])
                        # ws.cell(row,col).value = self.dis[k][i]
                    print()
                    # print()
        # wb.save(excel_path)
        # wb.close()

    # 佛洛依德算法
    def floyd(self):
        length: int = 0  # 变量保存距离
        # 对中间顶点的遍历,k 就是中间顶点的下标
        for k in range(len(self.dis)):  # ['A', 'B', 'C', 'D', 'E', 'F', 'G']
            # 从 i顶点开始出发['A', 'B', 'C', 'D', 'E', 'F', 'G']
            for i in range(len(self.dis)):
                # 到达j顶点 ['A', 'B', 'C', 'D', 'E', 'F', 'G']
                for j in range(len(self.dis)):
                    length = self.dis[i][k] + self.dis[k][j]  # 求出从i 顶点出发，经过k中间顶点，到达j顶点距离
                    if length < self.dis[i][j]:  # 如果length 小于dis[i][j]
                        self.dis[i][j] = length  # 更新距离
                        self.pre[i][j] = self.pre[k][j]  # 更新前驱顶点


if __name__ == '__main__':
    # 铁路
    # vertex: [] = ['K1', 'K2', 'K3', 'K4', 'K5', 'K6', 'K7', 'K8', 'K9', 'K10', 'K11', 'K12', 'K13', 'K14', 'K15', 'K16',
    #               'K17', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7']
    print("Vertex")
    #公路
    vertex: [] = ['K1', 'K2', 'K3', 'K4', 'K5', 'K6', 'K7', 'K8', 'K9', 'K10', 'K11', 'K12', 'K13', 'K14', 'K15', 'K16','K17',
                  'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7',
                  'A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15',
                  'K1', 'K2', 'K3', 'K4', 'K5', 'K6', 'K7', 'K8',
                  'A16', 'K10', 'K11', 'A17', 'A17', 'A19', 'A20', 'K16','K17',
                  'A21']
    print("test")
    # 邻接矩阵
    matrix: [] = [[0 for col in range(len(vertex))] for row in range(len(vertex))]
    # 用来表示一个极大的数
    nan: float = float('inf')
    matrix[0] = [0.0, 104.0, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
       nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
       nan, nan, nan, nan, nan, nan, nan, nan]
    matrix[1] = [104.0, 0.0, 301.0, nan, nan, nan, nan, nan, nan, nan, nan,
       nan, nan, nan, nan, 3.0, nan, nan, nan, nan, nan, nan, nan, nan,
       nan, nan, nan, nan, nan, nan, nan, nan, nan]
    matrix[2] = [nan, 301.0, 0.0, 750.0, nan, nan, nan, nan, nan, nan, nan,
       nan, nan, nan, nan, nan, nan, 2.0, nan, nan, nan, nan, nan, nan,
       nan, nan, nan, nan, nan, nan, nan, nan, nan]
    matrix[3] = [nan, nan, 750.0, 0.0, 606.0, nan, nan, nan, nan, nan, nan,
       nan, nan, nan, nan, nan, nan, nan, 600.0, nan, nan, nan, nan, nan,
       nan, nan, nan, nan, nan, nan, nan, nan, nan]
    matrix[4] = [nan, nan, nan, 606.0, 0.0, 194.0, nan, nan, nan, nan, nan,
       nan, nan, nan, nan, nan, nan, nan, nan, 10.0, nan, nan, nan, nan,
       nan, nan, nan, nan, nan, nan, nan, nan, nan]
    matrix[5] = [nan, nan, nan, nan, 194.0, 0.0, 205.0, nan, nan, nan, nan,
       nan, nan, nan, nan, nan, nan, nan, nan, nan, 5.0, nan, nan, nan,
       nan, nan, nan, nan, nan, nan, nan, nan, nan]
    matrix[6] = [nan, nan, nan, nan, nan, 205.0, 0.0, 201.0, nan, nan, nan,
       nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 10.0, nan, nan,
       nan, nan, nan, nan, nan, nan, nan, nan, nan]
    matrix[7] = [nan, nan, nan, nan, nan, nan, 201.0, 0.0, 680.0, nan, nan,
       nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 12.0, nan,
       nan, nan, nan, nan, nan, nan, nan, nan, nan]
    matrix[8] = [nan, nan, nan, nan, nan, nan, nan, 680.0, 0.0, 480.0, nan,
       nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 42.0,
       nan, nan, nan, nan, nan, nan, nan, nan, nan]
    matrix[9] = [nan, nan, nan, nan, nan, nan, nan, nan, 480.0, 0.0, 300.0,
       nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
       70.0, nan, nan, nan, nan, nan, nan, nan, nan]
    matrix[10] = [nan, nan, nan, nan, nan, nan, nan, nan, nan, 300.0, 0.0,
       220.0, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
       nan, nan, 10.0, nan, nan, nan, nan, nan, nan]
    matrix[11] = [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 220.0,
       0.0, 210.0, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
       nan, nan, nan, nan, 10.0, nan, nan, nan, nan]
    matrix[12] = [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
       210.0, 0.0, 420.0, nan, nan, nan, nan, nan, nan, nan, nan, nan,
       nan, nan, nan, nan, nan, nan, 62.0, nan, nan, nan]
    matrix[13] = [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
       420.0, 0.0, 500.0, nan, nan, nan, nan, nan, nan, nan, nan, nan,
       nan, nan, nan, nan, nan, nan, 30.0, nan, nan]
    matrix[14] = [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
       nan, 500.0, 0.0, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
       nan, nan, nan, nan, nan, nan, 20.0, nan]
    matrix[15] = [nan, 3.0, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
       nan, nan, nan, 0.0, 450.0, nan, nan, nan, nan, nan, nan, nan, nan,
       nan, nan, nan, nan, nan, nan, nan, nan]
    matrix[16] = [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
       nan, nan, nan, 450.0, 0.0, 80.0, 1150.0, nan, nan, nan, nan, nan,
       nan, nan, nan, nan, nan, nan, nan, nan, nan]
    matrix[17] = [nan, nan, 2.0, nan, nan, nan, nan, nan, nan, nan, nan, nan,
       nan, nan, nan, nan, 80.0, 0.0, nan, nan, nan, nan, nan, nan, nan,
       nan, nan, nan, nan, nan, nan, nan, nan]
    matrix[18] = [nan, nan, nan, 600.0, nan, nan, nan, nan, nan, nan, nan, nan,
       nan, nan, nan, nan, 1150.0, nan, 0.0, nan, nan, nan, 1100.0, nan,
       nan, nan, nan, nan, nan, nan, nan, nan, nan]
    matrix[19] = [nan, nan, nan, nan, 10.0, nan, nan, nan, nan, nan, nan, nan,
       nan, nan, nan, nan, nan, nan, nan, 0.0, 306.0, nan, nan, nan, nan,
       nan, nan, nan, nan, nan, nan, nan, nan]
    matrix[20] = [nan, nan, nan, nan, nan, 5.0, nan, nan, nan, nan, nan, nan,
       nan, nan, nan, nan, nan, nan, nan, 306.0, 0.0, 195.0, nan, nan,
       nan, nan, nan, nan, nan, nan, nan, nan, nan]
    matrix[21] = [nan, nan, nan, nan, nan, nan, 10.0, nan, nan, nan, nan, nan,
       nan, nan, nan, nan, nan, nan, nan, nan, 195.0, 0.0, 222.0, nan,
       nan, nan, nan, nan, nan, nan, nan, nan, nan]
    matrix[22] = [nan, nan, nan, nan, nan, nan, nan, 12.0, nan, nan, nan, nan,
       nan, nan, nan, nan, nan, nan, 1100.0, nan, nan, 222.0, 0.0, 720.0,
       nan, nan, nan, nan, nan, nan, nan, nan, nan]
    matrix[23] = [nan, nan, nan, nan, nan, nan, nan, nan, 42.0, nan, nan, nan,
       nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 720.0, 0.0,
       520.0, nan, nan, nan, nan, nan, nan, nan, nan]
    matrix[24] = [nan, nan, nan, nan, nan, nan, nan, nan, nan, 70.0, nan, nan,
       nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 520.0, 0.0,
       170.0, nan, nan, nan, nan, nan, nan, nan]
    matrix[25] = [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
       nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 170.0,
       0.0, 88.0, 160.0, nan, nan, nan, nan, nan]
    matrix[26] = [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 10.0, nan,
       nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
       88.0, 0.0, nan, 190.0, nan, nan, nan, nan]
    matrix[27] = [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
       nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
       160.0, nan, 0.0, 70.0, 320.0, nan, nan, nan]
    matrix[28] = [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, 10.0,
       nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
       nan, 190.0, 70.0, 0.0, 260.0, nan, nan, nan]
    matrix[29] = [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
       62.0, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
       nan, nan, 320.0, 260.0, 0.0, 160.0, nan, 100.0]
    matrix[30] = [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
       nan, 30.0, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
       nan, nan, nan, nan, 160.0, 0.0, 290.0, nan]
    matrix[31] = [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
       nan, nan, 20.0, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
       nan, nan, nan, nan, nan, 290.0, 0.0, nan]
    matrix[32] = [nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
       nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan, nan,
       nan, nan, nan, nan, 100.0, nan, nan, 0.0]
    g = Graph(len(vertex), matrix, vertex)
    # 调用弗洛伊德算法
    g.floyd()
    g.show_graph()
