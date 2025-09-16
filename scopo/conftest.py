import smtplib

import pytest

@pytest.fixture(scope="module", params=["smtp.gmail.com", "mail.python.org"])
def smtp_connection(request):
    smtp_connection = smtplib.SMTP(request.param, 587, timeout=5)
    yield smtp_connection
    print(f"finalizing {smtp_connection}")
    smtp_connection.close()

"""
function: o escopo padrão, a fixture é destruída ao final do teste.

class: a fixture é destruída durante a finalização do último teste na classe.

module: a fixture é destruída durante a finalização do último teste no módulo.

package: a fixture é destruída durante a finalização do último teste no pacote onde a fixture é definida, incluindo subpacotes e subdiretórios dentro dele.

session: a fixture é destruída ao final da sessão de testes.
"""




