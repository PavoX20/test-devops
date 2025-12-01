# DevOps Technical Assessment

Este repositorio contiene la solución a un reto técnico de
DevOps. El proyecto consiste en el desarrollo, contenerización,
infraestructura y despliegue automatizado de un microservicio REST, siguiendo metodologías de **TDD (Test Driven Development)**.

## 🚀 LIVE DEMO (Despliegue en Google Cloud)

La aplicación se encuentra actualmente desplegada y operativa en un
clúster de **Google Kubernetes Engine (GKE)** con Balanceo de Carga usando 2 Nodos.


   🟢 **Online**        GCP         Kubernetes    `http://34.136.147.55/DevOps`

### ⚡ Prueba de Éxito (Happy Path)

Copie y pegue el siguiente comando para validar el endpoint con los
datos requeridos por el reto:

``` bash
curl -X POST http://34.136.147.55/DevOps -H "X-Parse-REST-API-Key: 2f5ae96c-b558-4c7b-a590-a501ae1c3f6c" -H "X-JWT-KWY: cualquier_token_valido" -H "Content-Type: application/json" -d '{
    "message": "This is a test",
    "to": "Juan Perez",
    "from": "Rita Asturia",
    "timeToLifeSec": 45
}'
```

### Respuesta Esperada:

``` json
{
    "message": "Hello Juan Perez your message will be send"
}
```

------------------------------------------------------------------------

## 🚫 Prueba de Error (Métodos no permitidos)

Cualquier petición HTTP que no sea POST (ej: GET, PUT, DELETE) retornará
el mensaje solicitado.

``` bash
# Intento con GET
curl -X GET http://34.136.147.55/DevOps -H "X-Parse-REST-API-Key: 2f5ae96c-b558-4c7b-a590-a501ae1c3f6c" -H "X-JWT-KWY: token"
```

### Respuesta Esperada:

``` json
"ERROR"
```

------------------------------------------------------------------------

## 🛠️ Stack Tecnológico

-   **Aplicación:** Python 3.9 + FastAPI
-   **Pruebas:** Pytest (TDD)
-   **Contenerización:** Docker 
-   **IaC:** Terraform 
-   **Orquestador:** Google Kubernetes Engine 
-   **CI/CD:** GitHub Actions
-   **Registry:** Docker Hub

------------------------------------------------------------------------

## 🔄 Pipeline CI/CD (Automatización)

Cada cambio en la rama **main** ejecuta automáticamente:

### **Stage: Build & Test**

-   Instala dependencias\
-   Ejecuta pytest (si falla, se detiene)

### **Stage: Build & Push**

-   Construye imagen Docker\
-   Publica en Docker Hub con etiqueta SHA

### **Stage: Deploy to GKE**

-   Autenticación en Google Cloud\
-   Rolling Update sin downtime


------------------------------------------------------------------------

## ☁️ Infraestructura (IaC)

El clúster fue aprovisionado utilizando Terraform en Google Cloud
Platform.\
**Ubicación del código:** `./terraform/main.tf`\
**Recursos:** GKE Cluster + Node Pool (2 Nodos Standard)
