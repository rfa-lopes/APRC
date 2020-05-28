# Arquitectura e Protocolos de Redes de Computadores - 2020

## Trabalho Prático 2 - Passive Network Measurements and Analysis of NetFlow data

---

### Ferramentas e Tecnologias

* [Python3](https://www.python.org/download/releases/3.0/)
* [SQLite](https://www.sqlite.org/index.html)
* [IPGeolocation](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk)
* [Service-names](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)
* [Matplotlib](https://matplotlib.org)

---

### Como correr

* a1 - python3 [a1.py](a1.py)
* a2 - python3 [a2.py](a1.py)
* a3 - python3 [a3.py](a1.py)
* a4 - python3 [a4.py](a1.py)
* a5 - python3 [a5.py](a1.py)
* b1 - python3 [b1.py](a1.py)
* b2 - python3 [b2.py](a1.py)

---

### Ficheiros para base de dados SQLite ficheiro [aqui](database)
#### Correr Script 1 - Inserir ficheiros na base de dados
```cmd
python3 intoDB.py
```
#### Correr Script 2 - Abrir base de dados
```cmd
./StartSQLite.bat
```
#### Correr Script 3 - Ver número de tuplos em cada tabela
```sql
SELECT count(*) FROM fctTable;
SELECT count(*) FROM bigFlowsTable;
```

---

### Informação adicional

#### Autores

- Rodrigo Lopes - rfa.lopes@campus.fct.unl.pt - 50435
- João Machado - jpm.machado@campus.fct.unl.pt - 58722


#### Professor

- José Legatheaux Martins
- Paulo Afonso Lopes

#### Turnos práticos

- P1