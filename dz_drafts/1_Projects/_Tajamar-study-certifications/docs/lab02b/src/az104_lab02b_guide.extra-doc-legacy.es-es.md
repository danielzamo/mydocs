# Lab 02b - Manage Governance via Azure Policy - Guía Completa

## Task 1: Crear y asignar tags via Azure Portal

### Navegación por la interfaz web:

1. **Acceso al Portal de Azure**
   - Ir a `https://portal.azure.com`
   - Iniciar sesión con las credenciales de Azure

2. **Buscar Resource Groups**
   - En la barra de búsqueda superior, escribir "Resource groups"
   - Hacer clic en el servicio "Resource groups" en los resultados

![Búsqueda de Resource Groups](./images/search-resource-groups.png)

3. **Crear nuevo Resource Group**
   - Hacer clic en el botón **"+ Create"** en la parte superior izquierda
   - Completar el formulario:
     - **Subscription**: Seleccionar tu suscripción
     - **Resource group name**: `az104-rg2`
     - **Region**: `East US`

![Creación de Resource Group - Basics](./images/create-resource-group-basics.png)

4. **Configurar Tags**
   - Hacer clic en **"Next: Tags"** o ir directamente a la pestaña "Tags"
   - Agregar el tag:
     - **Name**: `Cost Center`
     - **Value**: `000`

![Configuración de Tags](./images/resource-group-tags.png)

5. **Revisar y crear**
   - Hacer clic en **"Review + create"**
   - Verificar la configuración y hacer clic en **"Create"**

![Revisión y creación](./images/review-create-resource-group.png)

### Comando CLI alternativo:

```bash
# Crear resource group con tags
az group create \
  --name az104-rg2 \
  --location eastus \
  --tags "Cost Center=000"
```

---

## Task 2: Enforce tagging via Azure Policy

### Navegación por la interfaz web:

1. **Acceder a Azure Policy**
   - En la barra de búsqueda, escribir "Policy"
   - Seleccionar "Policy" en los resultados

![Búsqueda de Azure Policy](./images/search-azure-policy.png)

2. **Crear nueva Policy Assignment**
   - En el panel izquierdo, hacer clic en **"Assignments"**
   - Hacer clic en **"+ Assign policy"**

![Policy Assignments](./images/policy-assignments.png)

3. **Configurar el Scope**
   - **Scope**: Seleccionar tu suscripción
   - **Resource Group**: Seleccionar `az104-rg2` (opcional, para limitar el alcance)

4. **Seleccionar Policy Definition**
   - Hacer clic en los **"..."** junto a "Policy definition"
   - Buscar "Require a tag and its value on resources"
   - Seleccionar esta policy built-in

![Selección de Policy Definition](./images/select-policy-definition.png)

5. **Configurar Parameters**
   - **Tag Name**: `Cost Center`
   - **Tag Value**: `000`

![Configuración de parámetros](./images/policy-parameters.png)

6. **Configurar Remediation**
   - Ir a la pestaña **"Remediation"**
   - Marcar **"Create a remediation task"** si deseas remediar recursos existentes

7. **Finalizar Assignment**
   - Ir a **"Review + create"**
   - Hacer clic en **"Create"**

### Comandos CLI alternativos:

```bash
# Buscar policy definition
az policy definition list --query "[?displayName=='Require a tag and its value on resources'].{Name:name,DisplayName:displayName}" --output table

# Asignar policy
az policy assignment create \
  --name "Require-CostCenter-Tag" \
  --display-name "Require Cost Center Tag" \
  --policy "/providers/Microsoft.Authorization/policyDefinitions/1e30110a-5ceb-460c-a204-c1c3969c6d62" \
  --scope "/subscriptions/YOUR_SUBSCRIPTION_ID/resourceGroups/az104-rg2" \
  --params '{"tagName":{"value":"Cost Center"},"tagValue":{"value":"000"}}'
```

---

## Task 3: Apply tagging via Azure Policy (Remediation)

### Navegación por la interfaz web:

1. **Acceder a Policy Compliance**
   - En Azure Policy, hacer clic en **"Compliance"** en el panel izquierdo
   - Verificar el estado de compliance de la policy asignada

![Policy Compliance](./images/policy-compliance.png)

2. **Crear Remediation Task**
   - Ir a **"Remediation"** en el panel izquierdo
   - Hacer clic en **"+ Remediate"**
   - Seleccionar la policy assignment creada anteriormente

![Crear Remediation Task](./images/create-remediation-task.png)

3. **Configurar Remediation**
   - **Policy assignment**: Seleccionar la policy "Require Cost Center Tag"
   - **Resources to remediate**: Seleccionar los recursos que necesitan ser remediados
   - Hacer clic en **"Remediate"**

4. **Verificar aplicación**
   - Crear un recurso de prueba (por ejemplo, Storage Account) para verificar que se aplica automáticamente el tag

![Verificación de tag aplicado](./images/verify-tag-applied.png)

### Comandos CLI alternativos:

```bash
# Verificar compliance de policy
az policy state list --resource-group az104-rg2 --query "[?complianceState=='NonCompliant'].{Resource:resourceId,State:complianceState}" --output table

# Crear remediation task
az policy remediation create \
  --name "remediate-cost-center-tag" \
  --policy-assignment "/subscriptions/YOUR_SUBSCRIPTION_ID/resourceGroups/az104-rg2/providers/Microsoft.Authorization/policyAssignments/Require-CostCenter-Tag" \
  --resource-group az104-rg2

# Verificar estado de remediation
az policy remediation show \
  --name "remediate-cost-center-tag" \
  --resource-group az104-rg2
```

---

## Task 4: Configure and test resource locks

### Navegación por la interfaz web:

1. **Acceder al Resource Group**
   - Ir a "Resource groups" y seleccionar `az104-rg2`

2. **Configurar Resource Lock**
   - En el panel izquierdo del resource group, hacer clic en **"Locks"**
   - Hacer clic en **"+ Add"**

![Acceso a Resource Locks](./images/resource-group-locks.png)

3. **Configurar el Lock**
   - **Lock name**: `az104-rg2-lock`
   - **Lock type**: Seleccionar **"Delete"** (previene eliminación) o **"Read-only"** (previene modificaciones)
   - **Notes**: Agregar una descripción opcional

![Configuración de Resource Lock](./images/configure-resource-lock.png)

4. **Aplicar el Lock**
   - Hacer clic en **"OK"** para crear el lock

5. **Probar el Lock**
   - Intentar eliminar el resource group para verificar que el lock funciona
   - Debería aparecer un error indicando que el recurso está protegido

![Prueba de Resource Lock](./images/test-resource-lock.png)

### Comandos CLI alternativos:

```bash
# Crear resource lock (Delete)
az lock create \
  --name az104-rg2-lock \
  --lock-type CanNotDelete \
  --resource-group az104-rg2 \
  --notes "Prevents accidental deletion of resource group"

# Listar locks
az lock list --resource-group az104-rg2 --output table

# Probar eliminación (debería fallar)
az group delete --name az104-rg2 --yes --no-wait

# Verificar que el grupo sigue existiendo
az group show --name az104-rg2 --query name --output tsv

# Eliminar lock (si es necesario)
az lock delete --name az104-rg2-lock --resource-group az104-rg2
```

---

## Verificación y Cleanup

### Verificar implementación completa:

```bash
# Verificar resource group y tags
az group show --name az104-rg2 --query "{Name:name,Tags:tags}" --output table

# Verificar policy assignments
az policy assignment list --resource-group az104-rg2 --query "[].{Name:displayName,State:enforcementMode}" --output table

# Verificar locks
az lock list --resource-group az104-rg2 --query "[].{Name:name,Level:level}" --output table
```

### Cleanup al final del lab:

```bash
# Eliminar lock primero
az lock delete --name az104-rg2-lock --resource-group az104-rg2

# Eliminar policy assignment
az policy assignment delete --name "Require-CostCenter-Tag" --resource-group az104-rg2

# Eliminar resource group
az group delete --name az104-rg2 --yes --no-wait
```

---

## Puntos Clave para Capturas de Pantalla

1. **Búsqueda de servicios**: Capturar la barra de búsqueda con resultados
2. **Formularios de creación**: Capturar cada paso del wizard
3. **Configuración de tags**: Mostrar la pestaña de tags y los valores ingresados
4. **Policy assignments**: Capturar la lista de policies y el proceso de asignación
5. **Compliance dashboard**: Mostrar el estado de compliance
6. **Resource locks**: Capturar la configuración y el mensaje de error al intentar eliminar

Este enfoque te permite tanto usar la interfaz gráfica como practicar con Azure CLI, proporcionando una comprensión completa de la gestión de governance en Azure.