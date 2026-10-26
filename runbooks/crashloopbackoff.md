# Pod in CrashLoopBackOff

## Likely causes
- Liveness probe fails because the app needs more startup time
- Wrong config value or missing environment variable
- Container killed for using too much memory

## Check
- kubectl get pods -n <namespace>
- kubectl describe pod <pod> -n <namespace>
- kubectl logs <pod> -n <namespace> --previous

## Fix
- Roll back first: kubectl rollout undo deployment/<name> -n <namespace>
- Add a startupProbe or raise initialDelaySeconds
- Fix the ConfigMap or Secret and restart the deployment
