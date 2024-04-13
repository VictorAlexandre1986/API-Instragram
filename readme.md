# Api simulando o instagram


### Tecnologias utilizadas 

<ul>
    <li>Python</li>
    <li>SQLAlchemy</li>
    <li>Marshmallow</li>
    <li>FastAPI</li>
</ul>

Para instalar as dependencias entre na pasta do projeto e digite no terminal do vscode :
```
python -m venv venv
```
````
.\venv\Scripts\activate
```
```
pip install -r requirements.txt
```

Para rodar o projeto utilize o comando:

```
uvicorn main>app --host 127.0.0.1 --port 8080
```

Para acessar o swagger no digite no navegador:
```
http://127.0.0.1:8080/docs
```