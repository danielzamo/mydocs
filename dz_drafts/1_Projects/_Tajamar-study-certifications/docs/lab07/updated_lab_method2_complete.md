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

**Note**: If you encounter the error *"The request may be blocked by network rules of storage account"*, follow these additional steps:

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

**Alternative option - Legal hold policy:**

```bash
# Alternative: Set legal hold policy (uses Azure AD authentication)
az storage container legal-hold set \
    --account-name $STORAGE_ACCOUNT_NAME \
    --container-name data \
    --tags retention-policy lab-exercise
```

4. Upload a file to blob storage:

```bash
# Create a sample file
echo "This is a test file for blob storage" > testfile.txt

# Upload file to specific folder
az storage blob upload \
    --account-name $STORAGE_ACCOUNT_NAME \
    --account-key $STORAGE_KEY \
    --container-name data \
    --name securitytest/testfile.txt \
    --file testfile.txt \
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
    --name securitytest/testfile.txt \
    --permissions r \
    --expiry $(date -d '+1 day' '+%Y-%m-%d') \
    --output tsv)

# Create full URL with SAS token
BLOB_URL="https://${STORAGE_ACCOUNT_NAME}.blob.core.windows.net/data/securitytest/testfile.txt?${SAS_TOKEN}"

echo "Blob URL with SAS token: $BLOB_URL"
```

6. Test secure access:

```bash
# Test access with SAS URL (this will show the file content)
curl "$BLOB_URL"
```

7. Optional - Restore network restrictions after lab completion:

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

### Troubleshooting Network Access Issues

**Common Issue**: Storage account network rules blocking CLI access

**Solution Steps**:
1. Check current network configuration
2. Add your public IP to allowed IPs
3. Temporarily set default action to "Allow"
4. Complete lab operations
5. Optionally restore restrictive settings

**Key Network Rule Settings**:
- `defaultAction`: Controls access when no specific rules match
- `ipRules`: List of allowed IP addresses
- `virtualNetworkRules`: List of allowed virtual networks
- `bypass`: Services that can bypass network rules (typically "AzureServices")

### Troubleshooting Immutability Policy Issues

**Common Issue**: Immutability policy configuration errors

**Solution**: The `immutability-policy create` command uses Azure AD authentication and creates a time-based retention policy. This is often more reliable than legal hold policies for lab exercises.

**Key Benefits of Time-based Retention**:
- More straightforward configuration
- Automatic expiration after the specified period
- Easier to manage and understand