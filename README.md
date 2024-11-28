## Prometheus metrics converter demo

The idea is to build a simple app that simulates a certain write load on a DB.
The app is integrated with Prometheus to collect metrics.
Those metrics will then be analyzed via a simple stat model and whenever an anomaly is found, a log with semantical meaning will be created (e.g. anomalous spike of write load for DB).

## To dos
1. Fix Prometheus mysqld-exporter, that it's still failing to collect metrics
2. Add the anomaly detection
3. Add the log converter

### How to run
Use docker compose to build and run the app.
At port 5000 there is the app UI to simulate certain DB loads.
At port 9000 there is the Prometheus dashboard.