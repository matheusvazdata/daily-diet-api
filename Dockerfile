# Usa imagem do Python
FROM python:3.10

# Cria diretório dentro do container
WORKDIR /app

# Copia os arquivos do projeto para o container
COPY . .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta do Flask
EXPOSE 5000

# Comando padrão para iniciar
CMD ["python", "run.py"]