# Api simulando o instagram


### Tecnologias utilizadas 

<ul>
    <li>Python</li>
    <li>SQLAlchemy</li>
    <li>Pydantic</li>
    <li>FastAPI</li>
    <li>AIOFiles</li>
    <li>Passlib</li>
    <li>Uvicorn</li>
    <li>Python multi-part</li>
    <li>Bcrypt</li>
</ul>

Para instalar as dependencias entre na pasta do projeto e digite no terminal do vscode :
```
python -m venv venv
```

```
.\venv\Scripts\activate
```

```
pip install -r requirements.txt
```

Para rodar o projeto utilize o comando:

```
uvicorn main:app --host 127.0.0.1 --port 8080
```

Para acessar o swagger digite no navegador:
```
http://127.0.0.1:8080/docs
```