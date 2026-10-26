# Failed Deployment

## Likely causes
- Image pull error: wrong tag or missing registry access (ImagePullBackOff)
- New release fails readiness probe
- Rollout stuck because of missing resources or quota

## Check
- kubectl rollout status deployment/<name> -n <namespace>
- kubectl get events -n <namespace> --sort-by=.lastTimestamp
- kubectl describe pod <pod> -n <namespace>

## Fix
- Roll back: kubectl rollout undo deployment/<name> -n <namespace>
- Fix the image tag or registry secret and redeploy
- Fix the readiness probe or raise resource quota
