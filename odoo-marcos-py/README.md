# Localización Paraguay para Odoo 19

Localización contable y fiscal de Paraguay para Odoo 19, basada en la
documentación de la **DNIT** (Dirección Nacional de Ingresos Tributarios) y la
**SET**. Desarrollada por Marcos Vallejos.

## Módulos

| Módulo | Qué hace |
|---|---|
| **l10n_py_dnit** | Plan de cuentas (Modelo de Estados Financieros DNIT), IVA 10/5/exento y posiciones fiscales. |
| **l10n_py_dnit_base** | RUC con dígito verificador (módulo 11) y tipos de identificación (RUC, CI, Pasaporte, Carnet de Residencia). |
| **l10n_py_dnit_account** | Tipos de documento de la SET, timbrado y numeración fiscal de facturas (establecimiento-punto-número). |
| **l10n_py_dnit_edi** | Estructura base para SIFEN / e-Kuatiá (*scaffold*, ver abajo). |

Cada módulo es instalable por separado; las dependencias se resuelven solas.

## Características destacadas

- **RUC + DV** validado con el algoritmo oficial (módulo 11, base 11),
  verificado contra constancias reales.
- **Timbrado** como rango de numeración por tipo de documento, establecimiento
  y punto de expedición, con control de vigencia.
- **Numeración fiscal** correlativa, asignada al validar la factura con bloqueo
  de fila (sin huecos ni duplicados) e inmutable una vez emitida.
- **Tipos de documento**: Factura, Autofactura, Nota de Crédito, Nota de Débito
  y Nota de Remisión.

## SIFEN

`l10n_py_dnit_edi` provee el punto de extensión (estado del documento, CDC) pero
**no** incluye la firma digital, los esquemas XSD ni el envío a la DNIT: eso
depende del certificado del contribuyente y de una librería de firma. Queda
preparado para que un conector lo complete.

## Instalación

Agregar el repositorio al `addons_path`, actualizar la lista de aplicaciones e
instalar los módulos que se necesiten. Para una empresa paraguaya nueva,
seleccionar el plan **Paraguay - Plan de Cuentas DNIT** en la configuración
contable.

## Licencia

LGPL-3.
