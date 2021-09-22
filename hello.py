from flask import Flask, render_template, redirect, url_for

#para o db 333
from flask_sqlalchemy import SQLAlchemy

#migrate 444
from flask_migrate import Migrate

#organizar 555
from forms import Criar_ensaio, Alfa

from MAIN_dosagem import Ensaio



#create a Flask Instance
app = Flask(__name__)

#para o form 222
app.config['SECRET_KEY'] = "you-will-never-know"
#para o db 333
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newapp.db'
db = SQLAlchemy(app)
#para migrate 444
migrate = Migrate(app, db)







    # ROTAS

@app.route('/')
@app.route('/home')
def home():
    ensaios_registrados = Ensaios.query.all()
    return render_template('home.html', ensaios_registrados=ensaios_registrados)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html')


@app.route('/criar', methods=['POST', 'GET'])
def criar():

    form = Criar_ensaio()
    if form.validate_on_submit():

        novo_ensaio = Ensaios(
        nome = form.nome.data,
        piloto = form.piloto.data,
        rico = form.rico.data,
        pobre = form.pobre.data,
        cp = form.cp.data,
        pesobrita = form.pesobrita.data,
        slump = form.slump.data,
        umidade = form.umidade.data
        )
        print(novo_ensaio)
        db.session.add(novo_ensaio)
        db.session.commit()

        return redirect('/home')
    return render_template('criar.html', form=form)


@app.route('/home/<int:id>')
def apagar_ensaio(id):
    apagar = Ensaios.query.get_or_404(id)

    try:
        db.session.delete(apagar)
        db.session.commit()
        return redirect('/home')

    except:
        "DEU ERRADO"


@app.route('/editar_ensaio/<int:id>', methods=['POST', 'GET'])
def editar_ensaio(id):

    form = Criar_ensaio()

    editar = Ensaios.query.get_or_404(id)
#    print(editar)
#    print(editar.nome)
#    print(form.nome.data)
    
    if form.validate_on_submit():
        editar.nome = form.nome.data
        editar.piloto = form.piloto.data
        editar.rico = form.rico.data
        editar.pobre = form.pobre.data
        editar.cp = form.cp.data
        editar.pesobrita = form.pesobrita.data
        editar.slump = form.slump.data
        editar.umidade = form.umidade.data
        db.session.commit()
        print('to aq')
        return redirect('/home')
    return render_template('editar_ensaio.html', form=form, editar=editar)



@app.route('/dosagem/<int:id>', methods=['POST', 'GET'])
def dosagem(id):
    form = Alfa()

    ensaio_salvo = Ensaios.query.filter_by(id=id).first()
    dosagens_do_ensaio_salvo = ensaio_salvo.dosagem_piloto

    m = ensaio_salvo.piloto
    cp = ensaio_salvo.cp
    alfa = form.alfa.data
    pesobrita = ensaio_salvo.pesobrita
    slump = ensaio_salvo.slump
    umidade = ensaio_salvo.umidade

    if form.validate_on_submit():
        if dosagens_do_ensaio_salvo == []:
            alfaantigo = 0
        else:
            alfaantigo = dosagens_do_ensaio_salvo[-1].alfa

        traco = Ensaio(
            m = m,
            cp = cp,
            alfa = form.alfa.data, 
            pesobrita = pesobrita,
            alfaantigo = alfaantigo,
            umidade = umidade)

        add_no_db = Dosagem_piloto(
            alfa = form.alfa.data,
            c_unitario = traco.massas_unitarias()[0],
            a_unitario = traco.massas_unitarias()[1],
            b_unitario = traco.massas_unitarias()[2],
            
            c_massa = traco.massas_iniciais()[0],
            a_massa = traco.massas_iniciais()[1],
            b_massa = traco.massas_iniciais()[2],
            
            c_acr = traco.quantidades_adicionar()[0],
            a_acr = traco.quantidades_adicionar()[1],
            
            agua = 0,
            ensaio = ensaio_salvo)
        print(add_no_db)
        db.session.add(add_no_db)
        db.session.commit()
        return redirect('/dosagem/{}'.format(id))
    return render_template("dosagem.html", form=form, id=id, dosagens_do_ensaio_salvo=dosagens_do_ensaio_salvo, m=m, slump=slump)



@app.route('/auxiliar/<int:id>', methods=['POST', 'GET'])
def dosagem_auxiliar(id):
    form = Alfa()

    ensaio_salvo = Ensaios.query.filter_by(id=id).first()
    dosagens_do_ensaio_salvo_rico = ensaio_salvo.dosagem_rico
    dosagens_do_ensaio_salvo_pobre = ensaio_salvo.dosagem_pobre
    print("dosagem rico")
    print(dosagens_do_ensaio_salvo_rico)
    print("dosagem pobre")
    print(dosagens_do_ensaio_salvo_pobre)
    m_rico = ensaio_salvo.rico
    m_pobre = ensaio_salvo.pobre
    cp = ensaio_salvo.cp
    alfa = form.alfa.data
    pesobrita = ensaio_salvo.pesobrita
    slump = ensaio_salvo.slump


    if form.validate_on_submit():

#        ESSA DOSAGEM NAO PRECISA DE ALFA ANTIGO
#        if dosagens_do_ensaio_salvo_rico == []:
#            alfaantigo = 0
#        else:
#            alfaantigo = dosagens_do_ensaio_salvo_rico[-1].alfa

        traco = Ensaio(
            m = m_rico,
            cp = cp,
            alfa = form.alfa.data, 
            pesobrita = pesobrita)

        add_no_db_rico = Dosagem_rico(
            alfa = form.alfa.data,
            c_unitario = traco.massas_unitarias()[0],
            a_unitario = traco.massas_unitarias()[1],
            b_unitario = traco.massas_unitarias()[2],
            
            c_massa = traco.massas_iniciais()[0],
            a_massa = traco.massas_iniciais()[1],
            b_massa = traco.massas_iniciais()[2],
            
            c_acr = traco.quantidades_adicionar()[0],
            a_acr = traco.quantidades_adicionar()[1],
            
            agua = 0,
            ensaio = ensaio_salvo)


#       Essa dosagem nao precisa de alfa antigo
#        if dosagens_do_ensaio_salvo_pobre == []:
#            alfaantigo = 0
#        else:
#            alfaantigo = dosagens_do_ensaio_salvo_pobre[-1].alfa

        traco = Ensaio(
            m = m_pobre,
            cp = cp,
            alfa = form.alfa.data, 
            pesobrita = pesobrita)

        add_no_db_pobre = Dosagem_pobre(
            alfa = form.alfa.data,
            c_unitario = traco.massas_unitarias()[0],
            a_unitario = traco.massas_unitarias()[1],
            b_unitario = traco.massas_unitarias()[2],
            
            c_massa = traco.massas_iniciais()[0],
            a_massa = traco.massas_iniciais()[1],
            b_massa = traco.massas_iniciais()[2],
            
            c_acr = traco.quantidades_adicionar()[0],
            a_acr = traco.quantidades_adicionar()[1],
            
            agua = 0,
            ensaio = ensaio_salvo)


        if dosagens_do_ensaio_salvo_rico == []:
            db.session.add(add_no_db_rico)
            db.session.add(add_no_db_pobre)
            db.session.commit()
            return redirect('/auxiliar/{}'.format(id))

        else:
            rico_velho = Dosagem_rico.query.get_or_404(id)
            pobre_velho = Dosagem_pobre.query.get_or_404(id)
            db.session.delete(rico_velho)
            db.session.delete(pobre_velho)
            db.session.add(add_no_db_rico)
            db.session.add(add_no_db_pobre)
            db.session.commit()
            return redirect('/auxiliar/{}'.format(id))

    return render_template("auxiliar.html", form=form, id=id, dosagens_do_ensaio_salvo_rico=dosagens_do_ensaio_salvo_rico, dosagens_do_ensaio_salvo_pobre=dosagens_do_ensaio_salvo_pobre, m_rico=m_rico, m_pobre=m_pobre, slump=slump)


@app.route('/dosagem/delete/<int:id>')#esse id é da linha na tabela Dosagem_piloto
def delete(id):
    #linha da dosagem a ser deletara
    dosagem_deletada = Dosagem_piloto.query.filter_by(id=id).first()
    #id do ensaio que essa dosagem pertence (.ensaio é o backref pra achar o o elemento "pai")
    dosagem_deletada.ensaio.id

    db.session.delete(dosagem_deletada)
    db.session.commit()

    return redirect('/dosagem/{}'.format(dosagem_deletada.ensaio.id))



@app.route('/dosagem_auxiliar/delete/<int:id>')#esse id é da linha na tabela Dosagem_piloto
def delete_auxiliar(id):
    #linha da dosagem a ser deletara
    dosagem_deletada_rico = Dosagem_rico.query.filter_by(id=id).first()
    dosagem_deletada_pobre = Dosagem_pobre.query.filter_by(id=id).first()
    #id do ensaio que essa dosagem pertence (.ensaio é o backref pra achar o o elemento "pai")
    dosagem_deletada_pobre.ensaio.id
    dosagem_deletada_pobre.ensaio.id


    db.session.delete(dosagem_deletada_rico)
    db.session.delete(dosagem_deletada_pobre)

    db.session.commit()

    return redirect('/auxiliar/{}'.format(dosagem_deletada_rico.ensaio.id))










@app.route('/resultados/<int:id>', methods=['POST', 'GET'])
def resultados(id):
#    form = Confirmar_dosagem()#Criar esse formulario
#    if form.validate_on_submit():
#        print('validou')
    return render_template('resultados.html', id=id)








@app.route('/corpo_de_prova/<int:id>', methods=['POST', 'GET'])
def corpo_de_prova(id):
#    form = Resistencia()#CRIAR O FORMULARIO DA RESISTENCIA IGUAL DO ALFA
#    if form.validate_on_submit():
#        pass
    return render_template('corpo_de_prova.html', id=id)





@app.route('/corpo_de_prova/deletar/<int:id>')
def deletar_corpo_de_prova(id):
    apagar = Corpo_de_prova.query.get_or_404(id)#CRIAR A TABELA DO CORPO DE PROVA

    try:
        db.session.delete(apagar)
        db.session.commit()
        return redirect('/home')

    except:
        "DEU ERRADO"










    # MODELS 333
class Ensaios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30))
    piloto = db.Column(db.Integer)
    rico = db.Column(db.Integer)
    pobre = db.Column(db.Integer)
    cp = db.Column(db.Integer)
    pesobrita = db.Column(db.Integer)
    slump = db.Column(db.Integer)
    umidade = db.Column(db.Integer)
    dosagem_piloto = db.relationship('Dosagem_piloto', backref='ensaio')
    dosagem_rico = db.relationship('Dosagem_rico', backref='ensaio')
    dosagem_pobre = db.relationship('Dosagem_pobre', backref='ensaio')

    def __repr__(self):
        return '\n<id: {}, nome: {} piloto: {}, rico: {}, pobre: {}, cp: {}, pesobrita: {}, slump: {}, umidade: {}, relation {} >'.format(self.id, self.nome, self.piloto, self.rico, self.pobre, self.cp, self.pesobrita, self.slump, self.umidade, self.dosagem_piloto)


class Dosagem_piloto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    alfa = db.Column(db.Integer)

    c_unitario = db.Column(db.Integer)
    a_unitario = db.Column(db.Integer)
    b_unitario = db.Column(db.Integer)
    
    c_massa = db.Column(db.Integer)
    a_massa = db.Column(db.Integer)
    b_massa = db.Column(db.Integer)
    
    c_acr = db.Column(db.Integer)
    a_acr= db.Column(db.Integer)
    
    umidade_agregado = db.Column(db.Integer)
    agua = db.Column(db.Integer)

    ensaio_id = db.Column(db.Integer, db.ForeignKey('ensaios.id'))
    def __repr__(self):
        return '\n<id: {}, Piloto: {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, foreign: {}>'.format(self.id, self.alfa, self.c_unitario, self.a_unitario, self.b_unitario, self.c_massa, self.a_massa, self.b_massa, self.c_acr, self.a_acr, self.umidade_agregado, self.agua, self.ensaio_id)
   

class Dosagem_rico(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    alfa = db.Column(db.Integer)

    c_unitario = db.Column(db.Integer)
    a_unitario = db.Column(db.Integer)
    b_unitario = db.Column(db.Integer)
    
    c_massa = db.Column(db.Integer)
    a_massa = db.Column(db.Integer)
    b_massa = db.Column(db.Integer)
    
    c_acr = db.Column(db.Integer)
    a_acr= db.Column(db.Integer)
    
    agua = db.Column(db.Integer)

    ensaio_id = db.Column(db.Integer, db.ForeignKey('ensaios.id'))
    def __repr__(self):
        return '\n<id: {}, Rico: {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, foreign: {}>'.format(self.id, self.alfa, self.c_unitario, self.a_unitario, self.b_unitario, self.c_massa, self.a_massa, self.b_massa, self.c_acr, self.a_acr, self.agua, self.ensaio_id)
   
class Dosagem_pobre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    alfa = db.Column(db.Integer)

    c_unitario = db.Column(db.Integer)
    a_unitario = db.Column(db.Integer)
    b_unitario = db.Column(db.Integer)
    
    c_massa = db.Column(db.Integer)
    a_massa = db.Column(db.Integer)
    b_massa = db.Column(db.Integer)
    
    c_acr = db.Column(db.Integer)
    a_acr= db.Column(db.Integer)
    
    agua = db.Column(db.Integer)

    ensaio_id = db.Column(db.Integer, db.ForeignKey('ensaios.id'))
    def __repr__(self):
        return '\n<id: {}, Pobre: {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, foreign: {}>'.format(self.id, self.alfa, self.c_unitario, self.a_unitario, self.b_unitario, self.c_massa, self.a_massa, self.b_massa, self.c_acr, self.a_acr, self.agua, self.ensaio_id)
   




























class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    pets = db.relationship('Pet', backref='owner')

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    owner_id = db.Column(db.Integer, db.ForeignKey('person.id'))
























