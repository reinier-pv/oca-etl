import sys
from jinja2 import Environment, FileSystemLoader

path_to_table = sys.argv[1]
table_name = "vales_"
table_headers = '"VALE", "T.PRAM", "PROMO", "MONEDA", "CAPITAL", "IMP.CTA", "CANT.CTAS.", "TDOC", "DOCUMENTO",' \
                ' "NOMBRE", "FECHA", "HORA", "SUCURSAL", "GARANTIA", " W/C/A ", "SUCURSAL1", "BOLSA", "COD_RES"'

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

template = env.get_template('transformation_base_template.j2')

output = template.render(table_name=table_name, table_headers=table_headers, path_to_table=path_to_table)
print(output)

with open("generated_transformation.py", "w") as fh:
    fh.write(output)
