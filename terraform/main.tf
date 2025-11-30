# 1. Definimos que usaremos Google Cloud
terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.51.0"
    }
  }
}

# 2. Configuración del Proyecto
provider "google" {
  # IMPORTANTE: Cambia esto por TU ID de proyecto que sale en la imagen que subiste
  project     = "refined-algebra-479620-s4" 
  region      = "us-central1"
  zone        = "us-central1-a"
  credentials = file("../credentials.json") # Le decimos dónde está la llave
}

# 3. Creación del Clúster de Kubernetes (GKE)
resource "google_container_cluster" "primary" {
  name     = "cluster-banco-devops"
  location = "us-central1-a"

  # Eliminamos el pool por defecto para crear uno personalizado
  remove_default_node_pool = true
  initial_node_count       = 1
}

# 4. Creación de los Nodos (Las máquinas virtuales)
# REQUISITO PDF: "minimum of two nodes"
resource "google_container_node_pool" "primary_preemptible_nodes" {
  name       = "pool-nodos-banco"
  location   = "us-central1-a"
  cluster    = google_container_cluster.primary.name
  node_count = 2  # <--- AQUÍ CUMPLIMOS EL REQUISITO

  node_config {
    preemptible  = true # Usamos máquinas "volátiles" (más baratas para pruebas)
    machine_type = "e2-medium" # 2 vCPU, 4GB RAM (Suficiente para el examen)
    
    # Permisos mínimos para que los nodos funcionen
    oauth_scopes = [
      "https://www.googleapis.com/auth/cloud-platform"
    ]
  }
}