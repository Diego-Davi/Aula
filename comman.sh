#!/bin/bash

# **************************************
#   Script para Executar Calculadora Python
#   Autor: [Seu Nome]
# **************************************

echo "=========================================="
echo "       Bem-vindo à Calculadora Python     "
echo "=========================================="
echo "Este script vai rodar sua calculadora em Python."

echo "Por favor, digite o seu nome:"
read nome_usuario

echo "Olá, $nome_usuario! Vamos começar a usar a calculadora!"

if [ -f "./calc.py" ]; then
    echo "Iniciando a calculadora Python..."

    python3 calc.py

    echo "=========================================="
    echo "       Obrigado por usar a calculadora, $nome_usuario!     "
    echo "=========================================="
else
    echo "Erro: O arquivo 'calculadora.py' não foi encontrado."
    echo "Por favor, verifique se o script Python está no mesmo diretório."
fi
