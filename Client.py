import socket
import pickle
import numpy as np

# Função para enviar processos ao servidor e receber os resultados
def send_processes_to_server(processes):
    # Configurações do servidor
    HOST = '127.0.0.1'
    PORT = 12345

    # Cria o socket do cliente
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))

        # Envia os processos para o servidor
        client_socket.sendall(pickle.dumps(processes))

        # Recebe os resultados dos processos do servidor
        data = client_socket.recv(4096)
        results = pickle.loads(data)

        return results

# Matrizes de exemplo
matrix_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_b = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# Lista de processos a serem executados
processes = []
for i in range(matrix_a.shape[0]):
    for j in range(matrix_b.shape[1]):
        processes.append((i, j))

# Chama a função para enviar os processos ao servidor e receber os resultados
results = send_processes_to_server([(matrix_a, matrix_b, process) for process in processes])

print("Matriz A:")
print(matrix_a)
print("")
print("Matriz B:")
print(matrix_b)
print("")

# Exibe os resultados
for i, result in enumerate(results):
    row_idx = processes[i][0]
    col_idx = processes[i][1]
    print(f"Resultado da multiplicação da {row_idx+1}ª linha de A pela {col_idx+1}ª coluna de B: {result}")
