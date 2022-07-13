import gspread
import pandas as pd

sa = gspread.service_account("second-broker-349713-8151d6ec29ec.json")
sh = sa.open("Woody Ordering System")
wks = sh.worksheet("Shipped")

df = pd.DataFrame(wks.get_all_values())
print(df[23])
print('Rows: ', wks.row_count)
print('Cols: ', wks.col_count)