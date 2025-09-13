from fastapi import FastAPI

from src.auth.router import router as auth_router

app = FastAPI(
    title='Lottery project',
    description='Lottery project API',
    version='1.0.0',
)
app.include_router(auth_router)


@app.get('/health-check')
async def health_check():
    return {'status': 'OK'}
