import pandas as pd
import numpy as np
data=pd.read_excel(r'总最低费用.xlsx')
print(list(np.array(data)))


# import pandas as pd
# import numpy as np
#
# # Read in data from Excel file
# data = pd.read_excel(r'总最低费用.xlsx')
#
# # Access the first row of the DataFrame and store it as a NumPy array
# matrix = np.array(data.iloc[:])
#
# # Print the matrix
# print(f'matrix[0] = {matrix}')
