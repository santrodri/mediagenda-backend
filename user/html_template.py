class HtmlTemplate:
    def __init__(self, html_template, basic_html_template, context):
        self.html_template = html_template
        self.basic_html = basic_html_template
        self.context = context

    def render(self):
        return self.html_template.format(**self.context)

    def basic_render(self):
        return self.basic_html.format(**self.context)

html_template = """
    <html>
        <body style="font-family: 'Georgia', serif; background-color: #f5f5f5; margin: 0; padding: 20px;">
            <div style="max-width: 600px; margin: 0 auto; background-color: #ffffff; padding: 30px; border: 1px solid #ddd;">
                <h1 style="color: #2a2a6d; font-size: 28px; margin-bottom: 20px;">Prezado(a) Cliente,</h1>
                <p style="color: #444444; font-size: 16px; line-height: 1.6; margin-bottom: 15px;">
                    É com imenso prazer que lhe damos as boas-vindas a este processo de confirmação.
                </p>
                <p style="color: #444444; font-size: 16px; line-height: 1.6; margin-bottom: 15px;">
                    Utilize o seguinte código para validar sua ação:
                </p>
                <div style="text-align: center; margin: 20px 0;">
                    <div style="display: inline-block; background-color: #2a2a6d; color: #ffffff; padding: 10px 20px; font-size: 20px; font-weight: bold; border-radius: 5px; letter-spacing: 0.2em;">
                        {codigo_confirmacao}
                    </div>
                </div>
                <p style="color: #444444; font-size: 16px; line-height: 1.6; margin-bottom: 15px;">
                    Ou clique no botão abaixo para confirmar diretamente:
                </p>
                <div style="text-align: center; margin: 20px 0;">
                    <a href="{link_confirmacao}" style="display: inline-block; background-color: #2a2a6d; color: #ffffff; padding: 12px 24px; font-size: 16px; font-weight: bold; text-decoration: none; border-radius: 5px;">
                        Confirmar Agora
                    </a>
                </div>
                <p style="color: #444444; font-size: 16px; line-height: 1.6; margin-bottom: 15px;">
                    Este código é de uso único e possui validade restrita. Recomendamos que realize a confirmação o quanto antes.
                </p>
                <p style="font-size: 12px; color: #777777; text-align: center; margin-top: 30px;">
                    Atenciosamente,<br>Equipe de Suporte - MediAgenda © 2025
                </p>
            </div>
        </body>
    </html>
"""

basic_html_template = """
        "Prezado(a) Cliente,\n\n"
        f"Use o código codigo_confirmacao para validar sua ação.\n\n"
        "Atenciosamente,\nEquipe de Suporte - MediAgenda
        """