import numpy as np
import pandas as pd
import warnings


class AHP:
    def __init__(self, criteria, samples):
        self.RI = (0, 0, 0.58, 0.9, 1.12, 1.24, 1.32, 1.41, 1.45, 1.49)
        self.criteria = criteria
        self.samples = samples
        self.num_criteria = criteria.shape[0]
        self.num_project = samples[0].shape[0]

    def calculate_weights(self, input_matrix):
        input_matrix = np.array(input_matrix)
        n, n1 = input_matrix.shape
        assert n==n1, "the matrix is not orthogonal"
        for i in range(n):
            for j in range(n):
                if np.abs(input_matrix[i,j]*input_matrix[j,i]-1) > 1e-7:
                    raise ValueError("the matrix is not symmetric")
        eigen_values, eigen_vectors = np.linalg.eig(input_matrix)
        max_eigen = np.max(eigen_values)
        max_index = np.argmax(eigen_values)
        eigen = eigen_vectors[:, max_index]
        eigen = eigen/eigen.sum()
        if n > 9:
            CR = None
            warnings.warn("can not judge the uniformity")
        else:
            CI = (max_eigen - n)/(n-1)
            CR = CI / self.RI[n-1]
        return max_eigen, CR, eigen

    def calculate_mean_weights(self,input_matrix):
        input_matrix = np.array(input_matrix)
        n, n1 = input_matrix.shape
        assert n == n1, "the matrix is not orthogonal"
        A_mean = []
        for i in range(n):
            mean_value = input_matrix[:, i]/np.sum(input_matrix[:, i])
            A_mean.append(mean_value)
        eigen = []
        A_mean = np.array(A_mean)
        for i in range(n):
            eigen.append(np.sum(A_mean[:, i])/n)
        eigen = np.array(eigen)
        matrix_sum = np.dot(input_matrix, eigen)
        max_eigen = np.mean(matrix_sum/eigen)
        if n > 9:
            CR = None
            warnings.warn("can not judge the uniformity")
        else:
            CI = (max_eigen - n) / (n - 1)
            CR = CI / self.RI[n - 1]
        return max_eigen, CR, eigen

    def run(self, method="calculate_weights"):
        weight_func = eval(f"self.{method}")
        max_eigen, CR, criteria_eigen = weight_func(self.criteria)
        print('准则层：最大特征值{:<5f},CR={:<5f},检验{}通过'.format(max_eigen, CR, '' if CR < 0.1 else '不'))
        print('准则层权重={}\n'.format(criteria_eigen))

        max_eigen_list, CR_list, eigen_list = [], [], []
        for sample in self.samples:
            max_eigen, CR, eigen = weight_func(sample)
            max_eigen_list.append(max_eigen)
            CR_list.append(CR)
            eigen_list.append(eigen)

        pd_print = pd.DataFrame(eigen_list, index=['准则' + str(i+1) for i in range(self.num_criteria)],
                                columns=['方案' + str(i+1) for i in range(self.num_project)],
                                )
        pd_print.loc[:, '最大特征值'] = max_eigen_list
        pd_print.loc[:, 'CR'] = CR_list
        pd_print.loc[:, '一致性检验'] = pd_print.loc[:, 'CR'] < 0.1
        print('方案层')
        print(pd_print)

        # 目标层
        obj = np.dot(criteria_eigen.reshape(1, -1), np.array(eigen_list))
        print('\n目标层', obj)
        print('最优选择是方案{}'.format(np.argmax(obj)+1))
        return obj


if __name__ == '__main__':
    # 准则重要性矩阵
    criteria = np.array([[1, 2, 7, 5],
                         [1 / 2, 1, 4, 3],
                         [1 / 7, 1 / 4, 1, 1 / 2],
                         [1 / 5, 1 / 3, 2, 1]])

    # 对每个准则，方案优劣排序
    sample1 = np.array([[1, 2, 8], [1/2, 1, 6], [1/8, 1/6, 1]])
    sample2 = np.array([[1, 2, 5], [1 / 2, 1, 2], [1 / 5, 1 / 2, 1]])
    sample3 = np.array([[1, 1, 3], [1, 1, 3], [1 / 3, 1 / 3, 1]])
    sample4 = np.array([[1, 3, 4], [1 / 3, 1, 1], [1 / 4, 1, 1]])

    samples = [sample1, sample2, sample3, sample4]
    a = AHP(criteria, samples).run("calculate_mean_weights")
