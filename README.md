# Farandulítica (sitio público)

Sitio estático. `index.html` lee las notas desde `data/notas.json`, `data/resumenes.json` y `data/meta.json`.
La redacción automática actualiza esos tres archivos dos veces al día; no hace falta tocar nada a mano.

- No edites `data/` a mano: se sobrescribe en cada ronda.
- `scripts/exportar.py` convierte la base de la redacción en estos JSON (solo lo publicado).
