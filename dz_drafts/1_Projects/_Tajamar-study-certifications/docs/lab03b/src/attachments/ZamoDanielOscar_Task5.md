---
title: "Lab 03 - Manage Azure resources by using Azure Resource Manager Templates"
author: "Daniel Oscar Zamo"
date: "2025-06-07"
type: "laboratory"
module: "Administer Azure Resources"
---

# Lab 03 - Manage Azure resources by using Azure Resource Manager Templates

## Lab introduction

In this lab, you learn how to automate resource deployments. You learn about Azure Resource Manager templates and Bicep templates. You learn about the different ways of deploying the templates.

This lab requires an Azure subscription. Your subscription type may affect the availability of features in this lab. You may change the region, but the steps are written using **East US**.

## Estimated timing: 50 minutes

## Interactive lab simulations

**Lab scenario**

Your team wants to look at ways to automate and simplify resource deployments. Your organization is looking for ways to reduce administrative overhead, reduce human error and increase consistency.

## Architecture diagram

![Diagram of the tasks.](./az104-lab03-architecture.png)

+ Task 1: Create an Azure Resource Manager template.
+ Task 2: Edit an Azure Resource Manager template and redeploy the template.
+ Task 3: Configure the Cloud Shell and deploy a template with Azure PowerShell.
+ Task 4: Deploy a template with the CLI.
+ Task 5: Deploy a resource by using Azure Bicep.

[... Existing content for Tasks 1–4 remains unchanged ...]

---

## Task 5: Deploy a resource by using Azure Bicep

In this task, you will deploy a managed disk using a Bicep file. Bicep is a domain-specific language (DSL) that simplifies the authoring of ARM templates.

1. Continue working in the **Cloud Shell** in a **Bash** session.

    ![Switch to Bash Shell](./images/task5-1-switch-bash.png)

2. Locate and download the `azuredeploydisk.bicep` file from the lab materials or trusted source.

3. **Upload** the Bicep file to the Cloud Shell.

    ![Upload Bicep File](./images/task5-2-upload-bicep.png)

4. Open the **Editor** (curly brackets icon) and navigate to the `azuredeploydisk.bicep` file.

    ![Open Bicep in Editor](./images/task5-3-open-editor.png)

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
