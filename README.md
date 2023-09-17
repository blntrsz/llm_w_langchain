# LLM with LangChain

1. Install dependencies

```bash
poetry install
```

2. Setup environment variables:

```bash
cp .env.example .env
```
... and add API keys

3. Run application

```bash
make run APP=<app-you-want-to-run>
# e.g. ice breaker app
make run APP=ice_breaker
```
