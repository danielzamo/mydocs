---
title: 'Lab 07: Manage Azure storage'
author: "Daniel Oscar Zamo"
date: "2025-06-20"
type: "laboratory"
module: 'Administer Azure Storage'
---


# Lab 07 - Manage Azure Storage

## Lab introduction

In this lab you learn to create storage accounts for Azure blobs and Azure files. You learn to configure and secure blob containers. You also learn to use Storage Browser to configure and secure Azure file shares.

This lab requires an Azure subscription. Your subscription type may affect the availability of features in this lab. You may change the region, but the steps are written using **East US**.

## Estimated timing: 50 minutes

## Lab scenario

Your organization is currently storing data in on-premises data stores. Most of these files are not accessed frequently. You would like to minimize the cost of storage by placing infrequently accessed files in lower-priced storage tiers. You also plan to explore different protection mechanisms that Azure Storage offers, including network access, authentication, authorization, and replication. Finally, you want to determine to what extent Azure Files is suitable for hosting your on-premises file shares.

<!--
## Interactive lab simulations

>**Note**: The lab simulations that were previously provided have been retired.

-->

_In Github Page:_

- [Job with Azure Cloud Shell - Bash](https://danielzamo.github.io/mydocs/azure/laboratories/lab07-cli/)
- [Job with Azure Portal](https://danielzamo.github.io/mydocs/azure/laboratories/lab07/)

## Architecture diagram

![Diagram of the tasks.](images/az104-lab07-architecture.png)

## Job skills

- Task 1: Create and configure a storage account.
- Task 2: Create and configure secure blob storage.
- Task 3: Create and configure secure Azure file storage.

## Task 1: Create and configure a storage account.

In this task, you will create and configure a storage account. The storage account will use geo-redundant storage and will not have public access.

### Method 1: Azure Portal

![Azure Portal Login](../images/azure-portal-login.png)

1. Sign in to the **Azure portal** - `https://portal.azure.com`.

2. Search for and select `Storage accounts`, and then click **+ Create**.

    ![Storage Account Creation](./images/storage-account-create.png)

3. On the **Basics** tab of the **Create a storage account** blade, specify the following settings (leave others with their default values):

    | Setting                                                        | Value                                                                                                           |
    | -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
    | Subscription                                                   | the name of your Azure subscription                                                                             |
    | Resource group                                                 | `az104-rg7` (create new)                                                                                        |
    | Storage account name                                           | `az104rg7dzstorageaccount` any globally unique name between 3 and 24 in length consisting of letters and digits |
    | Region                                                         | `(Europe) West Europe`                                                                                          |
    | Performance                                                    | `Standard` (notice the Premium option)                                                                          |
    | Redundancy                                                     | `Geo-redundant storage` (notice the other options)                                                              |
    | Make read access to data in the event of regional availability | Check the box                                                                                                   |

    >**Did you know?** You should use the Standard performance tier for most applications. Use the Premium performance tier for enterprise or high-performance applications.

    ![Storage Account Basics Tab](./images/storage-account-basics.png)

4. On the **Advanced** tab, use the informational icons to learn more about the choices. Take the defaults.

    ![Storage Account Advanced Tab](./images/storage-account-advanced.png)

5. On the **Networking** tab, in the **Network access** section, select `Disable public access and use private access`. This will restrict inbound access while allowing outbound access.

    ![Storage Account Networking Tab](./images/storage-account-networking.png)

6. Review the **Data protection** tab. Notice 7 days is the default soft delete retention policy. Note you can enable versioning for blobs. Accept the defaults.

    ![Storage Account Data Protection](./images/storage-account-data-protection.png)

7. Review the **Encryption** tab. Notice the additional security options. Accept the defaults.

    ![Storage Account Encryption](./images/storage-account-encryption.png)

8. Select **Review + Create**, wait for the validation process to complete, and then click **Create**.

9. Once the storage account is deployed, select **Go to resource**.

10. Review the **Overview** blade and the additional configurations that can be changed. These are global settings for the storage account. Notice the storage account can be used for Blob containers, File shares, Queues, and Tables.

    ![Storage Account Overview](./images/storage-account-overview.png)

11. In the **Security + networking** blade, select **Networking**. Notice **Public network access** is disabled.

    - Change the **Public network access** to **Enable from selected networks and IP addresses**.
    - In the **Firewall** section, select the checkbox to **Add your client IP address**.
    - Save your changes.

    ![Storage Account Networking Settings](./images/storage-account-networking-settings.png)

12. In the **Data management** blade, select **Redundancy**. Notice the information about your primary and secondary data center locations.

    ![Storage Account Redundancy](./images/storage-account-redundancy.png)

13. In the **Data management** blade, select **Lifecycle management**, and then select **Add a rule**.

    - **Name** the rule `Movetocool`. Notice your options for limiting the scope of the rule. Click **Next**.
    - On the **Base blobs** tab, *if* based blobs were last modified more than `30 days` ago *then* **Move to cool storage**. Notice your other choices.
    - Notice you can configure other conditions. Select **Add** when you are done exploring.

    ![Screenshot move to cool rule conditions.](./images/az104-lab07-movetocool.png)

### Method 2: Azure Cloud Shell (Bash)

![Azure Cloud Shell](./images/azure-cloud-shell.png)

1. Open Azure Cloud Shell and select **Bash**.

    ![Cloud Shell Bash Selection](./images/cloud-shell-bash.png)

2. Create the resource group:

    ```bash
    # Set variables
    RESOURCE_GROUP="az104-rg"
    LOCATION="eastus"
    STORAGE_ACCOUNT_NAME="storageaccount$(date +%s)"

    # Create resource group
    az group create --name $RESOURCE_GROUP --location $LOCATION
    ```

    ![Resource Group Creation](./images/resource-group-creation.png)

3. Create the storage account with geo-redundant storage:

    ```bash
    # Create storage account
    az storage account create \
      --name $STORAGE_ACCOUNT_NAME \
      --resource-group $RESOURCE_GROUP \
      --location $LOCATION \
      --sku Standard_GRS \
      --kind StorageV2 \
      --access-tier Hot \
      --allow-blob-public-access false \
      --public-network-access Disabled
    ```

    ![Storage Account Creation CLI](./images/storage-account-creation-cli.png)

4. Enable read access for geo-redundant storage:

    ```bash
    # Update storage account to enable read access geo-redundant storage
    az storage account update \
      --name $STORAGE_ACCOUNT_NAME \
      --resource-group $RESOURCE_GROUP \
      --sku Standard_RAGRS
    ```

5. Configure networking to allow access from selected networks:

    ```bash
    # Get your public IP
    MY_IP=$(curl -s https://ipinfo.io/ip)

    # Update network access
    az storage account update \
      --name $STORAGE_ACCOUNT_NAME \
      --resource-group $RESOURCE_GROUP \
      --public-network-access Enabled \
      --default-action Deny

    # Add your IP to firewall rules
    az storage account network-rule add \
      --resource-group $RESOURCE_GROUP \
      --account-name $STORAGE_ACCOUNT_NAME \
      --ip-address $MY_IP
    ```

    ![Network Configuration CLI](./images/network-configuration-cli.png)

6. Create lifecycle management policy:

    ```bash
    # Create lifecycle policy JSON
    cat > lifecycle-policy.json << EOF
    {
      "rules": [
        {
          "name": "Movetocool",
          "enabled": true,
          "type": "Lifecycle",
          "definition": {
            "filters": {
              "blobTypes": ["blockBlob"]
            },
            "actions": {
              "baseBlob": {
                "tierToCool": {
                  "daysAfterModificationGreaterThan": 30
                }
              }
            }
          }
        }
      ]
    }
    EOF

    # Apply lifecycle policy
    az storage account management-policy create \
      --account-name $STORAGE_ACCOUNT_NAME \
      --resource-group $RESOURCE_GROUP \
      --policy @lifecycle-policy.json
    ```

    ![Lifecycle Policy CLI](./images/lifecycle-policy-cli.png)

_List, review, and delete the entire Resource Group and/or Storage Account_

![Delete the Resource Group (and all its resources)](./images/remove-resource-group-cli.png)

## Task 2: Create and configure secure blob storage

In this task, you will create a blob container and upload an image. Blob containers are directory-like structures that store unstructured data.

### Method 1: Azure Portal

### Create a blob container and a time-based retention policy

1. Continue in the Azure portal, working with your storage account.

2. In the **Data storage** blade, select **Containers**.

    ![Storage Containers](./images/storage-containers.png)

3. Click **+ Add container** and **Create** a container with the following settings:

    | Setting             | Value                                     |
    | ------------------- | ----------------------------------------- |
    | Name                | `data`                                    |
    | Public access level | Notice the access level is set to private |

    ![Screenshot of create a container.](./images/az104-lab07-create-container.png)

    ![Container Creation](./images/container-creation.png)

4. On your container, scroll to the ellipsis (...) on the far right, select **Access Policy**.

    ![Container Access Policy](./images/container-access-policy.png)

5. In the **Immutable blob storage** area, select **Add policy**.

    | Setting                  | Value                  |
    | ------------------------ | ---------------------- |
    | Policy type              | `Time-based retention` |
    | Set retention period for | `180` days             |

6. Select **Save**.

    ![Retention Policy](./images/retention-policy.png)

### Manage blob uploads

1. Return to the containers page, select your **data** container and then click **Upload**.

    ![Blob Upload](./images/blob-upload.png)

2. On the **Upload blob** blade, expand the **Advanced** section.

    >**Note**: Locate a file to upload. This can be any type of file, but a small file is best. A sample file can be downloaded from the AllFiles directory.

    | Setting          | Value                                    |
    | ---------------- | ---------------------------------------- |
    | Browse for files | add the file you have selected to upload |
    | Select           | **Advanced**                             |
    | Blob type        | `Block blob`                             |
    | Block size       | `4 MiB`                                  |
    | Access tier      | `Hot`  (notice the other options)        |
    | Upload to folder | `securitytest`                           |
    | Encryption scope | Use existing default container scope     |

    ![Upload Advanced Settings](./images/upload-advanced-settings.png)

3. Click **Upload**.

4. Confirm you have a new folder, and your file was uploaded.

    ![Upload Confirmation](./images/upload-confirmation.png)

5. Select your upload file and review the options including **Download**, **Delete**, **Change tier**, and **Acquire lease**.

    ![Blob Management Options](./images/blob-management-options.png)

6. Copy the file **URL** (Properties blade) and paste into a new **Inprivate** browsing window.

7. You should be presented with an XML-formatted message stating **ResourceNotFound** or **PublicAccessNotPermitted**.

    > **Note**: This is expected, since the container you created has the public access level set to **Private (no anonymous access)**.

    ![Access Denied](./images/access-denied.png)

### Configure limited access to the blob storage

1. Browse back to the file that you uploaded and select the ellipsis (…) to the far right, then select **Generate SAS** and specify the following settings (leave others with their default values):

    | Setting              | Value                                |
    | -------------------- | ------------------------------------ |
    | Signing key          | **Key 1**                            |
    | Permissions          | **Read** (notice your other choices) |
    | Start date           | yesterday's date                     |
    | Start time           | current time                         |
    | Expiry date          | tomorrow's date                      |
    | Expiry time          | current time                         |
    | Allowed IP addresses | leave blank                          |

    ![SAS Token Generation](./images/sas-token-generation.png)

2. Click **Generate SAS token and URL**.

3. Copy the **Blob SAS URL** entry to the clipboard.

4. Open another InPrivate browser window and navigate to the Blob SAS URL you copied in the previous step.

    >**Note**: You should be able to view the content of the file.

    ![SAS Access Success](./images/sas-access-success.png)

    ![Generate token SAS and check access](./images/generate-token-sas-to-blob.png)

### Method 2: Azure Cloud Shell (Bash)

1. Create a blob container:

    ```bash
    # Set variables value
    RESOURCE_GROUP='az104-rg'; STORAGE_ACCOUNT_NAME='storageaccount1750491953'

    # Get storage account key
    STORAGE_KEY=$(az storage account keys list \
      --resource-group $RESOURCE_GROUP \
      --account-name $STORAGE_ACCOUNT_NAME \
      --query '[0].value' -o tsv)
    # Initial attempt to create container (may fail due to network rules)
    az storage container create \
      --name data \
      --account-name $STORAGE_ACCOUNT_NAME \
      --account-key $STORAGE_KEY \
      --public-access off
    ```

    >**Note**: If you encounter the error *"The request may be blocked by network rules of storage account"*, follow these additional steps:

    ```bash
    # Check current network rule configuration
    az storage account show -n $STORAGE_ACCOUNT_NAME --resource-group $RESOURCE_GROUP --query networkRuleSet

    # Get your current public IP
    MY_IP=$(curl -s https://ipinfo.io/ip)

    # Add your IP to the firewall rules
    az storage account network-rule add \
      --resource-group $RESOURCE_GROUP \
      --account-name $STORAGE_ACCOUNT_NAME \
      --ip-address $MY_IP

    # Update default action to Allow (temporarily for lab completion)
    az storage account update \
      --name $STORAGE_ACCOUNT_NAME \
      --resource-group $RESOURCE_GROUP \
      --default-action Allow
    # Verify network rules are updated
    echo "Mi IP es: $MY_IP"
    az storage account network-rule list \
      --resource-group $RESOURCE_GROUP \
      --account-name $STORAGE_ACCOUNT_NAME

    # Now retry creating the container
    az storage container create \
      --name data \
      --account-name $STORAGE_ACCOUNT_NAME \
      --account-key $STORAGE_KEY \
      --public-access off
    ```

    ![Container Creation CLI](./images/container-creation-cli.png)

2. Verify container creation:

    ```bash
    # List containers to confirm creation
    az storage container list \
      --account-name $STORAGE_ACCOUNT_NAME \
      --account-key $STORAGE_KEY \
      --output table
    ```

3. Set immutable blob storage policy:

    ```bash
    # Set time-based retention policy (30 days)
    az storage container immutability-policy create \
      --account-name $STORAGE_ACCOUNT_NAME \
      --container-name data \
      --period 30
    ```

<!--
**Alternative option - Legal hold policy:**

```bash
# Alternative: Set legal hold policy (uses Azure AD authentication)
az storage container legal-hold set \
    --account-name $STORAGE_ACCOUNT_NAME \
    --container-name data \
    --tags retention-policy lab-exercise
```

-->

4. Upload a file to blob storage:

    ```bash
    # Create a sample file
    echo "Hola mundo!" > testfile2.txt

    # Upload file to specific folder
    az storage blob upload \
      --account-name $STORAGE_ACCOUNT_NAME \
      --account-key $STORAGE_KEY \
      --container-name data \
      --name securitytest/testfile2.txt \
      --file testfile2.txt \
      --tier Hot
    ```

    ![File Upload CLI](./images/file-upload-cli.png)

5. Generate SAS token for secure access:

    ```bash
    # Generate SAS token for the blob
    SAS_TOKEN=$(az storage blob generate-sas \
      --account-name $STORAGE_ACCOUNT_NAME \
      --account-key $STORAGE_KEY \
      --container-name data \
      --name securitytest/testfile2.txt \
      --permissions r \
      --expiry $(date -d '+1 day' '+%Y-%m-%d') \
      --output tsv)

    # Create full URL with SAS token
    BLOB_URL="https://${STORAGE_ACCOUNT_NAME}.blob.core.windows.net/data/securitytest/testfile2.txt?${SAS_TOKEN}"

    echo "Blob URL with SAS token: $BLOB_URL"
    ```

6. Test secure access:

    ```bash
    # Test access with SAS URL (this will show the file content)
    curl "$BLOB_URL"
    ```

    ![Test secure access from CLI curl](images/test-secure-access-cli-curl.png)

- Optional - Restore network restrictions after lab completion:

    ```bash
    # Restore more restrictive network access (optional)
    az storage account update \
      --name $STORAGE_ACCOUNT_NAME \
      --resource-group $RESOURCE_GROUP \
      --default-action Deny

    # Remove your IP from firewall if desired
    az storage account network-rule remove \
      --resource-group $RESOURCE_GROUP \
      --account-name $STORAGE_ACCOUNT_NAME \
      --ip-address $MY_IP
    ```

## Task 3: Create and configure an Azure File storage

In this task, you will create and configure Azure File shares. You will use Storage Browser to manage the file share.

### Method 1: Azure Portal

### Create the file share and upload a file

1. In the Azure portal, navigate back to your storage account, in the **Data storage** blade, click **File shares**.

    ![File Shares Navigation](./images/file-shares-navigation.png)

2. Click **+ File share** and on the **Basics** tab give the file share a name, `share1`.

3. Notice the **Access tier** options. Keep the default **Transaction optimized**.

    ![File Share Creation](./images/file-share-creation.png)

4. Move to the **Backup** tab and ensure **Enable backup** is **not** checked. We are disabling backup to simplify the lab configuration.

    ![File Share Creation - backup tab](./images/file-share-creation-backup-tab.png)

5. Click **Review + create**, and then **Create**. Wait for the file share to deploy.

    ![Screenshot of the create file share page.](../../media/az104-lab07-create-share.png)

### Explore Storage Browser and upload a file

1. Return to your storage account and select **Storage browser**. The Azure Storage Browser is a portal tool that lets you quickly view all the storage services under your account.

    ![Storage Browser](./images/storage-browser.png)

2. Select **File shares** and verify your **share1** directory is present.

    ![File Shares Browser](./images/file-shares-browser.png)

3. Select your **share1** directory and notice you can **+ Add directory**. This lets you create a folder structure.

    ![Add Directory](./images/add-directory.png)

4. Select **Upload**. Browse to a file of your choice, and then click **Upload**.

    >**Note**: You can view file shares and manage those shares in the Storage Browser. There are currently no restrictions.

    ![File Upload](./images/file-upload.png)

### Method 2: Azure Cloud Shell (Bash)

1. Create Azure File Share:

    ```bash
    # Create file share
    az storage share create \
      --name share1-cli \
      --account-name $STORAGE_ACCOUNT_NAME \
      --account-key $STORAGE_KEY \
      --quota 1024
    ```

    ![File Share Creation CLI](./images/file-share-creation-cli.png)

2. Create a directory in the file share:

    ```bash
    # Create directory
    az storage directory create \
      --name testdir-cli \
      --share-name share1-cli \
      --account-name $STORAGE_ACCOUNT_NAME \
      --account-key $STORAGE_KEY
    ```

3. Upload a file to the file share:

    ```bash
    # Create another test file
    echo "This is a test file for Azure File Share - hello world!" > fileshare-test-cli.txt

    # Upload file to file share
    az storage file upload \
      --share-name share1-cli \
      --source fileshare-test-cli.txt \
      --path testdir-cli/fileshare-test-cli.txt \
      --account-name $STORAGE_ACCOUNT_NAME \
      --account-key $STORAGE_KEY
    ```

    ![File Share Upload CLI](./images/file-share-upload-cli.png)

4. List files in the file share:

    ```bash
    # List files in directory
    az storage file list \
      --share-name share1-cli \
      --path testdir-cli \
      --account-name $STORAGE_ACCOUNT_NAME \
      --account-key $STORAGE_KEY \
      --output table
    ```

    ![List files in directory](./images/list-files-directory.png)

### Restrict network access to the storage account

1. In the portal, search for and select **Virtual networks**.

    ![Virtual Networks Search](./images/virtual-networks-search.png)

2. Select **+ Create**. Select your resource group. and give the virtual network a **name**, `vnet1`.

    ![Virtual Network Creation](./images/virtual-network-creation.png)

3. Take the defaults for other parameters, select **Review + create**, and then **Create**.

4. Wait for the virtual network to deploy, and then select **Go to resource**.

5. In the **Settings** section, select the **Service endpoints** blade.

    - Select **Add**.
    - In the **Services** drop-down select **Microsoft.Storage**.
    - In the **Subnets** drop-down check the **Default** subnet.
    - Click **Add** to save your changes.

    ![Service Endpoints](./images/service-endpoints.png)

6. Return to your storage account.

7. In the **Security + networking** blade, select **Networking**.

8. Select **Add existing virtual network** and select **vnet1** and **default** subnet, select **Add**.

    ![Add Virtual Network](./images/add-virtual-network.png)

9. In the **Firewall** section, **Delete** your machine IP address. Allowed traffic should only come from the virtual network.

10. Be sure to **Save** your changes.

    >**Note:** The storage account should now only be accessed from the virtual network you just created.

    ![Network Restrictions](./images/network-restrictions.png)

11. Select the **Storage browser** and **Refresh** the page. Navigate to your file share or blob content.

    >**Note:** You should receive a message *not authorized to perform this operation*. You are not connecting from the virtual network. It may take a couple of minutes for this to take effect.

    <!--    ![Screenshot unauthorized access.](../../media/az104-lab07-notauthorized.png) -->

    ![Storage browser](images/storage-browser-refresh.png)

### Method 2: Azure Cloud Shell (Bash) - Network Configuration

1. Create virtual network:

    ```bash
    # Create virtual network
    az network vnet create \
      --resource-group $RESOURCE_GROUP \
      --name vnet1 \
      --address-prefix 10.0.0.0/16 \
      --subnet-name default \
      --subnet-prefix 10.0.0.0/24 \
      --location $LOCATION
    ```

    ![Virtual Network CLI](./images/virtual-network-cli.png)

2. Create service endpoint:

    ```bash
    # Add service endpoint to subnet
    az network vnet subnet update \
      --resource-group $RESOURCE_GROUP \
      --vnet-name vnet1 \
      --name default \
      --service-endpoints Microsoft.Storage
    ```

3. Configure storage account network rules:

    ```bash
    # Remove current IP from firewall
    az storage account network-rule remove \
      --resource-group $RESOURCE_GROUP \
      --account-name $STORAGE_ACCOUNT_NAME \
      --ip-address $MY_IP

    # Add virtual network rule
    az storage account network-rule add \
      --resource-group $RESOURCE_GROUP \
      --account-name $STORAGE_ACCOUNT_NAME \
      --vnet-name vnet1 \
      --subnet default
    ```

    ![Network Rules CLI](./images/network-rules-cli.png)

4. Verify network access is restricted:

    ```bash
    # Try to list containers (should fail)
    az storage container list \
      --account-name $STORAGE_ACCOUNT_NAME \
      --account-key $STORAGE_KEY
    ```

    ![Access Restriction Verification](./images/access-restriction-verification.png)

## Cleanup your resources

    ![Cleanup Resources](./images/cleanup-resources.png)

If you are working with **your own subscription** take a minute to delete the lab resources. This will ensure resources are freed up and cost is minimized. The easiest way to delete the lab resources is to delete the lab resource group.

### Method 1: Azure Portal

In the Azure portal, select the resource group, select **Delete the resource group**, **Enter resource group name**, and then click **Delete**.

### Method 2: Azure Cloud Shell (Bash)

```bash
# Delete resource group (this will delete all resources in the group)
az group delete --name $RESOURCE_GROUP --yes --no-wait
```

### Method 3: Azure PowerShell

Using Azure PowerShell, `Remove-AzResourceGroup -Name resourceGroupName`.

### Method 4: Azure CLI

Using the CLI, `az group delete --name resourceGroupName`.

![Resource Group Deletion](./images/resource-group-deletion.png)

### Extra

```bash
# Delete resource group (this will delete all resources in the group)
az group delete --name $RESOURCE_GROUP --yes
```

![Resource Group Deletion](./images/resource-group-deletion-wait.png)

## Extend your learning with Copilot
Copilot can assist you in learning how to use the Azure scripting tools. Copilot can also assist in areas not covered in the lab or where you need more information. Open an Edge browser and choose Copilot (top right) or navigate to *copilot.microsoft.com*. Take a few minutes to try these prompts.

- Provide an Azure PowerShell script to create a storage account with a blob container.
- Provide a checklist I can use to ensure my Azure storage account is secure.
- Create a table to compare Azure storage redundancy models.

<!-- [Copilot Learning](../../images/copilot-learning.png) -->

## Learn more with self-paced training

- [Optimize your cost with Azure Blob Storage](https://learn.microsoft.com/training/modules/optimize-your-cost-azure-blob-storage/). Learn how to optimize your cost with Azure Blob Storage.
- [Control access to Azure Storage with shared access signatures](https://learn.microsoft.com/training/modules/control-access-to-azure-storage-with-sas/). Grant access to data stored in your Azure Storage accounts securely by using shared access signatures.

## Key takeaways

<!-- ![Key Takeaways](./images/key-takeaways.png) -->

Congratulations on completing the lab. Here are the main takeaways for this lab.

- An Azure storage account contains all your Azure Storage data objects: blobs, files, queues, and tables. The storage account provides a unique namespace for your Azure Storage data that is accessible from anywhere in the world over HTTP or HTTPS.
- Azure storage provides several redundancy models including Locally redundant storage (LRS), Zone-redundant storage (ZRS), and Geo-redundant storage (GRS).
- Azure blob storage allows you to store large amounts of unstructured data on Microsoft's data storage platform. Blob stands for Binary Large Object, which includes objects such as images and multimedia files.
- Azure file Storage provides shared storage for structured data. The data can be organized in folders.
- Immutable storage provides the capability to store data in a write once, read many (WORM) state. Immutable storage policies can be time-based or legal-hold.

## Additional Azure CLI Commands Reference

Here are some additional useful Azure CLI commands for managing storage accounts:

### Command multiples

```bash
# Subscription list
az account list --output table
#
az account set --subscription "<SUBSCRIPTION_NAME> | (or) <SUBSCRIPTION_ID>"

#
RESOURCE_GROUP='<NAME_RESOURCE_GROUP>'; STORAGE_ACCOUNT_NAME='<NAME_STORAGE_ACCOUNT_NAME>'; STORAGE_KEY=$(az storage account keys list --resource-group $RESOURCE_GROUP --account-name $STORAGE_ACCOUNT_NAME --query '[0].value' -o tsv)
LOCATION="westeurope"

```

### Storage Account Management

```bash
# List all storage accounts
az storage account list --output table

# Show storage account details
az storage account show --name $STORAGE_ACCOUNT_NAME --resource-group $RESOURCE_GROUP

# Get storage account keys
az storage account keys list --account-name $STORAGE_ACCOUNT_NAME --resource-group $RESOURCE_GROUP

# Regenerate storage account key
az storage account keys renew --account-name $STORAGE_ACCOUNT_NAME --resource-group $RESOURCE_GROUP --key key1
```

### Blob Management

```bash
# List all containers
az storage container list --account-name $STORAGE_ACCOUNT_NAME --account-key $STORAGE_KEY --output table

# List blobs in container
az storage blob list --container-name data --account-name $STORAGE_ACCOUNT_NAME --account-key $STORAGE_KEY --output table

# Download blob
az storage blob download --container-name data --name securitytest/testfile.txt --file downloaded-file.txt --account-name $STORAGE_ACCOUNT_NAME --account-key $STORAGE_KEY

# Delete blob
az storage blob delete --container-name data --name securitytest/testfile.txt --account-name $STORAGE_ACCOUNT_NAME --account-key $STORAGE_KEY
```

### File Share Management

```bash
# List file shares
az storage share list --account-name $STORAGE_ACCOUNT_NAME --account-key $STORAGE_KEY --output table

# Download file from share
az storage file download --share-name share1 --path testdir/fileshare-test.txt --dest downloaded-share-file.txt --account-name $STORAGE_ACCOUNT_NAME --account-key $STORAGE_KEY

# Delete file from share
az storage file delete --share-name share1 --path testdir/fileshare-test.txt --account-name $STORAGE_ACCOUNT_NAME --account-key $STORAGE_KEY
```

<!-- ![CLI Commands Reference](./images/cli-commands-reference.png) -->
