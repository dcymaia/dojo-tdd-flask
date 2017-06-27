from flask import Flask, render_template


meu_web_app = Flask('meu_web_app')


DCYMAIA = {
    'nome': 'Danilo Cyrino Maia'
}


PERFIS = {
    'dcymaia': DCYMAIA
}


@meu_web_app.route('/<perfil>')
def pagina_inicial(perfil):
    perfil = PERFIS[perfil]
    return render_template('home.html', perfil=perfil)


if __name__ == "__main__":
    meu_web_app.run()