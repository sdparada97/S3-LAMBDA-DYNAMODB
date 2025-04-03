import json
import boto3
import os
import random
import uuid

# Inicializar clientes de AWS
dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')

# Variables de entorno
TABLE_NAME = os.getenv('FORTUNECOOKIES_TABLE_NAME')
BUCKET_NAME = os.getenv('FORTUNECOOKIES_BUCKET_NAME')

def lambda_handler(event, context):
    table = dynamodb.Table(TABLE_NAME)
    
    # Obtener todas las frases desde DynamoDB
    response = table.scan()
    items = response.get('Items', [])
    
    if not items:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "No hay frases en la base de datos"})
        }

    # Seleccionar una frase aleatoria
    fortune = random.choice(items)['text']

    # Crear un archivo JSON con la frase
    file_name = f"fortune-{uuid.uuid4()}.json"
    file_content = json.dumps({"fortune": fortune})

    # Guardar el archivo en S3
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=file_name,
        Body=file_content,
        ContentType='application/json'
    )

    # URL pública del archivo
    file_url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{file_name}"

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Aquí está tu fortuna", "url": file_url})
    }