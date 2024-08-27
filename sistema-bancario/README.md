# Sistema Bancário
![Python](https://img.shields.io/badge/Python-3.8-blue.svg)
## 📜 Descrição

O **`sistema_bancario.py`** é um projeto em Python que simula um sistema bancário básico. Este sistema permite realizar operações essenciais como depósitos, saques e consultar o extrato da conta. Desenvolvido para fins educacionais, o sistema inclui verificações de segurança, limites para saques e um menu interativo para facilitar a navegação.

## 🚀 Funcionalidades

- **Depósito:** Adicione fundos à sua conta com um valor informado, atualizando o saldo e registrando a operação no extrato.
- **Saque:** Realize saques respeitando limites diários e valores máximos. O sistema verifica saldo insuficiente e limites de saque.
- **Extrato:** Consulte um resumo detalhado de todas as operações realizadas, incluindo depósitos e saques, com data e hora.
- **Menu Interativo:** Interface de linha de comando para selecionar operações ou sair do sistema.

## 🛠️ Detalhes Técnicos

- **Formato de Data e Hora:** Transações são registradas no formato padrão brasileiro: `dd/mm/yy às HH:MM:SS`.
- **Formatação de Valores:** Valores monetários são apresentados com duas casas decimais e o símbolo `R$`.
- **Limites e Validações:**
  - **Saque Diário:** Máximo de 3 saques por dia.
  - **Limite de Saque:** Até R$ 500 por operação.
  - **Validações:** Valores de depósito e saque devem ser positivos e numéricos.

## 📥 Instruções de Uso

1. **Iniciar o Sistema:** Execute o script `sistema_bancario.py` para iniciar o sistema bancário.
2. **Escolher uma Operação:** Utilize o menu interativo para selecionar:
   - `d` para depósito
   - `s` para saque
   - `e` para extrato
   - `q` para sair
3. **Seguir as Instruções:** Insira os valores solicitados e siga as instruções fornecidas para realizar as operações desejadas.

## 📷 Exemplo de Uso

```plaintext
[d] depositar
[s] saque
[e] extrato 
[q] sair

=>  d

Deposito:

Informe o valor de depósito: 100
Depósito de R$100.00 realizado com sucesso!

