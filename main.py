import gspread
from google.oauth2.service_account import Credentials

# Xác định phạm vi và thông tin chứng thực
scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

# Mở workbook
sheet_id = "1PXZ4EmpwTOz_6fi8kEOCzEmliRcuyd9clzMH_jVL2-c"
workbook = client.open_by_key(sheet_id)

# Dữ liệu cần cập nhật
values = [
    ["Name", "Price", "Quantity"],
    ["Basketball", 29.99, 1],
    ["Jeans", 39.99, 4],
    ["Soap", 7.99, 3],
]

# Kiểm tra worksheet có tồn tại hay chưa, nếu chưa thì thêm mới
worksheet_list = map(lambda x: x.title, workbook.worksheets())
new_worksheet_name = "Values"

if new_worksheet_name in worksheet_list:
    sheet = workbook.worksheet(new_worksheet_name)
else:
    sheet = workbook.add_worksheet(new_worksheet_name, rows=1000, cols=100)

# Xóa dữ liệu cũ trên worksheet
sheet.clear()

# Cập nhật dữ liệu mới với thứ tự tham số đúng
sheet.update(range_name=f"A1:C{len(values)}", values=values)

# Thêm công thức tính tổng
sheet.update_cell(len(values) + 1, 2, "=sum(B2:B4)")
sheet.update_cell(len(values) + 1, 3, "=sum(C2:C4)")

# Định dạng header
sheet.format("A1:C1", {"textFormat": {"bold": True}})
