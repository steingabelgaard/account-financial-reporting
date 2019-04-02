import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo10-addons-oca-account-financial-reporting",
    description="Meta package for oca-account-financial-reporting Odoo addons",
    version=version,
    install_requires=[
        'odoo10-addon-account_bank_statement_line_reconciliation',
        'odoo10-addon-account_financial_report_date_range',
        'odoo10-addon-account_financial_report_horizontal',
        'odoo10-addon-account_financial_report_qweb',
        'odoo10-addon-account_move_line_report_xls',
        'odoo10-addon-account_tax_balance',
        'odoo10-addon-customer_activity_statement',
        'odoo10-addon-customer_outstanding_statement',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
