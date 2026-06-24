# Paraguay · Plan de Cuentas DNIT

Plan de cuentas para Odoo 19 basado en el **Modelo de Estados Financieros**
publicado por la DNIT (Dirección Nacional de Ingresos Tributarios). La
estructura y los códigos siguen el formulario oficial de Balance General y
Estado de Resultados.

## Qué incluye

- **27 grupos** jerárquicos (Activo, Pasivo, Patrimonio Neto, Resultados).
- **81 cuentas** con su `account_type` mapeado al estándar contable de Odoo.
- **IVA 10% y 5%** (venta y compra) más exento, con sus cuentas de débito y
  crédito fiscal.
- Cuentas por defecto de la compañía: cliente, impuestos y diferencia de cambio.

Los códigos respetan el formato del formulario DNIT:

```
1-              ACTIVO
1-01-           ACTIVO CORRIENTE
1-01-01-        DISPONIBILIDADES
1-01-01-01      CAJA
```

## Instalación

1. Copiar el módulo a una ruta del `addons_path`.
2. Actualizar la lista de aplicaciones e instalar **Paraguay - Plan de Cuentas DNIT**.
3. En una compañía paraguaya sin plan asignado, ir a *Contabilidad → Configuración*
   y seleccionar el plan **Paraguay - Plan de Cuentas DNIT**.

> Convive con otros planes paraguayos: este módulo registra el código de plantilla
> `py_dnit`, distinto del `py` de la OCA. El plan se elige manualmente.

## Estructura

```
l10n_py_dnit/
├── __manifest__.py
├── models/
│   └── template_py_dnit.py        # metadatos + cuentas por defecto
└── data/template/                 # cargados automáticamente por el framework
    ├── account.group-py_dnit.csv
    ├── account.account-py_dnit.csv
    ├── account.tax.group-py_dnit.csv
    └── account.tax-py_dnit.csv
```

## Fuente

DNIT — *Plantilla Modelo de Estados Financieros* (RG 110/13 y modificatorias).

## Licencia

LGPL-3.
