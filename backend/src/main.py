from fastapi import FastAPI

app = FastAPI(
    title='Lottery project',
    description='Lottery project API',
    version='1.0.0',
)


@app.get('/health-check')
async def health_check():
    return {'status': 'OK'}
