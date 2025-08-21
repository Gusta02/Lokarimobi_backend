from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

# Configuração básica de logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Cria a aplicação
app = FastAPI(
    title="Lokar Backend Gateway",
    description="API Gateway central do Lokar Backend",
    version="1.0.0"
)

# Configuração do CORS (temporário: liberado para qualquer origem)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ⚠️ Em produção, restrinja a domínios confiáveis
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint de healthcheck
@app.get("/healthcheck", tags=["System"])
def healthcheck():
    logger.info("Healthcheck executado no gateway")
    return {"status": "ok", "service": "gateway"}
