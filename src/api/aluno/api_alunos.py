# realizar o CRUD de alunos aqui
from flask import render_template, request, redirect, url_for, jsonify
from models.models_aluno import banco_de_dados
from models.models_aluno import Aluno

class AlunoApi:
    id = 0
    @staticmethod
    def AlunoPost():
        if request.method == 'POST':
            data = request.get_json()
            if not data or not all(k in data for k in ( "nome", "idade", "turma_id", "data_nascimento", "nota_primeiro_semestre", "nota_segundo_semestre" )):
                return jsonify({"error": " nome, idade, id de turma, data de nascimento e notas são obrigatorios"})
        novo_aluno = Aluno(
            id = id,
            nome = data["nome"],
            idade = data["idade"],
            turma_id = data["turma_id"],
            data_nascimento = data["data_nascimento"],
            nota_primeiro_semestre = data["nota_primeiro_semestre"],
            nota_segundo_semestre = data["nota_segundo_semestre"],
            media_final = (data["nota_primeiro_semestre"] + data["nota_segundo_semestre"])/2,
        )
        banco_de_dados.session.add(novo_aluno)
        banco_de_dados.session.commit()
        id = id + 1
        return jsonify({
            "id": novo_aluno.id,
            "nome": novo_aluno.nome,
            "idade": novo_aluno.idade,
            "turma_id": novo_aluno.turma_id,
            "data_nascimento": novo_aluno.data_nascimento,
            "nota_primeiro_semestre": novo_aluno.nota_primeiro_semestre,
            "nota_segundo_semestre": novo_aluno.nota_segundo_semestre,
            "media_final" = novo_aluno.media_final

        }), 201
    # TODO implementar os outros métodos aqui abaixo
    def update_aluno(id, id_turma):
        aluno = Aluno.query.get(id)
        if aluno:
            aluno.turma_id = id_turma
            db.session.commit()
        else:
            return "aluno não encontrado", 404

        return aluno
    def delete_aluno(id):
        aluno = Aluno.query.get(id)
        if aluno:
            db.session.delete(aluno)
            db.session.commit()
        else:
            return "aluno não encontrado", 404
        
