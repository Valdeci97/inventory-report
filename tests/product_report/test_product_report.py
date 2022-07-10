from inventory_report.inventory.product import Product

expected = (
    'O produto farinha' +
    ' fabricado em 01-05-2021' +
    ' por Farinini' +
    ' com validade até 02-06-2023' +
    ' precisa ser armazenado ao abrigo de luz.'
)


def test_relatorio_produto():
    product = Product(
        7,
        'farinha',
        'Farinini',
        '01-05-2021',
        '02-06-2023',
        '123456895',
        'ao abrigo de luz',
    )
    assert str(product) == expected
    assert isinstance(product, Product)
