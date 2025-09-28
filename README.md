# 😁 Números Felizes em Python

> Descubra se um número é **feliz** ou não, e encontre todos os números
> felizes dentro de um intervalo definido!

------------------------------------------------------------------------

## 📂 Estrutura do Projeto

    .
    ├── numero_feliz.py        # Função principal para verificar se um número é feliz
    ├── numeros_felizes.py     # Script para listar números felizes em um intervalo
    ├── test_numero_feliz.py   # Testes unitários com pytest
    ├── requirements.txt       # Dependências do projeto
    ├── .gitignore             # Pastas e arquivos ignorados pelo Git

------------------------------------------------------------------------

## ✨ O que é um Número Feliz?

Um **número feliz** é definido pelo seguinte processo:
1. Pegue o número e substitua-o pela soma dos **quadrados de seus
dígitos**.
2. Repita o processo até que o número seja **1** (feliz ✅) ou entre em
um **ciclo infinito** (não feliz ❌)

🔹 Exemplo:

    19 → 1² + 9² = 82  
    82 → 8² + 2² = 68  
    68 → 6² + 8² = 100  
    100 → 1² + 0² + 0² = 1 ✅

➡️ Portanto, **19 é um número feliz**.

------------------------------------------------------------------------

## ⚙️ Instalação

Clone o repositório e instale as dependências:

``` bash
git clone https://github.com/thallesborges/Numero-Feliz.git
cd Numero-Feliz
pip install -r requirements.txt
```

------------------------------------------------------------------------

## ▶️ Como Usar

### 🔹 Verificar se um número é feliz:

``` bash
python numero_feliz.py
```

➡️ O programa pedirá um número e informará se ele é feliz ou não.

### 🔹 Descobrir números felizes em um intervalo:

``` bash
python numeros_felizes.py
```

➡️ Insira os valores **X** e **Y**, e o programa listará todos os
números felizes nesse intervalo.

------------------------------------------------------------------------

## 🧪 Testes

Os testes utilizam **pytest**. Para rodá-los:

``` bash
pytest -v
```

📌 Exemplos de casos testados:
- ✅ Felizes: `1, 7, 10, 13, 19`
- ❌ Não felizes: `2, 3, 4, 5, 6`

------------------------------------------------------------------------

## 📦 Dependências

As principais dependências estão no `requirements.txt`:
- `pytest` → Para testes unitários
- `colorama`, `Pygments` → Saídas coloridas e realce
- `iniconfig`, `packaging`, `pluggy` → Dependências internas do pytest

------------------------------------------------------------------------

Desenvolvido por Thalles Borges.
Sinta-se livre para usar e modificar o código!
