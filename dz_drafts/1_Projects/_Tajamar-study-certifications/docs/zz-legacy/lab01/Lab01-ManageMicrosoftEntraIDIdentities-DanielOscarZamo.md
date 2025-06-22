# Lab 01 - Manage Microsoft Entra ID Identities - Guía Completa

## Información General
- **Tiempo estimado:** 30 minutos
- **Región recomendada:** East US
- **Prerrequisito:** Suscripción de Azure

## Tarea 1: Crear y configurar cuentas de usuario

### Paso 1: Acceder al portal de Azure
1. Ve a https://portal.azure.com
2. Inicia sesión con tu cuenta
3. Selecciona "Cancel" en la pantalla de bienvenida

### Paso 2: Navegar a Microsoft Entra ID
1. Busca "Microsoft Entra ID" en la barra de búsqueda
2. Selecciona el servicio
3. Explora las opciones del panel izquierdo
4. Ve a **Overview** → **Manage tenants** para familiarizarte
5. Revisa **Licenses** para ver las características disponibles

### Paso 3: Crear usuario interno
1. Ve a **Users** → **New user** → **Create new user**
2. Configura los siguientes valores:

| Campo | Valor |
|-------|-------|
| User principal name | az104-user1 |
| Display name | az104-user1 |
| Auto-generate password | ✓ Marcado |
| Account enabled | ✓ Marcado |
| Job title | IT Lab Administrator |
| Department | IT |
| Usage location | United States |

3. Selecciona **Review + create** → **Create**
4. Actualiza la página para confirmar la creación

### Paso 4: Invitar usuario externo
1. Ve a **New user** → **Invite an external user**
2. Configura:

| Campo | Valor |
|-------|-------|
| Email | tu dirección de email |
| Display name | tu nombre |
| Send invite message | ✓ Marcado |
| Message | "Welcome to Azure and our group project" |
| Job title | IT Lab Administrator |
| Department | IT |
| Usage location | United States |

3. Selecciona **Review + invite** → **Invite**
4. Actualiza y confirma que el usuario invitado fue creado

## Tarea 2: Crear grupos y agregar miembros

### Paso 1: Navegar a Groups
1. En Microsoft Entra ID, ve a **Manage** → **Groups**
2. Explora las opciones disponibles:
   - **Expiration:** Configura tiempo de vida del grupo
   - **Naming policy:** Establece reglas de nomenclatura

### Paso 2: Crear nuevo grupo
1. Selecciona **+ New group**
2. Configura los valores:

| Campo | Valor |
|-------|-------|
| Group type | Security |
| Group name | IT Lab Administrators |
| Group description | Administrators that manage the IT lab |
| Membership type | Assigned |

### Paso 3: Asignar propietarios
1. Selecciona **No owners selected**
2. Busca y selecciona tu cuenta como propietario
3. Confirma la selección

### Paso 4: Agregar miembros
1. Selecciona **No members selected**
2. Busca y selecciona:
   - **az104-user1** (usuario creado)
   - El **guest user** (usuario invitado)
3. Agrega ambos usuarios al grupo

### Paso 5: Finalizar creación
1. Selecciona **Create** para desplegar el grupo
2. Actualiza la página para confirmar
3. Selecciona el grupo creado
4. Revisa la información de **Members** y **Owners**

## Conceptos Clave Aprendidos

### Tipos de Usuarios
- **Usuarios Internos:** Cuentas creadas directamente en el tenant
- **Usuarios Externos/Guest:** Usuarios invitados de otras organizaciones

### Tipos de Grupos
- **Security Groups:** Para control de acceso a recursos
- **Microsoft 365 Groups:** Para colaboración y productividad

### Tipos de Membresía
- **Assigned (Estática):** Los administradores agregan/quitan miembros manualmente
- **Dynamic (Dinámica):** Membresía se actualiza automáticamente basada en propiedades del usuario (requiere licencia Premium)

## Preguntas de Reflexión
1. **¿Cómo planea tu organización crear y gestionar cuentas de usuario?**
2. **¿Tu organización tiene un plan para crear grupos y agregar miembros?**
3. **¿Qué ventajas tendría usar membresía dinámica vs. asignada?**

## Recursos Adicionales
- **Microsoft Learn:** Módulos sobre Microsoft Entra ID
- **Azure PowerShell/CLI:** Para automatización de tareas
- **Copilot:** Para asistencia con comandos y mejores prácticas

## Notas Importantes
- Un **tenant** representa tu organización en Microsoft Entra ID
- Las licencias Premium P1/P2 habilitan características avanzadas como grupos dinámicos
- La ubicación de uso es importante para cumplimiento y características regionales