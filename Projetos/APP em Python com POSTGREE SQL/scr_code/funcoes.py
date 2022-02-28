import psycopg2

#ABRE CONEXAO COM UM BANCO DE DADOS EXISTENTE
def conectar_banco():
  try:
    conexao = psycopg2.connect(host='localhost', database='postgres', user='postgres', password='')
  except psycopg2.DatabaseError as error:
    print (error)
  return conexao

#funcao para receber um comando SQL
def comando_sql(SQL):
    try:
      con = conectar_banco()
      cursor = con.cursor()
      cursor.execute(SQL)
      con.commit()
      print("Comando realizado com sucesso!")
      cursor.close()
      con.close()
    except psycopg2.DatabaseError as error:
      print (error)
    

#Funcao para receber um comando SQL(uma consulta). A funcao retorna um vetor com os resultados.
def consulta(SQL):
  try:
    con = conectar_banco()
    cursor = con.cursor()
    cursor.execute(SQL)
    con.commit()
    print("Comando realizado com sucesso!")
    resultado = cursor.fetchall()
    cursor.close()
    con.close()
    print('')
    print("Resultado da consulta:")
    if len(resultado) == 0:
      print("Nao ha oque mostrar")
    else:
      print(resultado)
  except psycopg2.DatabaseError as error:
      print (error)

#Funcoes de insercao para a leitura dos arquivos CSV dados pelo professor

def insert_turmas():
  arquivo = open("./dados/Turmas.csv", 'r' , encoding='utf8')

  linhas = arquivo.readlines()

  exe = "INSERT INTO Turmas (cod_turma, cod_disc, cod_prof, ano, horario) VALUES "
  for i in range(1, len(linhas) - 1):
    dados = linhas[i].replace('\n','').split(',')
    exe += ("(%s, %s, %s, '%s', '%s'), " % (dados[0], dados[1], dados[2], dados[3], dados[4]))

  dados = linhas[len(linhas) - 1].replace('\n','').split(',')
  exe += ("(%s, %s, %s, '%s', '%s');" % (dados[0], dados[1], dados[2], dados[3], dados[4]))
  
  comando_sql(exe)

def insert_profs():
  arquivo = open("./dados/Professores.csv", 'r' , encoding='utf8')

  linhas = arquivo.readlines()

  exe = "INSERT INTO Professores (cod_prof, nome, area_pesquisa) VALUES "
  for i in range(1, len(linhas) - 1):
    dados = linhas[i].replace('\n','').split(',')
    exe += ("(%s, '%s', '%s'), " % (dados[0], dados[1], dados[2]))

  dados = linhas[len(linhas) - 1].replace('\n','').split(',')
  exe += ("(%s, '%s', '%s');" % (dados[0], dados[1], dados[2]))

  comando_sql(exe)

def insert_alunos():
  arquivo = open("./dados/Alunos.csv", 'r' , encoding='utf8')

  linhas = arquivo.readlines()

  exe = "INSERT INTO Alunos (mat,nome,semestre,data_nasc) VALUES "
  for i in range(1, len(linhas) - 1):
    dados = linhas[i].replace('\n','').split(',')
    exe += ("('%s', '%s', %s, '%s'), " % (dados[0], dados[1], dados[2], dados[3]))

  dados = linhas[len(linhas) - 1].replace('\n','').split(',')
  exe += ("('%s', '%s', %s, '%s');" % (dados[0], dados[1], dados[2], dados[3]))
  
  comando_sql(exe)

def insert_disc():
  arquivo = open("./dados/Disciplinas.csv", 'r', encoding='utf8')
  linhas = arquivo.readlines()

  exe = "INSERT INTO Disciplinas (cod_disc,nome,creditos) VALUES "
  for i in range(1, len(linhas) - 1):
    dados = linhas[i].replace('\n','').split(',')
    exe += ("(%s, '%s', %s), " % (dados[0], dados[1], dados[2]))

  dados = linhas[len(linhas) - 1].replace('\n','').split(',')
  exe += ("(%s, '%s', %s);" % (dados[0], dados[1], dados[2]))
  
  comando_sql(exe)

def insert_hist():
  arquivo = open("./dados/Historico.csv", 'r' , encoding='utf8')

  linhas = arquivo.readlines()

  exe = "INSERT INTO Historico (cod_hist,mat,cod_turma,cod_disc,cod_prof,ano,frequencia,nota) VALUES "
  for i in range(1, len(linhas) - 1):
    dados = linhas[i].replace('\n','').split(',')
    exe += ("(%s, '%s', %s, %s, %s, '%s', %s, %s), " % (dados[0], dados[1], dados[2], dados[3], dados[4], dados[5], dados[6], dados[7]))

  dados = linhas[len(linhas) - 1].replace('\n','').split(',')
  exe += ("(%s, '%s', %s, %s, %s, '%s', %s, %s);" % (dados[0], dados[1], dados[2], dados[3], dados[4], dados[5], dados[6], dados[7]))

  comando_sql(exe)