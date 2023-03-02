
# pass in the contents of the registry

from azure.containerregistry import ContainerRegistryClient as Client_ccc_client
from azure.identity import DefaultAzureCredential as Default_ccc_id

#input local registry 

ccc_endpoint = "https://ociLocal.azurecr.io"
ccc_credential = DefaultAzureCredential()
ccc_client = ContainerRegistryClient(endpoint, credential)




list_repository_names = source.list.oci_list()



repositories = client.list_repository_names()
for repository in repositories:
    print(repository)


