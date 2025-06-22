**Lab 02b - Manage Governance via Azure Policy**

**Lab introduction**

In this lab, you learn how to implement your organization's governance
plans. You learn how Azure policies can ensure operational decisions are
enforced across the organization. You learn how to use resource tagging
to improve reporting.

This lab requires an Azure subscription. Your subscription type may
affect the availability of features in this lab. You may change the
region, but the steps are written using **East US**.

**Estimated timing: 30 minutes**

**Lab scenario**

Your organization\'s cloud footprint has grown considerably in the last
year. During a recent audit, you discovered a substantial number of
resources that do not have a defined owner, project, or cost center. In
order to improve management of Azure resources in your organization, you
decide to implement the following functionality:

-   apply resource tags to attach important metadata to Azure resources

-   enforce the use of resource tags for new resources by using Azure
    policy

-   update existing resources with resource tags

-   use resource locks to protect configured resources

**Architecture diagram**

![Diagram of the task
architecture.](./media/image1.png){width="5.905555555555556in"
height="3.0131944444444443in"}

**Job skills**

-   Task 1: Create and assign tags via the Azure portal.

-   Task 2: Enforce tagging via an Azure Policy.

-   Task 3: Apply tagging via an Azure Policy.

-   Task 4: Configure and test resource locks.

**Task 1: Assign tags via the Azure portal**

In this task, you will create and assign a tag to an Azure resource
group via the Azure portal. Tags are a critical component of a
governance strategy as outlined by the Microsoft Well-Architected
Framework and Cloud Adoption Framework. Tags can allow you to quickly
identify resource owners, sunset dates, group contacts, and other
name/value pairs that your organization deems important. For this task,
you assign a tag identifying the resource role (\'Infra\' for
\'Infrastructure\').

1.  Sign in to the **Azure portal** - https://portal.azure.com.

2.  Search for and select Resource groups.

3.  From the Resource groups, select **+ Create**.

  -----------------------------------------------------------------------
  **Setting**                            **Value**
  -------------------------------------- --------------------------------
  Subscription name                      your subscription

  Resource group name                    az104-rg2

  Location                               **East US**
  -----------------------------------------------------------------------

4.  **Note:** For each lab in this course you will create a new resource
    group. This lets you quickly locate and manage your lab resources.

5.  Select **Next: Tags** and create a new tag.

  -----------------------------------------------------------------------
  **Setting**                   **Value**
  ----------------------------- -----------------------------------------
  Name                          Cost Center

  Value                         000
  -----------------------------------------------------------------------

6.  Select **Review + Create**, and then select **Create**.

En las capturas a continuación se muestra la secuencia y/o capturas de
pantallas.

+-----------------------------------+----------------------------------+
| ![](./media/image2.               | ![](./medi                       |
| jpeg){width="2.732638888888889in" | a/image3.jpeg){width="2.69375in" |
| height="3.1333333333333333in"}    | height=                          |
|                                   | "3.1777777777777776in"}*Resource |
| *Resources Group*                 | groups \> Create*                |
+===================================+==================================+
| ![](./media/image4.j              | ![](./media/image5.j             |
| peg){width="2.8465277777777778in" | peg){width="2.811111111111111in" |
| height="                          | height                           |
| 3.3541666666666665in"}*Establecer | ="3.3118055555555554in"}*Segundo |
| especificación a crear*           | paso del asistente Create RG*    |
+-----------------------------------+----------------------------------+

  -----------------------------------------------------------------------
  ![](./media/image6.jpeg){width="2.8986111111111112in"
  height="3.415277777777778in"}*Revisión de la creación del RG*
  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

**Task 2: Enforce tagging via an Azure Policy**

In this task, you will assign the built-in *Require a tag and its value
on resources* policy to the resource group and evaluate the outcome.
Azure Policy can be used to enforce configuration, and in this case,
governance, to your Azure resources.

1.  In the Azure portal, search for and select Policy.

2.  In the **Authoring** blade, select **Definitions**. Take a moment to
    browse through the list of [built-in policy
    definitions](https://learn.microsoft.com/azure/governance/policy/samples/built-in-policies) that
    are available for you to use. Notice you can also search for a
    definition.

3.  Click the entry representing the **Require a tag and its value on
    resources** built-in policy. Take a minute to review the definition.

4.  On the **Require a tag and its value on resources** built-in policy
    definition blade, click **Assign**.

5.  Specify the **Scope** by clicking the ellipsis button and selecting
    the following values. Click **Select** when you are done.

  -----------------------------------------------------------------------
  **Setting**                        **Value**
  ---------------------------------- ------------------------------------
  Subscription                       *your subscription*

  Resource Group                     **az104-rg2**
  -----------------------------------------------------------------------

6.  **Note**: You can assign policies on the management group,
    subscription, or resource group level. You also have the option of
    specifying exclusions, such as individual subscriptions, resource
    groups, or resources. In this scenario, we want the tag on all the
    resources in the resource group.

7.  Configure the **Basics** properties of the assignment by specifying
    the following settings (leave others with their defaults):

  -----------------------------------------------------------------------
  **Setting**       **Value**
  ----------------- -----------------------------------------------------
  Assignment name   Require Cost Center tag with Default value

  Description       Require Cost Center tag with default value for all
                    resources in the resource group

  Policy            Enabled
  enforcement       
  -----------------------------------------------------------------------

8.  **Note**: The **Assignment name** is automatically populated with
    the policy name you selected, but you can change it.
    The **Description** is optional. Notice you can disable the policy
    at any time.

9.  Click **Next** and set **Parameters** to the following values:

  -----------------------------------------------------------------------
  **Setting**                       **Value**
  --------------------------------- -------------------------------------
  Tag Name                          Cost Center

  Tag Value                         000
  -----------------------------------------------------------------------

10. Click **Next** and review the **Remediation** tab. Leave
    the **Create a Managed Identity** checkbox unchecked.

11. Click **Review + Create** and then click **Create**.

+----------------------------------+-----------------------------------+
| **Task 2: Capturas sesión**      |                                   |
+==================================+===================================+
| ![](./media/image7.              | ![](./                            |
| png){width="2.845138888888889in" | media/image8.png){width="2.875in" |
| heig                             | hei                               |
| ht="3.341666666666667in"}*Search | ght="3.377083333333333in"}*Policy |
| bar \> Policy*                   | \> Authoring*                     |
+----------------------------------+-----------------------------------+
| ![](./media/image9.p             | ![](./media/image10               |
| ng){width="2.7840277777777778in" | .png){width="2.827777777777778in" |
| heigh                            | hei                               |
| t="3.2694444444444444in"}*Policy | ght="3.321527777777778in"}*Policy |
| \> Authoring \> Definitions*     | \> Definitions \> Search: Require |
|                                  | a tag\....*                       |
+----------------------------------+-----------------------------------+
| ![](./media/image11.             | ![](./media/image12               |
| png){width="2.801388888888889in" | .png){width="2.810416666666667in" |
| heig                             | heig                              |
| ht="3.290277777777778in"}Captura | ht="3.3006944444444444in"}Captura |
| 10: Policy \> Definitions \>     | 11: Policy \> Definitions \>      |
| Assign policy                    | Scope                             |
+----------------------------------+-----------------------------------+
| ![](./media/image13.             | ![](./media/image14               |
| png){width="2.801388888888889in" | .png){width="2.798611111111111in" |
| heig                             | hei                               |
| ht="3.290277777777778in"}Captura | ght="3.303472222222222in"}Captura |
| 12: Policy \> Definitions \>     | 13: Policy \> Definitions \>      |
| ..\> Assign policy               | \...\> Asign policy \...review +  |
|                                  | create                            |
+----------------------------------+-----------------------------------+
| ![](./media/image15.             |                                   |
| png){width="2.816666666666667in" |                                   |
| height="3.3243055555555556in"}   |                                   |
|                                  |                                   |
| *Captura 14: : Policy \>         |                                   |
| Definitions \> \...\> Asign      |                                   |
| policy \...review (create)*      |                                   |
+----------------------------------+-----------------------------------+

**Note**: Now you will verify that the new policy assignment is in
effect by attempting to create an Azure Storage account in the resource
group. You will create the storage account without adding the required
tag.

**Note**: It might take between 5 and 10 minutes for the policy to take
effect.

12. In the portal, search for and select Storage Account, and select **+
    Create**.

13. On the **Basics** tab of the **Create storage account** blade,
    complete the configuration.

  -----------------------------------------------------------------------
  **Setting**      **Value**
  ---------------- ------------------------------------------------------
  Resource group   **az104-rg2**

  Storage account  *any globally unique combination of between 3 and 24
  name             lower case letters and digits, starting with a letter*
  -----------------------------------------------------------------------

14. Select **Review** and then click **Create**.

15. You should receive a **Validation failed** message. View the message
    to identify the reason for the failure. Verify the error message
    states that the resource deployment was disallowed by the policy.

  ------------------------------------------------------------------------------------------------------------------------------
  **Task 2: Probando la "Policy" \> Capturas sesión resolución**  
  --------------------------------------------------------------- --------------------------------------------------------------
  ![A screenshot of a computer AI-generated content may be        ![A screenshot of a computer AI-generated content may be
  incorrect.](./media/image16.png){width="2.9402777777777778in"   incorrect.](./media/image17.png){width="2.957638888888889in"
  height="3.470138888888889in"}Search \> Storage Account          height="3.4902777777777776in"}Captura 16: Storage accounts \>
                                                                  Create

  ![A screenshot of a computer AI-generated content may be        ![A screenshot of a computer AI-generated content may be
  incorrect.](./media/image18.png){width="2.816666666666667in"    incorrect.](./media/image19.png){width="2.816666666666667in"
  height="3.3243055555555556in"}Storage accounts \> Create a      height="3.3243055555555556in"}Error al intentar crearlo (la
  storage account                                                 policy se aplicó)
  ------------------------------------------------------------------------------------------------------------------------------

**Note**: By clicking the **Raw Error** tab, you can find more details
about the error, including the name of the role definition **Require
Cost Center tag with Default value**. The deployment failed because the
storage account you attempted to create did not have a tag named **Cost
Center** with its value set to **Default**.

**Task 3: Apply tagging via an Azure policy**

In this task, we will use the new policy definition to remediate any
non-compliant resources. In this scenario, we will make any child
resources of a resource group inherit the **Cost Center** tag that was
defined on the resource group.

1.  In the Azure portal, search for and select Policy.

2.  In the **Authoring** section, click **Assignments**.

3.  In the list of assignments, click the ellipsis icon in the row
    representing the **Require Cost Center tag with Default
    value** policy assignment and use the **Delete assignment** menu
    item to delete the assignment.

4.  Click **Assign policy** and specify the **Scope** by clicking the
    ellipsis button and selecting the following values:

  -----------------------------------------------------------------------
  **Setting**                   **Value**
  ----------------------------- -----------------------------------------
  Subscription                  your Azure subscription

  Resource Group                az104-rg2
  -----------------------------------------------------------------------

5.  To specify the **Policy definition**, click the ellipsis button and
    then search for and select Inherit a tag from the resource group if
    missing.

6.  Select **Add** and then configure the
    remaining **Basics** properties of the assignment.

  -----------------------------------------------------------------------
  **Setting**        **Value**
  ------------------ ----------------------------------------------------
  Assignment name    Inherit the Cost Center tag and its value 000 from
                     the resource group if missing

  Description        Inherit the Cost Center tag and its value 000 from
                     the resource group if missing

  Policy enforcement Enabled
  -----------------------------------------------------------------------

7.  Click **Next** twice and set **Parameters** to the following values:

  -----------------------------------------------------------------------
  **Setting**                       **Value**
  --------------------------------- -------------------------------------
  Tag Name                          Cost Center

  -----------------------------------------------------------------------

8.  Click **Next** and, on the **Remediation** tab, configure the
    following settings (leave others with their defaults):

  -----------------------------------------------------------------------
  **Setting**               **Value**
  ------------------------- ---------------------------------------------
  Create a remediation task enabled

  Policy to remediate       **Inherit a tag from the resource group if
                            missing**
  -----------------------------------------------------------------------

> **Note**: This policy definition includes the **Modify** effect. So, a
> managed identity is required.

9.  Click **Review + Create** and then click **Create**.

+----------------------------------+-----------------------------------+
| **Session Task 3: Apply tagging  |                                   |
| via an Azure policy**            |                                   |
|                                  |                                   |
| -   **\...Delete                 |                                   |
|     assignment** \...            |                                   |
+==================================+===================================+
| ![](./media/image20.             | ![](./media/image21               |
| png){width="2.657638888888889in" | .png){width="2.640277777777778in" |
| height="3.1368055555555556in"}   | he                                |
|                                  | ight="3.115972222222222in"}Policy |
| Search bar \> policy             | \> Assignments                    |
+----------------------------------+-----------------------------------+
| ![](./media/image22.             | ![](./media/image23.              |
| png){width="2.692361111111111in" | png){width="2.6930555555555555in" |
| height="3.1777777777777776in"}   | he                                |
|                                  | ight="3.178472222222222in"}Policy |
| Policy \> Authoring \>           | \> Assignment \> Delete           |
| Assignments \> \[Seleccionar     | assignment                        |
| según corresponda\]              |                                   |
+----------------------------------+-----------------------------------+

**Note**: To verify that the new policy assignment is in effect, you
will create another Azure storage account in the same resource group
without explicitly adding the required tag.

**Note**: It might take between 5 and 10 minutes for the policy to take
effect.

10. Search for and select Storage Account, and click **+ Create**.

11. On the **Basics** tab of the **Create storage account** blade,
    verify that you are using the Resource Group that the Policy was
    applied to and specify the following settings (leave others with
    their defaults) and click **Review**:

  -----------------------------------------------------------------------
  **Setting**      **Value**
  ---------------- ------------------------------------------------------
  Storage account  *any globally unique combination of between 3 and 24
  name             lower case letters and digits, starting with a letter*

  -----------------------------------------------------------------------

12. Verify that this time the validation passed and click **Create**.

13. Once the new storage account is provisioned, click **Go to
    resource**.

14. On the **Tags** blade, note that the tag **Cost Center** with the
    value **000** has been automatically assigned to the resource.

  ---------------------------------------------------------------------------------------------------------------
  **Session Task 3: Apply tagging via an Azure policy \>  
  validando crear un Storage account**                    
  ------------------------------------------------------- -------------------------------------------------------
  ![](./media/image17.png){width="2.7159722222222222in"   ![](./media/image24.png){width="2.7104166666666667in"
  height="3.2055555555555557in"}Storage accounts          height="3.1993055555555556in"}Storage accounts \>
                                                          Create a storage account \>\[Basics\]

  ![](./media/image25.png){width="2.6875in"               
  height="3.172222222222222in"}\                          
  Storage accounts \> Create a storage account - review   

                                                          
  ---------------------------------------------------------------------------------------------------------------

**Did you know?** If you search for and select **Tags** in the portal,
you can view the resources with a specific tag.

Crear storage account

![A screenshot of a computer AI-generated content may be
incorrect.](./media/image26.png){width="2.66875in"
height="3.1493055555555554in"}

Review

![A screenshot of a computer AI-generated content may be
incorrect.](./media/image27.png){width="5.905555555555556in"
height="6.970138888888889in"}

Storage account creado

![A screenshot of a computer AI-generated content may be
incorrect.](./media/image28.png){width="5.905555555555556in"
height="6.970138888888889in"}

**Task 4: Configure and test resource locks**

In this task, you configure and test a resource lock. Locks prevent
either deletions or modifications of a resource.

1.  Search for and select your resource group.

2.  In the **Settings** blade, select **Locks**.

3.  Select **Add** and complete the resource lock information. When
    finished select **Ok**.

  -----------------------------------------------------------------------
  **Setting**       **Value**
  ----------------- -----------------------------------------------------
  Lock name         rg-lock

  Lock type         **delete** (notice the selection for read-only)
  -----------------------------------------------------------------------

4.  Navigate to the resource group **Overview** blade, and
    select **Delete resource group**.

5.  In the **Enter resource group name to confirm deletion** textbox
    provide the resource group name, az104-rg2. Notice you can copy and
    paste the resource group name.

6.  Notice the warning: Deleting this resource group and its dependent
    resources is a permanent action and cannot be undone.
    Select **Delete**.

7.  You should receive a notification denying the deletion.

**Note:** You will need to remove the lock if you intend to delete the
resource group.

**Cleanup your resources**

If you are working with **your own subscription** take a minute to
delete the lab resources. This will ensure resources are freed up and
cost is minimized. The easiest way to delete the lab resources is to
delete the lab resource group.

-   In the Azure portal, select the resource group, select **Delete the
    resource group**, **Enter resource group name**, and then
    click **Delete**.

-   Using Azure PowerShell, Remove-AzResourceGroup -Name
    resourceGroupName.

-   Using the CLI, az group delete \--name resourceGroupName.

**Extend your learning with Copilot**

Copilot can assist you in learning how to use the Azure scripting tools.
Copilot can also assist in areas not covered in the lab or where you
need more information. Open an Edge browser and choose Copilot (top
right) or navigate to *copilot.microsoft.com*. Take a few minutes to try
these prompts.

-   What are the Azure PowerShell and CLI commands for adding and
    deleting resource locks on a resource group?

-   Tabulate the differences between Azure policy and Azure RBAC,
    include examples.

-   What are the steps to enforce Azure policy and remediate resources
    which are not compliant?

-   How can I get a report of Azure resources with specific tags?

**Learn more with self-paced training**

-   [Design an enterprise governance
    strategy](https://learn.microsoft.com/training/modules/enterprise-governance/).
    Use RBAC and Azure Policy to limit access to your Azure solutions,
    and determine which method is right for your security goals.

**Key takeaways**

Congratulations on completing the lab. Here are the main takeaways for
this lab.

-   Azure tags are metadata that consists of a key-value pair. Tags
    describe a particular resource in your environment. In particular,
    tagging in Azure enables you to label your resources in a logical
    manner.

-   Azure Policy establishes conventions for resources. Policy
    definitions describe resource compliance conditions and the effect
    to take if a condition is met. A condition compares a resource
    property field or a value to a required value. There are many
    built-in policy definitions and you can customize the policies.

-   The Azure Policy remediation task feature is used to bring resources
    into compliance based on a definition and assignment. Resources that
    are non-compliant to a modify or deployIfNotExist definition
    assignment, can be brought into compliance using a remediation task.

-   You can configure a resource lock on a subscription, resource group,
    or resource. The lock can protect a resource from accidental user
    deletions and modifications. The lock overrides any user
    permissions.

-   Azure Policy is pre-deployment security practice. RBAC and resource
    locks are post-deployment security practice.
