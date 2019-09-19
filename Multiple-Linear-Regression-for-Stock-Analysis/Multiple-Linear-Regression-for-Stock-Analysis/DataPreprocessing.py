import pandas as pd

def fileVerification( filePath ):
    while not( filePath.endswith(('.csv','.xls','.xlsx','.sql'))):
        print('File can only be Comma Seperated Value, Excel or Sql')
        filePath = input(' Please Enter the path of the file that is valid : ')
    else:
        print('File accepted. Please wait for a moment while the file is  being processed.')
        return filePath
        

def findSuitableReadMethod( filePath ):
    if filePath.endswith('.csv'):
        readResult = pd.read_csv( filePath )
    elif filePath.endswith('.xls') or filePath.endswith('.xlsx'):
        readResult = pd.read_excel( filePath )
    elif filePath.endswith('.sql'):
        readResult = pd.read_sql( filePath )
    return readResult

if __name__ == '__main__':
    inputFilePath = input(' Enter the path of the file : ')
    inputFilePath = fileVerification( inputFilePath )
    readResult = findSuitableReadMethod( inputFilePath )
    print( readResult )