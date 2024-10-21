# Sistema Bancário
![Python](https://img.shields.io/badge/Python-3.8-blue.svg)

## 📜 Descrição

O **sistema_bancario.py** é um projeto em Python que simula um sistema bancário avançado. Esta versão permite realizar operações essenciais como depósitos, saques, consultas de extrato, e ainda inclui funcionalidades para cadastrar clientes e gerenciar contas. Desenvolvido para fins educacionais, o sistema conta com um menu interativo, verificações de segurança, limites para saques e transações, e um gerenciamento eficaz de clientes.

## 🚀 Funcionalidades

- **Depósito:** Adicione fundos à sua conta, atualizando o saldo e registrando a operação no extrato.
- **Saque:** Realize saques respeitando limites diários e valores máximos. O sistema verifica saldo insuficiente e limites de saque.
- **Extrato:** Consulte um resumo detalhado de todas as operações realizadas, incluindo depósitos e saques, com data e hora.
- **Cadastrar Cliente:** Cadastre novos clientes com informações como nome, CPF, data de nascimento e endereço, garantindo que não haja duplicatas.
- **Listar Contas:** Liste todas as contas cadastradas no sistema.
- **Menu Interativo:** Interface de linha de comando para selecionar operações ou sair do sistema.

## 🛠️ Detalhes Técnicos

- **Formato de Data e Hora:** Transações são registradas no formato padrão brasileiro: dd/mm/yy às HH:MM:SS.
- **Formatação de Valores:** Valores monetários são apresentados com duas casas decimais e o símbolo R$.
- **Limites e Validações:**
  - **Transações Diárias:** Máximo de 3 transações por dia.
  - **Limite de Saque:** Até R$ 500 por operação.
  - **Validações:** Valores de depósito e saque devem ser positivos e numéricos.
  - **Verificação de CPF:** Não permite o cadastro de clientes com CPF já existente.

## 📥 Instruções de Uso

1. **Iniciar o Sistema:** Execute o script `sistema_bancario.py` para iniciar o sistema bancário.
2. **Escolher uma Operação:** Utilize o menu interativo para selecionar:
   - `d` para depósito
   - `s` para saque
   - `e` para extrato
   - `cc` para cadastrar cliente
   - `nc` para nova conta
   - `lc` para listar contas
   - `q` para sair
3. **Seguir as Instruções:** Insira os valores solicitados e siga as instruções fornecidas para realizar as operações desejadas.

## 📷 Exemplo de Uso

```plaintext
======================== MENU ========================
[d]     Depositar
[s]     Saque
[e]     Extrato 
[cc]    Cadastrar cliente
[nc]    Nova conta
[lc]    Listar contas
[q]     Sair

=>  d

Informe o valor de depósito: 100
☰☰☰  Depósito de R$100.00 realizado com sucesso!  ☰☰☰

## Contribuições

Contribuições são bem-vindas! Se você gostaria de ajudar a melhorar este sistema bancário, siga estas etapas:

1. **Fork este repositório**: Clique no botão "Fork" no canto superior direito da página do projeto para criar uma cópia do repositório em sua conta.

2. **Crie uma branch**: Crie uma nova branch para sua contribuição. É recomendável usar um nome descritivo:
   ```bash
   git checkout -b nome-da-sua-branch


## ⚠️ Observações

    As operações são interativas e requerem entradas válidas.
    Mantenha o código e as bibliotecas atualizadas para garantir o melhor desempenho.


