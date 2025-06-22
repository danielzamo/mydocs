---
title: "Lab 03 - Manage Azure resources by using Azure Resource Manager
Templates"
author: "Daniel Oscar Zamo"
date: "2025-06-07"
type: "laboratory"
module: "Administer Azure Resources"
---

# Lab 03 - Manage Azure resources by using Azure Resource Manager
Templates

## Lab introduction

In this lab, you learn how to automate resource deployments. You learn about Azure Resource Manager templates and Bicep templates. You learn about the different ways of deploying the templates.

This lab requires an Azure subscription. Your subscription type may affect the availability of features in this lab. You may change the region, but the steps are written using **East US**.

## Estimated timing: 50 minutes

## Interactive lab simulations

**Lab scenario**

Your team wants to look at ways to automate and simplify resource
deployments. Your organization is looking for ways to reduce
administrative overhead, reduce human error and increase consistency.

## Architecture diagram

![Diagram of the tasks.](./az104-lab03-architecture.png)

+ Task 1: Create an Azure Resource Manager template.
+ Task 2: Edit an Azure Resource Manager template and redeploy the template.
+ Task 3: Configure the Cloud Shell and deploy a template with Azure PowerShell.
+ Task 4: Deploy a template with the CLI.
+ Task 5: Deploy a resource by using Azure Bicep.

## Task 1: Create an Azure Resource Manager template

In this task, we will create a managed disk in the Azure portal. Managed disks are storage designed to be used with virtual machines. Once the disk is deployed you will export a template that you can use in other deployments.

1. Sign in to the **Azure portal** - `https://portal.azure.com`.

    ![Azure Portal Home](../../azure-portal-home.png)

2. Search for and select `Disks`.

    ![Search Disks Service](./images/search-disks.png)

3. On the Disks page, select **Create**.

    ![Create Disk Button](./images/create-disk-button.png)

4. On the **Create a managed disk** page, configure the disk and then select **Ok**.

    | Setting | Value |
    | --- | --- |
    | Subscription | `your subscription` |
    | Resource Group | `az104-rg3` (If necessary, select `Create new`.)
    | Disk name | `az104-disk1` |
    | Region | `East US` |
    | Availability zone | `No infrastructure redundancy required` |
    | Source type | `None` |
    | Performance | `Standard HDD` (change size) |
    | Size | `32 Gib` |

    >**Note:** We are creating a simple managed disk so you can practice with templates. Azure managed disks are block-level storage volumes that are managed by Azure.

    ![Disk Configuration Form](./images/disk-configuration.png)

1. Click **Review + Create** then select **Create**.

    ![Final Create Button](./images/final-create-disk.png)

2. Monitor the notifications (upper right) and after the deployment select **Go to resource**.

    ![Deployment Notification](./images/deployment-notification.png)

3. In the **Automation** blade, select **Export template**.

    ![Export Template Menu](./images/export-template-menu.png)

4. Take a minute to review the **Template** and **Parameters** files.

    ![Template Review](./images/template-review.png)

5. Click **Download** and save the templates to the local drive. This creates a compressed zipped file.

    - Click **Download** to save the template files
    - Extract the ZIP file to your Downloads folder
    - Verify you have both `template.json` and `parameters.json`

6. Use File Explorer to extract the content of the downloaded file into the **Downloads** folder on your computer. Notice there are two JSON files (template and parameters).

    >**Did you know?**  You can export an entire resource group or just specific resources within that resource group.

    ![Download Template](./images/download-template.png)

---

## Task 2: Edit an Azure Resource Manager template and then redeploy the template

In this task, you use the downloaded template to deploy a new managed disk. This task outlines how to quicky and easily repeat deployments.

1. In the Azure portal, search for and select `Deploy a custom template`.

    ![Custom Template Deployment](./images/custom-template-deploy.png)

1. On the **Custom deployment** blade, notice there is the ability to use a **Quickstart template**. There are many built-in templates as shown in the drop-down menu.

2. Instead of using a Quickstart, select **Build your own template in the editor**.

3. On the **Edit template** blade, click **Load file** and upload the **template.json** file you downloaded to the local disk.

    - Click **Build your own template in the editor**
    - Click **Load file** and select your downloaded `template.json`

   ![Load Template File](./images/load-template-file.png)

4. Within the editor pane, make these changes.

    + Change **disks_az104_disk1_name** to disk_name (two places to change)
    + Change **az104-disk1** to az104-disk2 (one place to change)
    + Modify the disk name in the template:

    ```json
    "diskName": {
      "defaultValue": "az104-disk2",
      "type": "String"
    }
    ```

    ![Edit Template](./images/edit-template.png)

5. Notice this is a **Standard** disk. The location is **eastus**. The disk size is **32GB**.

6. **Save** your changes.

7. Don\'t forget the parameters file. Select **Edit parameters**, click **Load file** and upload the **parameters.json**.

8. Make this change so it matches the template file.

    Change **disks_az104_disk1_name** to **disk_name** (one place to change)

9.  **Save** your changes.

10. Complete the custom deployment settings:

    | Setting | Value |
    | --- |--- |
    | Subscription | `your subscription` |
    | Resource Group | `az104-rg3` |
    | Region | `(US) East US)` |
    | Disk_name | `az104-disk2` |

    ![Template Parameters](./images/template-parameters.png)

11. Select **Review + Create** and then select **Create**.

    ![Deploy Modified Template](./images/deploy-modified-template.png)

12. Select **Go to resource**. Verify **az104-disk2** was created.

13. On the **Overview** blade, select the resource group, **az104-rg3**. You should now have two disks.

    ![az104-rg3 RG actual](./images/resources-group-actual.png)

14. In the **Settings** section, click **Deployments**.

    >**Note:** All deployments details are documented in the resource group. It is a good practice to review the first few template-based deployments to ensure success prior to using the templates for large-scale operations.

    ![RG > Settings > Deployments](./images/resources-group-setting-deployments.png)

15. Select a deployment and review the content of the **Input** and **Template** blades.

    ![RG > Settings > Deployments > ... > Template](./images/RG-setting-deployments-overview-template.png)

---

## Task 3: Configure the Cloud Shell and deploy a template with PowerShell

In this task, you work with the Azure Cloud Shell and Azure PowerShell. Azure Cloud Shell is an interactive, authenticated, browser-accessible terminal for managing Azure resources. It provides the flexibility of choosing the shell experience that best suits the way you work, either Bash or PowerShell. In this task, you use PowerShell to deploy a template.

1. Select the **Cloud Shell** icon in the top right of the Azure Portal. Alternately, you can navigate directly to https://shell.azure.com.

    ![Selected Cloud Shell](images/cloud-shell-selection.png)

1. When prompted to select either **Bash** or **PowerShell**, select **PowerShell**.
    <!--   ![Selection Azure Cloud Shell](images/cloud-shell-selection.png) -->

    >**Did you know?** If you mostly work with Linux systems, Bash (CLI) feels more familiar. If you mostly work with Windows systems, Azure PowerShell feels more familiar.

3. On the **Getting started** screen select **Mount storage account**, select your **Storage account subscription**, and then select **Apply**.

4. Select **I want to create a storage account** and then **Next**. Complete the **Create storage account** information.

    |**Settings**       | **Values** |
    |:--|:--|
    |Resource Group |      `az104-rg3` |
    |Region  |             `select your region` |
    |Storage account (Create new)    | `must be globally unique, between 3 and 24 characters in length and use numbers and lower case letters only` |
    |File share (Create  new) | `fs-cloudshell` |

5. When completed select **Create**.
    >It will take a couple of minutes to provision the storage.
6. Select **Settings** (top bar) and then **Go to classic version**. It will take a couple of minutes to provision the storage.
7. Select the **Upload/Download files** icon (top bar) and then select **Upload**. It will take a couple of minutes to provision the storage.
8. Upload both the template and parameters files from the **Downloads** directory. It will take a couple of minutes to provision the storage.
9. Select the **Editor (curly brackets)** icon and navigate to the template JSON file on the left in the navigation pane. It will take a couple of minutes to provision the storage.
10. Make a change. For example, change the disk name to `az104-disk3`. Use **Ctrl +S** to save your changes.
    >_It will take a couple of minutes to provision the storage._

    >**Note**: You can target your template deployment to a resource group, subscription, management group, or tenant. Depending on the scope of the deployment, you use different commands.

11. To deploy to a resource group, use `New-AzResourceGroupDeployment`.

    ```powershell
    PS > New-AzResourceGroupDeployment `
     -ResourceGroupName az104-rg3 `
     -TemplateFile template.json `
     -TemplateParameterFile parameters.json
    ```

12. Ensure the command completes and the ProvisioningState is **Succeeded**.
13. Confirm the disk was created.

    ```powershell
    PS> Get-AzDisk
    ```

_**Author's Note:**_ In this case, all tasks are run from the `powershell` CLI.

![Check subscription actual](images/verificar-suscripcion-actual.3.2.png)

![Check RG and create](images/3.3.verificar-existencia-y-creacion-de-RG.png)

![Create w/name random/unique storage account](images/3.4.creacion-storage-account-con-nombre-unico-y-random.png)

![Upload files](images/3.5.subida-ficheros-json.png)

![Ok upload files](images/3.6.subida-ficheros-json-ok.png)

![template.json edit](images/3.7.edicion-fichero-template.json.png)

![parameters.json edit](images/3.8.edicion-fichero-parameters.json.png)

![template.json review](images/3.9.revision-template.json.png)

![parameters.json review](images/3.10.revision-parameters.json.png)

![Resource Group review, and deploy](images/3.11.revision-RG-y-deployment-RG.png)

![Execute: Get-AzDisk](images/3.12.check-disk-was-created.png)

**Note:** Below is the history of commands executed from Azure Cloud Shell (PowerShell). The main commands executed were:

```Powershell
PS> # Verificar suscripción actual
PS> Get-AzContext
PS> # Verificar existencia (o no) del Resource Group az104-rg3
PS> Get-AzResourceGroup -Name "az104-rg3"

PS> # Crear el resource group
PS> New-AzResourceGroup -Name "az104-rg3" -Location "East US"

PS> # Crear storage account (cambia el nombre por uno único)
PS> ## El siguiente comando inicializa variable con un nombre unico (GLOBAL) sobre el entorno/environment Azure
PS> $storageAccountName = "cloudshell" + (Get-Random -Maximum 9999)
PS> New-AzStorageAccount -ResourceGroupName "az104-rg3" -Name  $storageAccountName -Location "East US" -SkuName "Standard_LRS"

PS> # Editar ficheros (segun corresponda)
PS> vim ./template.json
PS> vim ./parameters.json

PS> # Verificar ficheros .json
PS> cat ./template.json
PS> cat ./parameters.json

PS> # Verificación existencia de "az104-rg3"
PS> Get-AzResourceGroup -Name "az104-rg3"

PS> # Ejecutar el Deployment
PS> New-AzResourceGroupDeployment -ResourceGroupName az104-rg3 -TemplateFile template.json -TemplateParameterFile parameters.json

PS> # Check if the disk is created
PS> Get-AzDisk
```

---

## Task 4: Deploy a template with the CLI

1. Continue in the **Cloud Shell** select **Bash**. **Confirm** your choice.

2. Verify your files are available in the Cloud Shell storage. If you completed the previous task your template files should be available.

    ```sh
    ls
    ```

3. Select the **Editor** (curly brackets) icon and navigate to the template JSON file.

4. Make a change. For example, change the disk name to `az104-disk4`. Use `Ctrl +S` to save your changes.

    >**Note**: You can target your template deployment to a resource group, subscription, management group, or tenant. Depending on the scope of the deployment, you use different commands.

5. To deploy to a resource group, use `az deployment group create`.

    ```sh
    az deployment group create \
     --resource-group az104-rg3
     --template-file template.json \--parameters parameters.json
    ```

6. Ensure the command completes and the ProvisioningState is **Succeeded**.

7.  Confirm the disk was created.

    ```sh
    az deployment group create --resource-group az104-rg3 --template-file template.json --parameters parameters.json
    ```

---

## Task 4: Deploy a template with the CLI

1. Continue in the **Cloud Shell** select **Bash**. **Confirm** your choice.

    ![Switch to Bash](images/4.1.switch-to-bash.png)

    ![Confirmed change to Bash](images/4.2.shell-confirmed.png)

2. Verify your files are available in the Cloud Shell storage. If you     completed the previous task your template files should be available.
    ```sh
    ls
    ```

3. Select the **Editor** (curly brackets) icon and navigate to the template JSON file.
4. Make a change. For example, change the disk name to `az104-disk4`. Use `Ctrl +S` to save your changes.

    >**Note**: You can target your template deployment to a resource group, subscription, management group, or tenant. Depending on the scope of the deployment, you use different commands.

    >**Author's note:** Changes are made primarily using the `sed` command of the Bash shell CLI.

    ![Change disk name to az104-disk4](images/4.3.changes-files-to-az104-disk4.png)

5. To deploy to a resource group, use `az deployment group create`.

    ```sh
    $ az deployment group create \
      --resource-group az104-rg3 \
      --template-file template.json \
      --parameters parameters.json
    ```

    ![Execution: az deployment group create](images/4.4.az-deployment-group-create.png)

6. Ensure the command completes and the ProvisioningState is **Succeeded**.

7. Confirm the disk was created.

    ```sh
    az disk list \
      --output table
    ```

    ![az disk list...](images/4.5.az-disk-list.png)

_**Author's Note:**_ The main Bash shell commands executed here were the following:

```sh
# List files
$ ls
# Grep name disk3 in json files
$ grep disk3 *.json
# Change az104-disk3 -> to -> az104-disk4 (w/file backups)
$ sed -i.$(date +%s) 's/az104-disk3/az104-disk4/' *.json
# Check files
$ grep -E 'disk[3-4]{1}' *.json
# az deployment ...
$ az deployment group create \
  --resource-group az104-rg3 \
  --template-file template.json \
  --parameters parameters.json
# List disk (output format table)
$ az disk list --output table
# List group
$ az group list

```

---

## Task 5: Deploy a resource by using Azure Bicep

In this task, you will deploy a managed disk using a Bicep file. Bicep is a domain-specific language (DSL) that simplifies the authoring of ARM templates.

1. Continue working in the **Cloud Shell** in a **Bash** session.

    ![Switch to Bash Shell](./images/task5-1-switch-bash.png)

2. Locate and download the `azuredeploydisk.bicep` file from the lab materials or trusted source.

3. **Upload** the Bicep file to the Cloud Shell.

    ![Upload Bicep File](./images/task5-2-upload-bicep.png)

4. Open the **Editor** (curly brackets icon) and navigate to the `azuredeploydisk.bicep` file.

    <!-- ![Open Bicep in Editor](./images/task5-3-open-editor.png) -->

5. Review the Bicep file. Note how the managed disk is defined using the Bicep syntax.

6. Make the following edits to the Bicep file:
    - Change `managedDiskName` value to `az104-disk5`.
    - Change `sku name` value to `StandardSSD_LRS`.
    - Change `diskSizeGB` value to `32`.

    ![Edit Bicep File](./images/task5-4-edit-bicep.png)

7. Save your changes with `Ctrl + S`.

8. Deploy the Bicep template using the Azure CLI:

    ```sh
    az deployment group create \
      --resource-group az104-rg3 \
      --template-file azuredeploydisk.bicep
    ```

    ![Deploy Bicep Template](./images/task5-5-deploy-bicep.png)

9. Confirm that the disk was created:

    ```sh
    az disk list \
      --output table
    ```

    ![Check Disk Created](./images/task5-6-check-disk.png)

> **Note:** You have now successfully deployed five managed disks, each using a different method: Portal, ARM template (GUI), PowerShell, Azure CLI, and Bicep. Great job!

---

## Cleanup your resources

If you are working with **your own subscription** take a minute to delete the lab resources. This will ensure resources are freed up and cost is minimized. The easiest way to delete the lab resources is to delete the lab resource group.

+ In the Azure portal, select the resource group, select **Delete the resource group**, **Enter resource group name**, and then click **Delete**.
+ Using Azure PowerShell, `Remove-AzResourceGroup -Name az104-rg3`.
+ Using the CLI, `az group delete --name az104-rg3`.

## Extend your learning with Copilot

Copilot can assist you in learning how to use the Azure scripting tools. Copilot can also assist in areas not covered in the lab or where you need more information. Open an Edge browser and choose Copilot (top right) or navigate to *copilot.microsoft.com*. Take a few minutes to try these prompts.

+ What is the format of the Azure Resource Manager template file? Explain each component with examples.
+ How do I use an existing Azure Resource Manager template?
+ Compare and contrast Azure Resource Manager templates and Azure Bicep templates.

## Learn more with self-paced training

+ [Deploy Azure infrastructure by using JSON ARM templates](https://learn.microsoft.com/training/modules/create-azure-resource-manager-template-vs-code/). Write JSON Azure Resource Manager templates (ARM templates) by using
    Visual Studio Code to deploy your infrastructure to Azure consistently and reliably.
+ [Review the features and tools for Azure Cloud Shell](https://learn.microsoft.com/training/modules/review-features-tools-for-azure-cloud-shell/). Cloud Shell features and tools.
+ [Manage Azure resources with Windows PowerShell](https://learn.microsoft.com/training/modules/manage-azure-resources-windows-powershell/). This module explains how to install the necessary modules for cloud services management and use PowerShell commands to perform simple administrative tasks on cloud resources like Azure virtual machines, Azure subscriptions and Azure storage accounts.
+ [Introduction to Bash](https://learn.microsoft.com/training/modules/bash-introduction/). Use Bash to manage IT infrastructure.
+ [Build your first Bicep template](https://learn.microsoft.com/training/modules/build-first-bicep-template/). Define Azure resources within a Bicep template. Improve the consistency and reliability of your deployments, reduce the manual effort required, and scale your deployments across environments. Your template will be flexible and reusable by using parameters, variables, expressions, and modules.

## Key takeaways

Congratulations on completing the lab. Here are the main takeaways for this lab.

+ Azure Resource Manager templates let you deploy, manage, and monitor all the resources for your solution as a group, rather than handling these resources individually.
+ An Azure Resource Manager template is a JavaScript Object Notation (JSON) file that lets you manage your infrastructure declaratively rather than with scripts.
+ Rather than passing parameters as inline values in your template, you can use a separate JSON file that contains the parameter values.
+ Azure Resource Manager templates can be deployed in a variety of ways including the Azure portal, Azure PowerShell, and CLI.
+ Bicep is an alternative to Azure Resource Manager templates. Bicep uses a declarative syntax to deploy Azure resources.
+ Bicep provides concise syntax, reliable type safety, and support for code reuse. Bicep offers a first-class authoring experience for your infrastructure-as-code solutions in Azure.


