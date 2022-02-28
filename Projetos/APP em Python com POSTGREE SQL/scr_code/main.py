import funcoes as fn

'''
Programa feito em Python para desenvolver uma aplicação para o cliente que consome o serviço de banco de dados(PostgreSQL)
'''

# 2.2 Criando as tabelas

#Comandos SQL para deletar registros e tabelas para teste do programa
print("Deletando os registros e as tabelas... : ")
SQL = 'DELETE FROM Historico; DELETE FROM Turmas; DELETE FROM Alunos; DELETE FROM Disciplinas; DELETE FROM Professores; '
fn.comando_sql(SQL)

SQL = 'DROP TABLE IF EXISTS Alunos, Disciplinas, Professores, Turmas, Historico'
fn.comando_sql(SQL)



print('')
print("="*50)
print("Criando as tabelas... :")
SQL = '''CREATE TABLE Alunos(mat varchar(6) not null, 
                nome varchar(100) not null, 
                semestre int not null, 
                data_nasc varchar not null, 
                primary key(mat));'''
fn.comando_sql(SQL)



SQL = '''CREATE TABLE Disciplinas (cod_disc serial, 
                nome varchar(100) not null,
                creditos int not null,
                primary key (cod_disc) ); '''
fn.comando_sql(SQL)


SQL = '''CREATE TABLE Professores (cod_prof serial,
                nome varchar(100) not null,
                area_pesquisa varchar not null,
                primary key (cod_prof) ); '''
fn.comando_sql(SQL)



SQL = '''CREATE TABLE Turmas (cod_turma serial,
                cod_disc int not null,
                cod_prof int not null,
                ano varchar(6) not null,
                horario varchar not null,
                primary key (cod_turma),
                FOREIGN KEY (cod_disc)
                REFERENCES Disciplinas(cod_disc),
                FOREIGN KEY (cod_prof) 
                REFERENCES Professores(cod_prof) );'''
fn.comando_sql(SQL)


SQL = '''CREATE TABLE Historico ( cod_hist SERIAL PRIMARY KEY, 
                mat varchar(6) not null, 
                cod_turma int not null, 
                cod_disc int not null, 
                cod_prof int not null, 
                ano varchar(6) not null, 
                frequencia real not null, 
                nota int not null,  
                FOREIGN KEY (mat) 
                REFERENCES Alunos(mat), 
                FOREIGN KEY (cod_turma)  
                REFERENCES Turmas(cod_turma), 
                FOREIGN KEY (cod_disc) 
                REFERENCES Disciplinas(cod_disc), 
                FOREIGN KEY (cod_prof) 
                REFERENCES Professores(cod_prof) );'''

fn.comando_sql(SQL)
#2.3
#Lendo os arquivos csv dados pelo professor
print('')
print("="*50)
print("Inserindo registros dos arquivos csv... :")

fn.insert_alunos()    

fn.insert_disc()            

fn.insert_profs()            

fn.insert_turmas()         

fn.insert_hist()


#2.3.5 Inserindo outros dados

print('')
print("="*50)
print("Inserindo novos registros: ")
SQL = """INSERT INTO Alunos (mat,nome,semestre,data_nasc)
      VALUES ('29382', 'Jose Machado', '1','02-05-2002'), 
      ('29308', 'Lucas Sampaio', '2', '18-06-2001'),
      ('29839', 'Isabel Silva', '1', '11-01-2002'),
      ('39288', 'Ana Barros', '4', '05-03-2000');

      INSERT INTO Disciplinas (cod_disc,nome,creditos)
      VALUES (20, 'Sistemas Distribuídos', 4),
      (21, 'Linguagens de Programação I', 6),
      (22, 'Análise e Projeto de Sistemas I', 4),
      (23, 'Seminários em Computação', 4);

      INSERT INTO Professores (cod_prof,nome,area_pesquisa)
      VALUES (20, 'Francisco Heron', 'Computação de Alto Desempenho'),
      (21, 'Pablo Mayckon', 'Lógica'),
      (22, 'João Bosco', 'Engenharia de Software'),
      (23, 'Paulo Rego', 'Redes de Computadores');

      INSERT INTO Turmas (cod_turma,cod_disc,cod_prof,ano,horario)
      VALUES (20, 20, 23, '2020.1', '08h-10h'),
      (21, 21, 20, '2020.2', '10h-12h'),
      (22, 22, 22, '2020.2', '08h-10h'),
      (23, 23, 21, '2020.1', '14h-16h');
    
      INSERT INTO Historico (cod_hist,mat, cod_turma, cod_disc, cod_prof, ano, frequencia, nota)
      VALUES (159,'29382',20, 20, 23, '2020.1', 0.59, 6), 
      (160,'29308', 21, 21, 20, '2020.2', 0.72, 8),
      (161,'29839', 22, 22, 22, '2020.2', 0.82, 7),
      (162,'39288', 23, 23, 21, '2020.1', 0.64, 6),
      (163,'29382',6, 6, 3, '2021.1', 0.59, 3), 
      (164,'29308', 6, 6, 3, '2021.1', 0.72, 4),
      (165,'29839', 6, 6, 3, '2021.1', 0.82, 10),
      (166,'39288', 6, 6, 3, '2021.1', 0.64, 9);
    """

fn.comando_sql(SQL)

#2.4 Consulta
print('')
print("="*50)
print('Consultas: ')
#item 1
SQL = ''' SELECT a.mat, a.nome 
          FROM Alunos a, Historico h, Disciplinas d
          WHERE a.mat = h.mat AND h.cod_disc = d.cod_disc AND
          d.nome = 'Fundamentos de Banco de Dados' AND h.nota > 7 
      '''
fn.consulta(SQL)



#item 2
SQL = ''' SELECT ROUND(AVG(h.nota),2) AS MEDIA
          FROM Alunos a, Historico h, Disciplinas d
          WHERE a.mat = h.mat AND h.cod_disc = d.cod_disc AND d.nome = 'Computação Gráfica I'
      '''

fn.consulta(SQL)

#item 3
SQL = ''' SELECT a.nome as Aluno, d.nome as Disciplina
          FROM Alunos a, Historico h, Disciplinas d
          WHERE a.mat = h.mat AND h.cod_disc = d.cod_disc AND h.frequencia < 0.75
      '''
fn.consulta(SQL)

#item 4
SQL = '''
      SELECT COUNT(Tr.cod_turma) AS QUANTIDADE_de_ALUNOS, Pr.nome as Nome_professor FROM HISTORICO AS HS
            JOIN TURMAS AS Tr ON HS.cod_turma = Tr.cod_turma
            JOIN PROFESSORES AS Pr ON HS.cod_prof = Pr.cod_prof
      WHERE
            Pr.area_pesquisa = 'Algoritmos e Otimização'
      GROUP BY Tr.cod_turma, Pr.nome
      HAVING COUNT(Tr.cod_turma) >= 5;
      '''

fn.consulta(SQL)

#item 5
SQL = ''' SELECT a.nome, a.data_nasc
          FROM Alunos a, Historico h, Disciplinas d
          WHERE a.mat = h.mat AND h.cod_disc = d.cod_disc AND
          d.nome = 'Fundamentos de Banco de Dados' AND h.nota < 5 AND h.ano = '2021.1'
      '''
fn.consulta(SQL)



#2.5 Transacao
print('')
print("Transacoes: ")

SQL = '''INSERT INTO Alunos (mat,nome,semestre,data_nasc)
         VALUES ('392889', 'Tiago', 3, '09-04-2001');

        INSERT INTO Historico (cod_hist,mat, cod_turma, cod_disc, cod_prof, ano, frequencia, nota)
        VALUES (167, '392889', 1, 1, 1, '2020.1', 0.90, 8);
      '''
fn.comando_sql(SQL)

SQL = '''SELECT a.mat, a.nome 
        FROM Alunos a, Historico h, Disciplinas d
        WHERE a.mat = h.mat AND h.cod_disc = d.cod_disc AND
        d.nome = 'Fundamentos de Banco de Dados' AND h.nota > 8'''

fn.consulta(SQL)
print('')


