# Azure Policy Lab - GUI Navigation Guide

## Task 1: Create and Assign Tags via Azure Portal

### Step-by-Step Navigation:

1. **Access Azure Portal**
   - Go to: `https://portal.azure.com`
   - Sign in with your credentials

2. **Create Resource Group**
   - **Search Bar** (top) → Type: `Resource groups`
   - Click **Resource groups** from results
   - Click **+ Create** button
   - **Blade: "Create a resource group"**
     - **Basics tab:**
       - Subscription: Select your subscription
       - Resource group name: `az104-rg2`
       - Region: `East US`
   - Click **Next: Tags**
   - **Tags tab:**
     - Name: `Cost Center`
     - Value: `000`
   - Click **Review + Create**
   - Click **Create**

---

## Task 2: Enforce Tagging via Azure Policy

### Navigation Path:

1. **Access Policy Service**
   - **Search Bar** → Type: `Policy`
   - Click **Policy** from results

2. **Browse Policy Definitions**
   - **Left Menu: "Authoring"** → Click **Definitions**
   - **Browse built-in policies** or use search
   - **Search Box** → Type: `Require a tag and its value on resources`
   - Click on the policy definition

3. **Assign the Policy**
   - **Blade: Policy Definition** → Click **Assign** button
   - **Blade: "Assign Policy"**
     
     **Basics Tab:**
     - **Scope section:**
       - Click **ellipsis (...)** button
       - Select your subscription
       - Select resource group: `az104-rg2`
       - Click **Select**
     - **Assignment name:** `Require Cost Center tag with Default value`
     - **Description:** `Require Cost Center tag with default value for all resources in the resource group`
     - **Policy enforcement:** `Enabled`
     
     **Parameters Tab:**
     - **Tag Name:** `Cost Center`
     - **Tag Value:** `000`
     
     **Remediation Tab:**
     - Leave **Create a Managed Identity** unchecked
   
   - Click **Review + Create**
   - Click **Create**

4. **Test the Policy (Create Storage Account)**
   - **Search Bar** → Type: `Storage accounts`
   - Click **Storage accounts**
   - Click **+ Create**
   - **Blade: "Create storage account"**
     - **Basics tab:**
       - Resource group: `az104-rg2`
       - Storage account name: `[unique-name]` (3-24 lowercase letters/numbers)
   - Click **Review**
   - Click **Create**
   - **Result:** Should get **Validation failed** error

---

## Task 3: Apply Tagging via Azure Policy (Remediation)

### Navigation Path:

1. **Delete Previous Policy Assignment**
   - **Search Bar** → Type: `Policy`
   - **Left Menu: "Authoring"** → Click **Assignments**
   - Find: `Require Cost Center tag with Default value`
   - Click **ellipsis (...)** → **Delete assignment**

2. **Create New Policy Assignment**
   - **Assignments blade** → Click **Assign policy**
   - **Blade: "Assign Policy"**
     
     **Basics Tab:**
     - **Scope:**
       - Click **ellipsis (...)**
       - Select subscription and `az104-rg2`
       - Click **Select**
     - **Policy definition:**
       - Click **ellipsis (...)**
       - **Search:** `Inherit a tag from the resource group if missing`
       - Select the policy
       - Click **Add**
     - **Assignment name:** `Inherit the Cost Center tag and its value 000 from the resource group if missing`
     - **Description:** Same as assignment name
     - **Policy enforcement:** `Enabled`
     
     **Parameters Tab:**
     - **Tag Name:** `Cost Center`
     
     **Remediation Tab:**
     - **Create a remediation task:** ✅ Enabled
     - **Policy to remediate:** `Inherit a tag from the resource group if missing`
   
   - Click **Review + Create**
   - Click **Create**

3. **Test New Policy**
   - **Search Bar** → Type: `Storage accounts`
   - Click **+ Create**
   - **Create storage account blade:**
     - Resource group: `az104-rg2`
     - Storage account name: `[another-unique-name]`
   - Click **Review** → Click **Create**
   - **Result:** Should succeed
   - After creation, click **Go to resource**
   - **Left Menu** → Click **Tags**
   - **Verify:** `Cost Center: 000` tag is automatically present

---

## Task 4: Configure and Test Resource Locks

### Navigation Path:

1. **Access Resource Group**
   - **Search Bar** → Type: `Resource groups`
   - Click on `az104-rg2`

2. **Configure Resource Lock**
   - **Left Menu: "Settings"** → Click **Locks**
   - Click **+ Add**
   - **Blade: "Add lock"**
     - **Lock name:** `rg-lock`
     - **Lock type:** `Delete` (note: Read-only is also available)
   - Click **OK**

3. **Test the Lock**
   - **Resource group blade** → Click **Overview** (if not already there)
   - Click **Delete resource group**
   - **Confirmation blade:**
     - **Text box:** Type `az104-rg2` (exact name)
     - Notice warning message
   - Click **Delete**
   - **Result:** Should receive denial notification

---

## Key Interface Elements to Remember:

### **Common Navigation Patterns:**
- **Search Bar:** Always at the top for quick service access
- **Left Menu:** Service-specific options (changes based on current service)
- **Ellipsis (...):** Additional actions/options
- **Breadcrumbs:** Top navigation showing current location

### **Policy-Specific Blades:**
- **Policy → Definitions:** Browse available policies
- **Policy → Assignments:** Manage active policy assignments
- **Policy → Compliance:** View compliance status

### **Resource Management Blades:**
- **Resource Groups → Overview:** Main resource information
- **Resource Groups → Settings → Locks:** Resource protection
- **Resource Groups → Settings → Tags:** Tag management

### **Storage Account Blades:**
- **Storage accounts → Create:** Resource creation wizard
- **Storage account → Tags:** View/manage resource tags

---

## Troubleshooting Tips:

1. **Policy takes 5-10 minutes to take effect** - Wait before testing
2. **If policy doesn't work:** Check assignment scope and parameters
3. **If lock doesn't prevent deletion:** Verify lock type and inheritance
4. **Search not finding resources:** Check correct spelling and try synonyms