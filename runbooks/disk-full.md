# Node or Volume Disk Full

## Likely causes
- Logs filling the disk with no rotation
- Old container images left on the node
- Persistent volume too small for the data

## Check
- kubectl describe node <node> (look for DiskPressure)
- kubectl get pvc -n <namespace>
- df -h on the node or inside the pod

## Fix
- Delete old logs and set up log rotation
- Prune unused images: crictl rmi --prune
- Expand the PVC or add a larger volume
