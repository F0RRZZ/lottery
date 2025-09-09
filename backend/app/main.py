from fastapi import FastAPI

app = FastAPI(
    title='Lottery project',
    description='Lottery project API',
    version='1.0.0',
)


@app.get('/index')
async def index():
    return {'status': 'OK'}
