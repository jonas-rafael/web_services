import sqlite3
banco="banco_8.db"
def criar_basedata():
    with sqlite3.connect(banco) as conexão:
        conexão.execute("""
        create table if not exists contato (
            id integer primary key not null,
            nome text not null,
            email text unique not null,
            fone int not null,
            data_nasc date not null)
            
        
        
        
        
        """)

def cadastrar(nome, email, fone, data_nasc):
    try:
        with sqlite3.connect(banco) as conexão:
            cursor = conexão.execute("insert into contato (nome, email,fone, data_nasc) values(?,?,?,?)",
                                     (nome, email, fone,data_nasc))
            sucesso = cursor.rowcount == 1
    except sqlite3.Error:
        sucesso = False
    return sucesso



def remover(email):
        try:
            with sqlite3.connect(banco) as conexao:
                cursor = conexao.execute("delete from contato where email = ?", (email,))
                sucesso = cursor.rowcount == 1
        except sqlite3.Error:
            sucesso = False
        return sucesso


def atualizar (n_nome,n_email,n_tell,n_data_nasc,id):
   try:
        with sqlite3.connect(banco) as conexão:
            cursor = conexão.execute("update contato set nome = ?, email = ?, fone = ?, data_nasc = ?  where id = ?",
                                 (n_nome,n_email,n_tell,n_data_nasc,id))

            sucesso = cursor.rowcount == 1
   except sqlite3.Error:
       sucesso = False

   return sucesso


def listar():
    tabela =[]
    with sqlite3.connect(banco) as conexão:
        conexão.row_factory = sqlite3.Row
        cursor = conexão.execute("select * from contato")

        for registro in cursor.fetchall():
            tabela.append(dict(registro))
    return  tabela


def buscar(nome):
    tabela=[]
    with sqlite3.connect(banco) as conexão:
        conexão.row_factory = sqlite3.Row
        cursor =conexão.execute(("select nome from contato where nome like = ?",(nome,)))

        for registro in cursor.fetchall():
            tabela.append(dict(registro))
    return tabela




#linha =cursor.fetchone()
#return dict(linha) if linha else {}