# 🇵🇾 Odoo 19 - Adaptación y Localización Paraguay

   Este repositorio contiene un entorno integrado de desarrollo de **Odoo 19 Community** optimizado para operar con las normativas impositivas de Paraguay. El proyecto toma como base los módulos de Marcos Vallejos (`l10n-paraguay`), aplicando reingeniería de software para garantizar estabilidad en las vistas web modernas y el backend del sistema.

   ---

   ## 🛠️ Características Principales
   * **Cálculo del DV Novedoso:** Ejecución del algoritmo Módulo 11 homologado directamente con las especificaciones de la DNIT.
   * **Persistencia Robusta:** Datos de identificación fiscal limpios de bucles de recálculo en la interfaz gráfica.
   * **Arquitectura Modular:** Bypass seguro de los módulos de restricciones internacionales de Odoo corporativo para el RUC paraguayo.

   ---

   ## 🚀 Estructura del Entorno
   * **`odoo-server/`**: Núcleo oficial de Odoo 19 Community.
   * **`odoo-marcos-py/`**: Módulos de localización paraguaya (Base y Contabilidad) extendidos y optimizados.
   * **`CHANGELOG.md`**: Registro detallado de la evolución técnica, versiones y parches del sistema.

   ---

   ## 📈 Flujo de Trabajo Local
   Para levantar el entorno de desarrollo de Odoo en tu WSL2 de forma habitual: