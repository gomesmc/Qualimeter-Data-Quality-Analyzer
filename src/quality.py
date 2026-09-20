def check_duplicates(archive):
   duplicates = archive[archive.duplicated()]
   return duplicates

def check_total_duplicates(archive):
   total_duplicates = archive.duplicated().sum().sum()
   return total_duplicates

def check_nan(archive):
    nan = archive[archive.isna().any(axis=1)]
    return nan

def check_null(archive):
    null = archive[archive.isnull().any(axis=1)]
    return null

def columns(archive):
   columns = archive.columns
   return columns

def data_describe(archive):
    describe = archive.describe()
    return describe

# data = pd.read_csv('archives/clientes.csv')

# print("check_duplicates(data)")
# print(f"\nNumber of data's duplicates: {check_total_duplicates(data)}")
# print(f"\nCheck data's NaN:\n {check_nan(data)}")
# print(f"\nCheck data's null:\n {check_null(data)}")
# print(f"\nCheck data's estatistic:\n {data_describe(data)}")