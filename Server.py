import socket
import pickle
import numpy as np

# Função para multiplicação de linhas e colunas
def multiply_row_column(matrix_a, matrix_b, row_idx, col_idx):
    return np.dot(matrix_a[row_idx], matrix_b[:, col_idx])

# Configurações do servidor
HOST = '127.0.0.1'
PORT = 12345

# Cria o socket do servidor
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print("Servidor está esperando conexões...")

    # Aceita a conexão do cliente
    conn, addr = server_socket.accept()
    with conn:
        print('Conectado por', addr)

        while True:
            # Recebe os dados do cliente
            data = conn.recv(4096)
            if not data:
                break
            processes = pickle.loads(data)

            # Executa os processos e armazena os resultados
            results = []
            for process in processes:
                row_idx, col_idx = process[2]
                result = multiply_row_column(process[0], process[1], row_idx, col_idx)
                results.append(result)

            # Envia os resultados de volta para o cliente
            conn.sendall(pickle.dumps(results))
        # Fecha a conexão após enviar os resultados
        conn.close()
