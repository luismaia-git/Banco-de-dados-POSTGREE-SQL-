import psycopg2

#ABRE CONEXAO COM UM BANCO DE DADOS EXISTENTE
def conectar_banco():
  try:
    conexao = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='')
  except psycopg2.DatabaseError as error:
    print (error)
  return conexao

'''--------------------------------------------------------------------------------------------'''

def create_aluno():
    try:
        print("Inserindo registro na tabela alunos")
        mat = input('Numero da matricula: ')
        nome = input('Nome: ')
        semestre = input('Semestre: ')
        data_nasc = input('Data de Nascimento: ')
        
        con = conectar_banco()
        cursor = con.cursor()
        SQL = ("INSERT INTO Alunos (mat,nome,semestre,data_nasc) VALUES ('%s','%s',%s,'%s')" %(mat,nome,semestre,data_nasc))
        cursor.execute(SQL)
        con.commit()
        cursor.close()
        con.close()

        return print("\nAluno inserido com sucesso!")
    except psycopg2.DatabaseError as error:
        print("Ocorreu um erro na insercao")
        print (error)
        
def read_aluno():
    try:
        mat = input('Numero da matricula: ')
        
        con = conectar_banco()
        cursor = con.cursor()
        SQL = ("SELECT * FROM Alunos WHERE mat = '%s' " %(mat))
        cursor.execute(SQL)
        con.commit()
        resultado = cursor.fetchall()
        cursor.close()
        con.close() 
        if len(resultado) == 0:
            print("Nao ha oque mostrar")
        else:
            print("\nBusca feita com sucesso!\nResultado:\n")
            return print(resultado)
    except psycopg2.DatabaseError as error:
        print("Ocorreu um erro na busca")
        print (error)

def update_aluno():
    print("Atualizando registro na tabela alunos")
    try:
        con = conectar_banco()
        cursor = con.cursor()

        matricula = input('Numero da matricula do aluno que deseja atualizar os dados: ')
        SQL = ("SELECT * FROM Alunos WHERE mat = '%s' " %(matricula))
        cursor.execute(SQL)
        con.commit()
        resultado = cursor.fetchall()
        if len(resultado) == 0:
            print("Nao ha oque mostrar")
        else:
            print("Registro encontrado:\n")
            print(resultado)

        mat = input('Numero da matricula: ')
        nome = input('Nome: ')
        semestre = input('Semestre: ')
        data_nasc = input('Data de Nascimento: ')
        
        
        SQL = ("UPDATE Alunos set mat = '%s',nome = '%s',semestre= %s,data_nasc= '%s' WHERE mat = '%s' " %(mat,nome,semestre,data_nasc,matricula))
        cursor.execute(SQL)
        con.commit()
        cursor.close()
        con.close()
        

        return print("\nAluno atualizado com sucesso!")
    except psycopg2.DatabaseError as error:
        print("Ocorreu um erro na atualizacao")
        print (error)

def delete_aluno():

    try:
        print("Deletando registro na tabela alunos")
        mat = input('Numero da matricula: ')
        
        con = conectar_banco()
        cursor = con.cursor()
        SQL = ("DELETE FROM Alunos WHERE mat = '%s' " %(mat)) 
        cursor.execute(SQL)
        con.commit()
        cursor.close()
        con.close()

        return print("\nAluno excluído com sucesso!")
    except psycopg2.DatabaseError as error:
        print("Ocorreu um erro na exclusao do aluno")
        print (error)

'''--------------------------------------------------------------------------------------------'''
#funcoes disciplinas

def create_disciplinas():
    try:
        print("Inserindo registro na tabela Disciplinas")
        cod_disc = input('Código da Disciplina: ')
        nome = input('Nome: ')
        creditos = input('Créditos: ')
                
        con = conectar_banco()
        cursor = con.cursor()
        SQL = ("INSERT INTO Disciplinas (cod_disc, nome, creditos) VALUES (%s,'%s',%s)" %(cod_disc,nome,creditos))
        cursor.execute(SQL)
        con.commit()
        cursor.close()
        con.close()

        return print("\nDisciplina inserida com sucesso!")
    except psycopg2.DatabaseError as error:
        print("Ocorreu um erro na insercao")
        print (error)
        
def read_disciplinas():
    try:
        cod_disc = input('Código da Disciplina: ')
        con = conectar_banco()
        cursor = con.cursor()
        SQL = ("SELECT * FROM Disciplinas WHERE cod_disc = %s " %(cod_disc))
        cursor.execute(SQL)
        con.commit()
        resultado = cursor.fetchall()
        cursor.close()
        con.close() 
        if len(resultado) == 0:
            print("Nao ha oque mostrar")
        else:
            print("\nBusca feita com sucesso!\nResultado:\n")
            return print(resultado)
    except psycopg2.DatabaseError as error:
        print("Ocorreu um erro na busca")
        print (error)

def update_disciplinas():
    print("Atualizando registro na tabela Disciplinas")
    try:
        con = conectar_banco()
        cursor = con.cursor()

        codigo = input('Código da Disciplina que deseja atualizar os dados: ')
        SQL = ("SELECT * FROM Disciplinas WHERE cod_disc = %s " % codigo)
        cursor.execute(SQL)
        con.commit()
        resultado = cursor.fetchall()
        if len(resultado) == 0:
            print("Nao ha oque mostrar")
        else:
            print("Registro encontrado:\n")
            print(resultado)

        cod_disc = input('Código da Disciplina: ')
        nome = input('Nome: ')
        creditos = input('Créditos: ')
        
        
        SQL = ("UPDATE Disciplinas set cod_disc = %s, nome = '%s', creditos = '%s' WHERE cod_disc = %s " %(cod_disc, nome, creditos, codigo))
        cursor.execute(SQL)
        con.commit()
        cursor.close()
        con.close()
        

        return print("\nDisciplina atualizado com sucesso!")
    except psycopg2.DatabaseError as error:
        print("Ocorreu um erro na atualizacao")
        print (error)

def delete_disciplinas():

    try:
        print("Deletando registro na tabela Disciplinas")
        cod_disc = input('Código do Disciplina: ')
        
        con = conectar_banco()
        cursor = con.cursor()
        SQL = ("DELETE FROM Disciplinas WHERE cod_disc = %s " %(cod_disc)) 
        cursor.execute(SQL)
        con.commit()
        cursor.close()
        con.close()

        return print("\nDisciplina excluída com sucesso!")
    except psycopg2.DatabaseError as error:
        print("Ocorreu um erro na exclusao da Disciplina")
        print (error)

'''--------------------------------------------------------------------------------------------'''
#funcoes historico

def create_historico():
    try:
        print("Inserindo registro na tabela Historico")
        cod_hist = input('Código do historico: ')
        mat = input('Códiga matricula: ')
        cod_turma = input('Código da turma: ')
        cod_disc= input('Código da disciplina: ')
        cod_prof = input('Código do professor: ')
        ano = input('Ano: ')
        frequencia = input('Frequencia: ')
        nota = input('Nota: ')
                
        con = conectar_banco()
        cursor = con.cursor()
        SQL = ("INSERT INTO Historico (cod_hist,mat,cod_turma,cod_disc,cod_prof,ano,frequencia,nota) VALUES (%s, '%s', %s, %s, %s, '%s', %s, %s)" %(cod_hist, mat, cod_turma, cod_disc, cod_prof,ano,frequencia,nota))
        cursor.execute(SQL)
        con.commit()
        cursor.close()
        con.close()

        return print("\nDados inseridos com sucesso!")
    except psycopg2.DatabaseError as error:
        print("Ocorreu um erro na insercao")
        print (error)
        
def read_historico():
    try:
        cod_hist = input('Código do Historico: ')
        
        con = conectar_banco()
        cursor = con.cursor()
        SQL = ("SELECT * FROM Historico WHERE cod_hist= %s " %(cod_hist))
        cursor.execute(SQL)
        con.commit()
        resultado = cursor.fetchall()
        cursor.close()
        con.close() 
        if len(resultado) == 0:
            print("Nao ha oque mostrar")
        else:
            print("\nBusca feita com sucesso!\nResultado:\n")
            return print(resultado)
    except psycopg2.DatabaseError as error:
        print("Ocorreu um erro na busca")
        print (error)

def update_historico():
    print("Atualizando registro na tabela Historico")
    try:
        con = conectar_banco()
        cursor = con.cursor()

        codigo = input('Código do historico de um aluno que deseja atualizar os dados: ')
        SQL = ("SELECT * FROM Historico WHERE cod_hist = %s " % codigo)
        cursor.execute(SQL)
        con.commit()
        resultado = cursor.fetchall()
        if len(resultado) == 0:
            print("Nao ha oque mostrar")
        else:
            print("Registro encontrado:\n")
            print(resultado)

        cod_hist = input('Código da Historico: ')
        mat = input('Digite a matricula: ')
        cod_turma = input('Codigo da turma: ')
        cod_disc = input('Codigo da disciplina: ')
        cod_prof = input('Código do professor: ')
        ano = input('Ano: ')
        frequencia = input('Frequencia: ')
        nota = input('Nota: ')
        
        
        SQL = ("UPDATE Historico set cod_hist = %s, mat = '%s', cod_turma = %s, cod_disc = %s, cod_prof = %s, ano = '%s', frequencia = %s, nota = %s WHERE cod_hist = %s " %(cod_hist, mat, cod_turma, cod_disc, cod_prof, ano, frequencia, nota, codigo))
        cursor.execute(SQL)
        con.commit()
        cursor.close()
        con.close()
        

        return print("\nHistorico atualizado com sucesso!")
    except psycopg2.DatabaseError as error:
        print("Ocorreu um erro na atualizacao")
        print (error)

def delete_historico():

    try:
        print("Deletando registro na tabela Historico")
        cod_hist = input('Código da Historico: ')
        
        con = conectar_banco()
        cursor = con.cursor()
        SQL = ("DELETE FROM Historico WHERE cod_hist = %s " %(cod_hist)) 
        cursor.execute(SQL)
        con.commit()
        cursor.close()
        con.close()

        return print("\nHistorico excluído com sucesso!")
    except psycopg2.DatabaseError as error:
        print("Ocorreu um erro na exclusao")
        print (error)

'''--------------------------------------------------------------------------------------------'''
def create_professores():
    try:
        print("Inserindo registro na tabela Professores")
        cod_prof = input('Código do professor: ')
        nome = input('Nome: ')
        area_pesquisa = input('Área de Pesquisa: ')
                
        con = conectar_banco()
        cursor = con.cursor()
        SQL = ("INSERT INTO Professores (cod_prof, nome, area_pesquisa) VALUES (%s,'%s','%s')" %(cod_prof,nome,area_pesquisa))
        cursor.execute(SQL)
        con.commit()
        cursor.close()
        con.close()

        return print("\nProfessor inserido com sucesso!")
    except psycopg2.DatabaseError as error:
        print("Ocorreu um erro na insercao")
        print (error)
        
def read_professores():
    try:
        cod_prof = input('Código do professor: ')
        
        con = conectar_banco()
        cursor = con.cursor()
        SQL = ("SELECT * FROM Professores WHERE cod_prof = %s " %(cod_prof))
        cursor.execute(SQL)
        con.commit()
        resultado = cursor.fetchall()
        cursor.close()
        con.close() 
        if len(resultado) == 0:
            print("Nao ha oque mostrar")
        else:
            print("\nBusca feita com sucesso!\nResultado:\n")
            return print(resultado)
    except psycopg2.DatabaseError as error:
        print("Ocorreu um erro na busca")
        print (error)

def update_professores():
    print("Atualizando registro na tabela Professores")
    try:
        con = conectar_banco()
        cursor = con.cursor()

        codigo = input('Código do professor que deseja atualizar os dados: ')
        SQL = ("SELECT * FROM Professores WHERE cod_prof = %s " % codigo)
        cursor.execute(SQL)
        con.commit()
        resultado = cursor.fetchall()
        if len(resultado) == 0:
            print("Nao ha oque mostrar")
        else:
            print("Registro encontrado:\n")
            print(resultado)

        cod_prof = input('Código do professor: ')
        nome = input('Nome: ')
        area_pesquisa = input('Área de Pesquisa: ')
        
        
        SQL = ("UPDATE Professores set cod_prof = %s, nome = '%s', area_pesquisa = '%s' WHERE cod_prof = %s " %(cod_prof, nome, area_pesquisa, codigo))
        cursor.execute(SQL)
        con.commit()
        cursor.close()
        con.close()
        

        return print("\nProfessor atualizado com sucesso!")
    except psycopg2.DatabaseError as error:
        print("Ocorreu um erro na atualizacao")
        print (error)

def delete_professores():

    try:
        print("Deletando registro na tabela Professores")
        cod_prof = input('Código do professor: ')
        
        con = conectar_banco()
        cursor = con.cursor()
        SQL = ("DELETE FROM Professores WHERE cod_prof = %s " %(cod_prof)) 
        cursor.execute(SQL)
        con.commit()
        cursor.close()
        con.close()

        return print("\nProfessor excluído com sucesso!")
    except psycopg2.DatabaseError as error:
        print("Ocorreu um erro na exclusao do professor")
        print (error)

'''--------------------------------------------------------------------------------------------'''
#funcoes turmas

def create_turmas():
    try:
        print("Inserindo registro na tabela Turmas")
        cod_turma= input('Código da turma: ')
        cod_disc= input('Código da disciplina: ')
        cod_prof = input('Código do professor: ')
        ano = input('Ano: ')
        horario = input('Horario: ')
                
        con = conectar_banco()
        cursor = con.cursor()
        SQL = ("INSERT INTO Turmas (cod_turma, cod_disc, cod_prof, ano, horario) VALUES (%s, %s, %s, '%s', '%s')" %(cod_turma,cod_disc,cod_prof,ano,horario))
        cursor.execute(SQL)
        con.commit()
        cursor.close()
        con.close()

        return print("\nTurma inserida com sucesso!")
    except psycopg2.DatabaseError as error:
        print("Ocorreu um erro na insercao")
        print (error)
        
def read_turmas():
    try:
        cod_turma = input('Código da Turma: ')
        
        con = conectar_banco()
        cursor = con.cursor()
        SQL = ("SELECT * FROM Turmas WHERE cod_turma = %s " %(cod_turma))
        cursor.execute(SQL)
        con.commit()
        resultado = cursor.fetchall()
        cursor.close()
        con.close() 
        if len(resultado) == 0:
            print("Nao ha oque mostrar")
        else:
            print("\nBusca feita com sucesso!\nResultado:\n")
            return print(resultado)
    except psycopg2.DatabaseError as error:
        print("Ocorreu um erro na busca")
        print (error)

def update_turmas():
    print("Atualizando registro na tabela turmas")
    try:
        con = conectar_banco()
        cursor = con.cursor()

        codigo = input('Código da turma que deseja atualizar os dados: ')
        SQL = ("SELECT * FROM Turmas WHERE cod_turma = %s " % codigo)
        cursor.execute(SQL)
        con.commit()
        resultado = cursor.fetchall()
        if len(resultado) == 0:
            print("Nao ha oque mostrar")
        else:
            print("Registro encontrado:\n")
            print(resultado)

        cod_turma = input('Código da turma: ')
        cod_disc = input('Código da discplina: ')
        cod_prof = input('Código do professor: ')
        ano = input('Ano: ')
        horario = input('Horario: ')
        
        
        SQL = ("UPDATE Turmas set cod_turma = %s, cod_disc = %s, cod_prof= %s, ano = '%s', horario = '%s' WHERE cod_turma = '%s' " %(cod_turma, cod_disc, cod_prof, ano, horario, codigo))
        cursor.execute(SQL)
        con.commit()
        cursor.close()
        con.close()
        

        return print("\nTurma atualizada com sucesso!")
    except psycopg2.DatabaseError as error:
        print("Ocorreu um erro na atualizacao")
        print (error)

def delete_turmas():

    try:
        print("Deletando registro na tabela Turmas")
        cod_turma = input('Código da turma: ')
        
        con = conectar_banco()
        cursor = con.cursor()
        SQL = ("DELETE FROM Turmas WHERE cod_turma = %s " %(cod_turma)) 
        cursor.execute(SQL)
        con.commit()
        cursor.close()
        con.close()

        return print("\nTurma excluída com sucesso!")
    except psycopg2.DatabaseError as error:
        print("Ocorreu um erro na exclusao")
        print (error)

'''--------------------------------------------------------------------------------------------'''
#MENU DOS CRUDS
def alunos():

    while True:
        print("============MENU CRUD ALUNOS============")
        print("Deseja Inserir dados ? (1)")
        print("Deseja Buscar dados ? (2)")
        print("Deseja Atualizar dados ? (3)")
        print("Deseja Deletar dados ? (4)")
        print("Deseja voltar para o menu principal? (0)")
        print("="*40)
        resposta = int(input("Qual sua opcao: "))

        if resposta == 0:
            break
        elif resposta == 1:
            create_aluno()
        elif resposta == 2:
            read_aluno()
        elif resposta == 3:
            update_aluno()
        elif resposta == 4:
            delete_aluno()
        else:
            print("Entrada invalida")
        print('')

def disciplinas():
    while True:
        print("=========MENU CRUD DISCIPLINAS==========")
        print("Deseja Inserir dados ? (1)")
        print("Deseja Buscar dados ? (2)")
        print("Deseja Atualizar dados ? (3)")
        print("Deseja Deletar dados ? (4)")
        print("Deseja voltar para o menu principal? (0)")
        print("="*40)
        resposta = int(input("Qual sua opcao: "))

        if resposta == 0:
            break
        elif resposta == 1:
            create_disciplinas()
        elif resposta == 2:
            read_disciplinas()
        elif resposta == 3:
            update_disciplinas()
        elif resposta == 4:
            delete_disciplinas()
        else:
            print("Entrada invalida")
        print('')

def historico():
    while True:
        print("==========MENU CRUD HISTORICO===========")
        print("Deseja Inserir dados ? (1)")
        print("Deseja Buscar dados ? (2)")
        print("Deseja Atualizar dados ? (3)")
        print("Deseja Deletar dados ? (4)")
        print("Deseja voltar para o menu principal? (0)")
        print("="*40)
        resposta = int(input("Qual sua opcao: "))

        if resposta == 0:
            break
        elif resposta == 1:
            create_historico()
        elif resposta == 2:
            read_historico()
        elif resposta == 3:
            update_historico()
        elif resposta == 4:
            delete_historico()
        else:
            print("Entrada invalida")
        print('')

def professores():
    while True:
        print("=========MENU CRUD PROFESSORES==========")
        print("Deseja Inserir dados ? (1)")
        print("Deseja Buscar dados ? (2)")
        print("Deseja Atualizar dados ? (3)")
        print("Deseja Deletar dados ? (4)")
        print("Deseja voltar para o menu principal? (0)")
        print("="*40)
        resposta = int(input("Qual sua opcao: "))

        if resposta == 0:
            break
        elif resposta == 1:
            create_professores()
        elif resposta == 2:
            read_professores()
        elif resposta == 3:
            update_professores()
        elif resposta == 4:
            delete_professores()
        else:
            print("Entrada invalida")
        print('')

def turmas():
    while True:
        print("============MENU CRUD TURMAS============")
        print("Deseja Inserir dados ? (1)")
        print("Deseja Buscar dados ? (2)")
        print("Deseja Atualizar dados ? (3)")
        print("Deseja Deletar dados ? (4)")
        print("Deseja voltar para o menu principal? (0)")
        print("="*40)
        resposta = int(input("Qual sua opcao: "))

        if resposta == 0:
            break
        elif resposta == 1:
            create_turmas()
        elif resposta == 2:
            read_turmas()
        elif resposta == 3:
            update_turmas()
        elif resposta == 4:
            delete_turmas()
        else:
            print("Entrada invalida")
        print('')

'''--------------------------------------------------------------------------------------------'''

def main():
  
    while True:
        print("=============MENU DE ESCOLHA=============")
        print("TABELA: Alunos (1)")
        print("TABELA: Disciplinas (2)")
        print("TABELA: Historico (3)")
        print("TABELA: Professores (4)")
        print("TABELA: Turmas (5)")
        print("Deseja encerrar o programa? (0)")
        print("="*40)
        resposta = int(input("Qual sua opcao: "))
        print('')

        if resposta == 0:
            break
        elif resposta == 1:
            alunos()
        elif resposta == 2:
            disciplinas()
        elif resposta == 3:
            historico()
        elif resposta == 4:
            professores()
        elif resposta == 5:
            turmas()
        else:
            print("Entrada invalida")
        print('')

main()