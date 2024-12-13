## Prometheus metrics converter demo

The idea is to build a simple app that simulates a certain write load on a DB.
The app is integrated with Prometheus to collect metrics.
Those metrics will then be analyzed via a simple stat model and whenever an anomaly is found, a log with semantical meaning will be created (e.g. anomalous spike of write load for DB).

## To dos
0. Start from v3 - Fix prometheus metrics extractor for Flask (in master works)
1. Add real db connection issue when db_issu=true (by setting wrong password so that prometheus will track it OR make db crash for real)
2. Add logs (customize flask logs + db logs) and metrics to be saved periodically (every 5s) in a txt file
3. first client script that call API get_data with 10 requests/second per 3 minutes and then simulates x10 requests per 1 minute with overload=true
4. second client script that does the same and, after 3m, set db_issue=true
5. Generate data = log.txt, metrics.txt (plan b: simulate fake data using chatGPT), context for metrics and logs (via chatGPT) 
6. Bootstrap lightRAG with logs and metrics context

### How to run
Use docker compose to build and run the app.
At port 5000 there is the app UI to simulate certain DB loads.
At port 9000 there is the Prometheus dashboard.
At port 3000 there is Grafana.