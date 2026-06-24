# 🇵🇾 Odoo 19 - Adaptación y Localización Paraguay (DNIT)

Este repositorio contiene un entorno completo de desarrollo de **Odoo 19 Community** adaptado y optimizado para las normativas vigentes de Paraguay. El proyecto toma como base estructural el repositorio original de Marcos Vallejos (`l10n-paraguay`), aplicando reingeniería de software y correcciones de arquitectura para garantizar su total compatibilidad con el motor moderno de Odoo 19 y el sistema asíncrono de la interfaz web.

---

## 🚀 Hitos de Ingeniería y Correcciones Aplicadas

A lo largo del proceso de desarrollo, se han auditado y resuelto los siguientes cuellos de botella críticos:

### 1. Compatibilidad de Compilación en Odoo 19
* **Problema:** Errores de sintaxis y colapsos del ORM en el arranque debido a declaraciones obsoletas de `_sql_constraints` en los módulos heredados.
* **Solución:** Ajuste y refactorización completa de la herencia del framework, logrando una instalación limpia y una base de datos operativa (`py_v19`).

### 2. Homologación del Dígito Verificador (DV) con la DNIT
* **Problema:** El algoritmo nativo de cálculo matemático no contemplaba caracteres alfanúmericos ni procesaba correctamente las constancias impositivas modernas.
* **Solución:** Se reescribió la lógica del archivo `ruc.py` traduciendo de manera directa la función oficial PL/SQL provista por la **DNIT**, añadiendo soporte seguro para la conversión de caracteres ASCII y el aislamiento estricto de la raíz numérica.

### 3. Resolución del Bucle Asíncrono de Recálculo (Mutación del RUC)
* **Problema:** Al formatear e inyectar guiones (`-`) directamente en el campo estándar `vat` (Tax ID) desde el backend, el JavaScript del navegador web de Odoo 19 entraba en un bucle recursivo asíncrono que concatenaba los dígitos anteriores de forma infinita (ej: `5004943` ➡️ `500494371-0`).
* **Solución:** Se eliminó la manipulación del string visual en el core. Ahora el campo `vat` almacena la raíz limpia y el dígito verificador se calcula de forma pasiva a través del campo `l10n_py_ruc_dv` con persistencia física en PostgreSQL (`store=True`), estabilizando la interfaz gráfica.

### 4. Bypass del Validador Internacional Corporativo (`_check_vat`)
* **Problema:** El módulo global de Odoo (`l10n_latam_base`) interceptaba el botón "Guardar" arrojando un error de validación e impidiendo registrar clientes locales.
* **Solución:** Se realizó un *override* limpio del método `@api.constrains` adaptando la firma con argumentos variables (`*args, **kwargs`) para neutralizar errores RPC. El sistema ahora otorga inmunidad a los registros paraguayos frente al validador genérico de Odoo, aplicando de forma exclusiva la validación matemática local.

---

## 📂 Estructura del Proyecto

* **`odoo-server/`**: Core oficial de Odoo 19 Community.
* **`odoo-marcos-py/`**: Módulos de localización paraguaya (Base y Contabilidad) con las correcciones de arquitectura inyectadas de forma modular.
* **`.gitignore`**: Archivo de seguridad que blinda el entorno virtual (`venv`), cachés de Python y los parámetros privados de conexión del archivo `odoo.conf`.

---

## 🛠️ Créditos y Reconocimientos
* **Base del Proyecto:** Agradecimiento especial a **Marcos Vallejos** (`vallejosmarcos.py@gmail.com`) por proveer la estructura inicial de la localización.
* **Evolución y Mantenimiento:** Modificado, corregido y optimizado de forma independiente para extender el soporte hacia implementaciones reales bajo las exigencias de la DNIT en Paraguay.
