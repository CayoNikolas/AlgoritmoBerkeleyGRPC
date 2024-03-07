# AlgoritmoBerkeleyGRPC
Trabalho para a AB2 da disciplina de Sistemas Distribuídos.

## Instalação e execução:
1. Instalar as ferramentas básicas de gRPC para Python: [https://grpc.io/docs/languages/python/basics/](https://grpc.io/docs/languages/python/basics/)
2. Clonar o repositório
3. Rodar os seguintes comando cada um em um terminal diferente:
```bash
python3 slave.py 50052 
```
```bash
python3 slave.py 50053
```
```bash
python3 master.py
```
4. O resultado esperado deve ser algo parecido com isso:
```bash
Hora do servidor: 10
Diferença de Tempo para o servidor: 6
Diferença de Tempo para o servidor: 6
Hora atual: 14
Tempo ajustado com sucesso!
Tempo ajustado com sucesso!
```
Para o terminal que rodou o master e
```bash
Servidor rodando na porta: 50052
Hora atual: 16
Hora atual: 14
```
para os demais terminais.
