import sys
import pandas as pd

path_to_table = sys.argv[1]
headers = {
    "vales_": ["VALE", "T.PRAM", "PROMO", "MONEDA", "CAPITAL", "IMP.CTA", "CANT.CTAS.", "TDOC", "DOCUMENTO", "NOMBRE",
               "FECHA", "HORA", "SUCURSAL", "GARANTIA", " W/C/A ", "SUCURSAL1", "BOLSA", "COD_RES"],

}

try:
    if "vales_" in path_to_table.lower():
        data = pd.read_csv(path_to_table, sep=";", names=headers["vales_"], usecols=headers["vales_"],
                           encoding="latin1", dtype=str, skiprows=1)
        data = data.drop(["NOMBRE"], axis=1)
        data.DOCUMENTO = data["DOCUMENTO"].apply(hash)
        data.to_csv(path_to_table, index=False, sep=";")
    else:
        print("no table defined with that name")

except:
    print("ERROR EN EL ENMASCARADO")
