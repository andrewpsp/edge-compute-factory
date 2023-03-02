# edge-compute-factory


# iOT callcenter products 

# Access Edge Compute Factory  

## Playground try it out now.


## Complete Onboarding Assessments B2B Operations


https://swagger-api.github.io/apidom/
Data Stack 
``` 
LABEL vendor=BOdataFactory \
      BusinessObject.Project=BODF-1.0 \
      BusinessOBject.client="BODF" \  
      BusinessOBject.version="0.0.1" \
      BusinessOBj-API.release-date="2023-27-2"

``` 


Network 



Onboarding documentation: 
![alt text][dashboard]

[dashboard]: https://github.com/andrewpsp/edge-compute-factory/blob/main/images/ccc-tool-dashboard.png "ccc-tool download and ccc dashboard"




## Access Base Oci registry  
```
#!/bin/bash
# This script requires Azure CLI version 2.25.0 or later. Check version with `az --version`.

# Modify for your environment.
# ACR_NAME: The name of your Azure Container Registry
# SERVICE_PRINCIPAL_NAME: Must be unique within your AD tenant
ACR_NAME=$containerRegistry
SERVICE_PRINCIPAL_NAME=$servicePrincipal

# Obtain the full registry ID
ACR_REGISTRY_ID=$(az acr show --name $ACR_NAME --query "id" --output tsv)
# echo $registryId

# Create the service principal with rights scoped to the registry.
# Default permissions are for docker pull access. Modify the '--role'
# argument value as desired:
# acrpull:     pull only
# acrpush:     push and pull
# owner:       push, pull, and assign roles
PASSWORD=$(az ad sp create-for-rbac --name $SERVICE_PRINCIPAL_NAME --scopes $ACR_REGISTRY_ID --role acrpull --query "password" --output tsv)
USER_NAME=$(az ad sp list --display-name $SERVICE_PRINCIPAL_NAME --query "[].appId" --output tsv)

# Output the service principal's credentials; use these in your services and
# applications to authenticate to the container registry.
echo "Service principal ID: $USER_NAME"
echo "Service principal password: $PASSWORD"
```

