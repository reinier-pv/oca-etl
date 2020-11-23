import pandas as pd

table_file_path = "VALES_20200929.TXT"
headers = ['VALE', 'T.PRAM', 'PROMO', 'MONEDA', 'CAPITAL', 'IMP.CTA', 'CANT.CTAS.', 'TDOC', 'DOCUMENTO', 'NOMBRE', 'FECHA', 'HORA', 'SUCURSAL', 'GARANTIA', ' W/C/A ', 'SUCURSAL1', 'BOLSA', 'COD_RES']

try:
    data = pd.read_csv(table_file_path, sep=";", names=headers, usecols=headers, encoding="latin1", dtype=str,
                       skiprows=1)
    data = data.drop(["NOMBRE"], axis=1)
    data.DOCUMENTO = data["DOCUMENTO"].apply(hash)
    data.to_csv(table_file_path, index=False, sep=";")
except:
    print("ERROR EN EL ENMASCARADO")