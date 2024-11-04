# UnitConverter Application Monitoring with Prometheus and Grafana

## Overview

This project aims to integrate Prometheus and Grafana to monitor application metrics such as request per second, memory usage, and CPU usage. The setup will include:

1. Exporting metrics from the application.
2. Installing Prometheus and Grafana using Helm.
3. Configuring Prometheus to scrape metrics from the application.
4. Creating dashboards in Grafana to visualize the metrics.
5. Deploy the unitConverter Application in Minikube
Run the following commands to deploy your application:

# To deploy the deployment file
```bash
   kubectl apply -f Deployment.yaml
   
   # To deploy the service file
   kubectl apply -f service.yaml
```
6. Install Prometheus and Grafana
 Use Helm to install both applications in your Kubernetes cluster.

```bash
# Add the Helm repositories
 helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
 helm repo add grafana https://grafana.github.io/helm-charts
 helm repo update

# Install Prometheus
helm install prometheus prometheus-community/prometheus

# Install Grafana
 helm install grafana grafana/grafana
```
```bash
7. Configure Prometheus Scrape Configs
Customize the scrape configuration by editing the values.yaml of the Prometheus Helm release or overriding it during installation:

scrapeConfigs:
  - job_name: 'your_app'
    metrics_path: '/metrics'
    static_configs:
      - targets: ['<minikube ip>:<Nodeport>']
 ``` 
8. Access the Applications
   Access the applications with Minikube IP and their respective NodePorts:

   Prometheus UI: http://<minikube-ip>:<prometheus-nodeport>
   Grafana UI: http://<minikube-ip>:<grafana-nodeport>
   UnitConverter Application UI: http://<minikube-ip>:<your-nodeport>

9. Add Prometheus as a Data Source in Grafana UI
    
   Navigate to Configuration > Data Sources.

   Click Add data source and select Prometheus.

   Set the URL to http://prometheus-server.

11. Create Dashboards
    
    Go to Create > Dashboard. Add panels to visualize the metrics, such as:

    > Total HTTP Requests

    > Memory Usage

    > CPU Usage

# Snapshots:


![Screenshot from 2024-11-04 12-40-56](https://github.com/user-attachments/assets/d62c2a36-6b1e-43f9-b27d-9b321b1bbb32)

![Screenshot from 2024-11-04 12-40-36](https://github.com/user-attachments/assets/55121741-6fb7-4714-a556-f6c201df6047)

![Screenshot from 2024-11-04 12-44-33](https://github.com/user-attachments/assets/8a8c5fb6-262c-42e8-b0ce-e1a756bd34dd)

![Screenshot from 2024-11-04 12-44-09](https://github.com/user-attachments/assets/0ac84f27-0e4c-4187-876d-6ba61cac0e19)




