# Flask Calc API (Bootstrap)

Projeto simples em Flask que chama uma API para calcular expressões aritméticas.

## Requisitos
- Python 3.10+ (recomendado)

## Clonar
```bash
git clone <URL_DO_REPOSITORIO>
cd <PASTA_DO_REPOSITORIO>
```

## Criar venv e instalar dependências

### Unix

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Rodar

```bash
python app.py
```
**ou**

```bash
flask run
```

**Abra no navegador:**

* [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Testar a API via curl

```bash
curl -X POST http://127.0.0.1:5000/api/calc \
  -H "Content-Type: application/json" \
  -d '{"expr":"(2+3)*4"}'
```

**Resposta esperada:**

```json
{"result":20}
```

