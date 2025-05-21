import xlrd
file_path = r'C:\Kavin Kumar\Job\Assessment\Framework\data\Locators_.xlsx'
workbook = xlrd.open_workbook(file_path)
login_sheet = workbook.sheet_by_name('Login')
l_rows = login_sheet.get_rows()
headers = next(l_rows)

def login():
    login_dic = {}
    for ele in l_rows:
        login_dic[ele[0].value] = (ele[1].value,ele[2].value)
    return login_dic

pim_sheet = workbook.sheet_by_name('Pim')
p_rows = pim_sheet.get_rows()
header = next(p_rows)
def pim():
    p_dic = {}
    for ele in p_rows:
        p_dic[ele[0].value] = (ele[1].value,ele[2].value)
    return  p_dic

emp_sheet = workbook.sheet_by_name('Emp')
e_rows = emp_sheet.get_rows()
e_header = next(e_rows)
def emp():
    e_dic = {}
    for ele in e_rows:
        e_dic[ele[0].value] = (ele[1].value,ele[2].value)
    return  e_dic

logout_sheet = workbook.sheet_by_name('Logout')
lo_rows = logout_sheet.get_rows()
lo_headers = next(lo_rows)
def logout():
    logout_dic = {}
    for ele in lo_rows:
        logout_dic[ele[0].value] = (ele[1].value, ele[2].value)
    return logout_dic

