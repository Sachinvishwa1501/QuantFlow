FROM python:3.13-slim AS runtime

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN addgroup --system quantflow && adduser --system --ingroup quantflow quantflow

COPY pyproject.toml README.md ./
COPY src ./src
COPY alembic.ini ./
COPY alembic ./alembic

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir .

USER quantflow

EXPOSE 8000

CMD ["uvicorn", "quantflow.api.main:create_app", "--factory", "--host", "0.0.0.0", "--port", "8000"]
