# TrataImagensPython
Tratando imagens para machine learning com Python e Pillow

## Funcionalidades atuais
- Conversão para tons de cinza
- Redução de tamanho
- Conversão para PDF

## Restaurando o ambiente de desenvolvimento
Após clonar o repositório, execute os comandos abaixo para restaurar o ambiente de desenvolvimento:
```
virtualenv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Instalando novas dependências
Utilize o PIP para instalar novas dependências e as inclua no arquivo requirements.txt com o comando abaixo (Powershell):
```
pip freeze | Out-File -Encoding ASCII requirements.txt
```