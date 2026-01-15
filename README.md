# Analisador de Frequência em Cifra de César

Projeto desenvolvido como atividade prática para estudo de **criptografia clássica** e **criptoanálise**, com foco na compreensão de como cifras simples funcionam e como podem ser quebradas utilizando **análise de frequência de letras**.

Este projeto consiste em uma aplicação em **Python** que realiza a **decifração automática da Cifra de César**, analisando a frequência das letras presentes em um texto cifrado e estimando o deslocamento mais provável com base nas letras mais comuns da língua utilizada.

## 🛠 Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat\&logo=python\&logoColor=white)
![Criptografia](https://img.shields.io/badge/Criptografia%20Cl%C3%A1ssica-000000?style=flat\&logo=letsencrypt\&logoColor=white)

## 📑 Sumário

* [Funcionalidades](#-funcionalidades)
* [Funcionamento](#-funcionamento)
* [Limitações](#-limitações)
* [Aprendizados](#-aprendizados)

## ⚙️ Funcionalidades

* Leitura de texto cifrado a partir de arquivo (`text.txt`)
* Normalização do texto:
  * Conversão para letras minúsculas
  * Remoção de acentos
  * Desconsideração de caracteres não alfabéticos para análise
* Análise de frequência das letras mais comuns no texto cifrado
* Estimativa automática do deslocamento da **Cifra de César**
* Decifração do texto preservando caracteres não alfabéticos
* Opção de saída:
  * Exibição do texto decifrado no terminal
  * Geração de arquivo `deciphered_text.txt`
* Medição do tempo de execução do processo

## 🔁 Funcionamento

O programa realiza uma **análise de frequência** identificando as letras mais recorrentes no texto cifrado e as compara com letras estatisticamente mais comuns da língua inglesa (como **E**, **T** e **O**).
Com base nessa comparação, o sistema estima o deslocamento mais provável utilizado na cifra e aplica o deslocamento inverso para decifrar o texto original.

Essa abordagem caracteriza uma forma básica de **criptoanálise**, indo além da simples aplicação manual da cifra.

## ⚠️ Limitações

Este projeto possui limitações inerentes à técnica utilizada e ao tipo de cifra analisada:

* Textos muito curtos podem não conter amostras suficientes para uma análise de frequência confiável
* Mesmo em textos longos, existe a possibilidade de as letras mais frequentes não coincidirem com as letras mais comuns da língua
* O método assume uma língua específica, o que pode gerar resultados incorretos caso o texto esteja em outro idioma
* A Cifra de César é uma cifra extremamente simples e **insegura**, não sendo adequada para qualquer uso real em segurança da informação

Apesar dessas limitações, a análise de frequência **funciona corretamente na maioria dos casos**, especialmente em textos maiores, demonstrando como cifras clássicas podem ser quebradas com técnicas estatísticas simples.

## 🧠 Aprendizados

* Fundamentos de criptografia clássica
* Funcionamento da Cifra de César
* Introdução à criptoanálise por análise de frequência
* Processamento e normalização de texto em Python
* Manipulação de arquivos e entrada/saída de dados
* Importância da estatística na quebra de cifras
* Compreensão prática de por que cifras simples não são seguras

