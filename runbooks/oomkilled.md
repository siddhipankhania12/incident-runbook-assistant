# Pod OOMKilled

## Likely causes
- Container memory limit set too low
- Memory leak in the application
- Traffic spike pushes memory above the limit

## Check
- kubectl get pods -n <namespace>
- kubectl describe pod <pod> -n <namespace> (look for Reason: OOMKilled, Exit Code: 137)
- kubectl top pod <pod> -n <namespace>

## Fix
- Raise resources.limits.memory in the deployment
- Set resources.requests.memory close to real usage
- Profile the app for leaks and roll back if a new release caused the spike
