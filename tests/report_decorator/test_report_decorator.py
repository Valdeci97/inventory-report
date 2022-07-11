from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


products = [{
    'id': '1',
    'nome_do_produto': 'farinha',
    'nome_da_empresa': 'Rosa Branca',
    'data_de_fabricacao': '2022-07-08',
    'data_de_validade': '2022-11-04',
    'numero_de_serie': '1234567891',
    'instrucao_de_armazenamento': 'em local seco e arejado',
}]


expected = '''\033[32mData de fabricação mais antiga:\033[0m \033[36m2022-07-08\033[0m
\033[32mData de validade mais próxima:\033[0m \033[36m2022-11-04\033[0m
\033[32mEmpresa com mais produtos:\033[0m \033[31mRosa Branca\033[0m'''


def test_decorar_relatorio():
    colored_report = ColoredReport(SimpleReport).generate(products)

    assert colored_report == expected
