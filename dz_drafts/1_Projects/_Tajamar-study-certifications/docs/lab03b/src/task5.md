## Task 5: Deploy a resource by using Azure Bicep

In this task, you will use a Bicep file to deploy a managed disk. Bicep is a declarative automation tool that is built on ARM templates.

1. Continue working in the **Cloud Shell** in a **Bash** session.
2. Locate and download the **[azuredeploydisk.bicep]{.mark}** file.
3. **Upload** the bicep file to the Cloud Shell.
4. Select the **Editor** (curly brackets) icon and navigate to the file.
5. Take a minute to read through the bicep template file. Notice how the disk resource is defined.
6. Make the following changes:

   - Change the **managedDiskName** value to Disk4.
   - Change the **sku name** value to StandardSSD_LRS.
   - Change the **diskSizeinGiB** value to 32.

7. Use `Ctrl +S` to save your changes.
8. Now, deploy the template.

    ```sh
    az deployment group create \
      --resource-group az104-rg3 \
      --template-file azuredeploydisk.bicep
    ```

9. Confirm the disk was created.

    ```sh
    az disk list \
      --output table
    ```

    >**Note:** You have successfully deployed five managed disks, each in a different way. Nice job!

## Cleanup your resources

If you are working with **your own subscription** take a minute to delete the lab resources. This will ensure resources are freed up and cost is minimized. The easiest way to delete the lab resources is to
delete the lab resource group.

- In the Azure portal, select the resource group, select **Delete the resource group**, **Enter resource group name**, and then click **Delete**.
- Using Azure PowerShell, `Remove-AzResourceGroup -Name resourceGroupName`.
- Using the CLI, 
  
    ```sh
    az group delete \
      --name resourceGroupName
    ```

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
