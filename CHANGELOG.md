# Historial de Cambios (Changelog) - Odoo 19 Paraguay

   Todos los cambios notables en este proyecto serán documentados en este archivo. El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/).

   ## [1.0.0] - 2026-06-24

   ### Añadido
   - Repositorio principal unificado en GitHub para control de código de todo el espacio de trabajo.
   - Archivo `.gitignore` de seguridad para blindar credenciales locales (`odoo.conf`) y entornos virtuales (`venv`).

   ### Corregido
   - **Compatibilidad Odoo 19:** Refactorización de declaraciones de herencia y restricciones SQL para permitir la instalación de la localización paraguaya de forma limpia.
   - **Algoritmo del DV:** Reescritura del cálculo matemático en `ruc.py` homologado con las funciones ASCII oficiales de la DNIT.
   - **Bucle de Recálculo:** Migración del campo `l10n_py_ruc_dv` a almacenamiento físico (`store=True`) en PostgreSQL, solucionando la mutación y duplicación asíncrona del RUC en la interfaz web.
   - **Bypass de Validación:** Override modular del método de restricciones de Odoo corporativo (`_check_vat`) para otorgar inmunidad a los RUC locales y evitar bloqueos RPC al guardar registros nuevos.
