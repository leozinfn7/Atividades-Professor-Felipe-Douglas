from conexao import conectar_banco

def atualizar_aluno():

    conn = conectar_banco()

    if conn:

        cursor = conn.cursor()

        id_aluno = input("Digite o ID do aluno: ")
        novo_nome = input("Novo nome: ")

        sql = "UPDATE alunos SET nome = %s WHERE id = %s"

        cursor.execute(sql, (novo_nome, id_aluno))
        conn.commit()

        print("Aluno atualizado com sucesso!")

        cursor.close()
        conn.close()

leia1 = int(input("digite sua idade;"))
leia2 = int (input('digite sua idade:'))

soma = (leia1 + leia2)

print("a soma da idade entre os alunos" ,soma)



idade1 = int(input("digite sua idade: "))
idade2 = int (input('digite sua idade: '))

soma_idade = idade1 + idade2

print("a soma da idade entre os alunos" ,soma_idade)