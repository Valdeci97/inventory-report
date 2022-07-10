from inventory_report.inventory.product import Product


expected = (
    'O produto extrato de tomate' +
    ' fabricado em 2022-05-12' +
    ' por Quero' +
    ' com validade até 2022-08-07' +
    ' precisa ser armazenado em local seco e arejado.')


def test_cria_produto():
    product = Product(
        7,
        'extrato de tomate',
        'Quero',
        '2022-05-12',
        '2022-08-07',
        '12458664',
        'em local seco e arejado')

    assert type(product.id) is int
    assert type(product.nome_do_produto) is str
    assert type(product.nome_da_empresa) is str
    assert type(product.data_de_fabricacao) is str
    assert type(product.data_de_validade) is str
    assert type(product.numero_de_serie) is str
    assert type(product.instrucoes_de_armazenamento) is str
    assert str(product) == expected
