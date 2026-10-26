# RDS Too Many Connections

## Likely causes
- App opens new database connections without a pool
- Connection leak in the code
- max_connections set too low for the instance size

## Check
- CloudWatch metric DatabaseConnections for the RDS instance
- SHOW PROCESSLIST; (MySQL) or SELECT count(*) FROM pg_stat_activity; (Postgres)
- kubectl logs <pod> -n <namespace> (look for "too many connections")

## Fix
- Add connection pooling in the app or use RDS Proxy
- Kill idle connections
- Raise max_connections in the parameter group or move to a larger instance
