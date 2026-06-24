# Paraguay - Plan de Cuentas DNIT

Plan de cuentas e impuestos para Odoo 19 basado en el **Modelo de Estados
Financieros** de la DNIT (Dirección Nacional de Ingresos Tributarios).

## Características

- **Plan de cuentas**: 30 grupos jerárquicos y 81 cuentas, con la estructura y
  los códigos del formulario oficial (Balance General y Estado de Resultado).
- **Impuestos**: IVA 10%, IVA 5% y exento, para ventas y compras, con sus
  cuentas de débito y crédito fiscal.
- **Posiciones fiscales**: nueve clasificaciones de compra y venta según la SET.
- **Valores por defecto**: cuentas de cliente, impuestos y diferencia de cambio
  configuradas a nivel de compañía.

## Alcance

El módulo solo depende de `account`. El plan se registra con el código de
plantilla `py_dnit`, distinto del `py` de la OCA, de modo que ambas
localizaciones pueden coexistir en la misma base.
