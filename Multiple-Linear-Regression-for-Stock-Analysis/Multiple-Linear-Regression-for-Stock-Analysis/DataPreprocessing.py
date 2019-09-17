import pandas as pd

def findSuitableReadMethod( filePath ):
    if filePath.endswith('.csv'):
        readResult = pd.read_csv( filePath )
    elif filePath.endswith('.xls') or filePath.endswith('.xlsx'):
        readResult = pd.read_excel( filePath )
    return readResult

if __name__ == '__main__':
    readResult = findSuitableReadMethod('D:\Chrome Download\iris_data.csv')
    print( readResult )