


'''

id que eu tenho é o valor do id na tabela ENSAIOS

entrei no auxiliar


se validar

    se a linha com id tal da tabela ensaio nao possuir nenhum filho rico
        crie a instancia rico e pobre

    se tiver filho rico
        recalcule os valores







if objeto.dosagem_rico == []:
    cria os filhos rico e pobre

else:
    delete o objeto.dosagem_rico[0]
    commit()
    cria os filhos rico e pobre




objeto = Ensaios.query.filter_by(id=id).first()
    vai me dar a linha da tabela Ensaios com o id=id

objeto.dosagem_rico
    vai me dar uma LISTA elementos filhos

objeto.dosagem_rico[0]
    da a linha da tabela Dosagem_rico na posição 0

objeto.dosagem_rico[0].XXX
    da o valor XXX da linha 0 da tabela Dosagem_rico



partindo do filho
filho = Dosagem_rico.query.filter_by(id=1).first()
    da a linha da tabela Dosagem_rico com o id=1

filho.id
    da o id dele
    ...

filho.backref
    da o objeto pai, que é uma linha da tabela Ensaios

filho.backref.name
    da o valor name do objeto pai


'''






def dosagem_auxiliar(id):

	ensaio_salvo = Ensaios.query.filter_by(id=id).first()

	m_rico = ensaio_salvo.rico
	m_pobre = ensaio_salvo.pobre
	cp = ensaio_salvo.cp
	alfa = form.alfa.data
	pesobrita = ensaio_salvo.pesobrita
	slump = ensaio_salvo.slump


	if form.validate_on_submit():

		if ensaio_salvo.dosagem_rico == []:
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


            print('add no db pobre')
            print(add_no_db_pobre)
            print('dosagens no ensaio salvo rico')
            print(dosagens_do_ensaio_salvo_rico)

            db.session.add(add_no_db_rico)
            db.session.add(add_no_db_pobre)
            db.session.commit()

        else:
            rico_velho = ensaio_salvo.dosagem_rico[0]
            pobre_velho = ensaio_salvo.dosagem_pobre[0]
            db.session.delete(rico_velho)
            db.session.delete(pobre_velho)

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
            db.session.add(add_no_db_rico)
            db.session.add(add_no_db_pobre)
            db.session.commit()

        return redirect('/auxiliar/{}'.format(id))
    return render_template("auxiliar.html", form=form, id=id, dosagens_do_ensaio_salvo_rico=dosagens_do_ensaio_salvo_rico, dosagens_do_ensaio_salvo_pobre=dosagens_do_ensaio_salvo_pobre, m_rico=m_rico, m_pobre=m_pobre, slump=slump)



































