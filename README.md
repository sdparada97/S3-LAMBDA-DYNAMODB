# FortunaCookiesDemo

**FortunaCookiesDemo** es un proyecto demostrativo que muestra cómo integrar **Amazon S3**, **AWS Lambda** y **Amazon DynamoDB** utilizando una arquitectura serverless en AWS. Este demo genera "galletas de la fortuna" aleatorias, almacenadas en S3, procesadas por una función Lambda en **Python** y registradas en DynamoDB, asegurando un flujo sin costos dentro de la capa gratuita de AWS.

## Tecnologías Utilizadas
- **AWS S3**: Almacena los mensajes predefinidos de las galletas de la fortuna.
- **AWS Lambda**: Función sin servidor desarrollada en Python que selecciona y entrega una galleta de la fortuna al azar.
- **Amazon DynamoDB**: Base de datos NoSQL utilizada para llevar un registro de las galletas mostradas.
- **AWS SAM**: Marco de desarrollo para desplegar la infraestructura como código.

## Instalación y Configuración
1. **Clonar el repositorio**
   ```sh
   git clone <URL_DEL_REPOSITORIO>
   cd FortunaCookiesDemo
   ```
2. **Construir el proyecto con AWS SAM**
   ```sh
   sam build --template-file fortune-demo.yml
   ```
3. **Desplegar los recursos con AWS SAM**
   ```sh
   sam deploy --guided
   ```
4. **Subir los archivos de las galletas a S3**.
5. **Ejecutar la función Lambda para probar el flujo**.

## Uso
- Se puede invocar la función Lambda directamente desde la consola de AWS o mediante un API Gateway.
- Desde la consola de AWS Lambda, se puede enviar un evento de prueba para ejecutar la función y verificar su salida.
- También se puede invocar la función desde la línea de comandos con AWS CLI:
  ```sh
  aws lambda invoke --function-name FortuneDemo-FortuneLambda-rW0KaH8H3DXA response.json
  ```
- DynamoDB almacena registros de las galletas ya generadas para evitar repeticiones si es necesario.

## Contribución
Si deseas contribuir, puedes hacer un fork del repositorio y enviar un Pull Request con mejoras o correcciones.

## Licencia
Este proyecto está bajo la licencia MIT.

## Contacto
Si tienes dudas o sugerencias, siéntete libre de abrir un issue en GitHub o contactar al creador del proyecto.
