#!/usr/bin/env python3
"""Convierte los documentos exportados de la base del artefacto (out_dir de ArtifactData)
en los archivos públicos notas.json, resumenes.json, meta.json y anuncios.json (en la raíz del sitio).
Uso: python3 exportar.py <carpeta_out_dir> <carpeta_sitio>
Solo exporta lo publicado. Nunca exporta candidatos, eventos ni secretos."""
import json, glob, os, sys
src, dst = sys.argv[1], sys.argv[2]
os.makedirs(dst, exist_ok=True)
def load(col):
    out = []
    for f in glob.glob(os.path.join(src, col, "*.json")):
        d = json.load(open(f, encoding="utf-8"))
        if d.get("estado", "publicada") != "publicada":
            continue
        for k in ("ig", "imagen_prompt", "caption", "origen", "instagram", "ig_aprobado"):
            d.pop(k, None)
        d["id"] = os.path.basename(f)[:-5]
        out.append(d)
    out.sort(key=lambda x: x.get("publicado", ""), reverse=True)
    return out
notas, res = load("notas"), load("resumenes")
for name, data in (("notas", notas), ("resumenes", res[:60])):
    json.dump(data, open(os.path.join(dst, name + ".json"), "w", encoding="utf-8"), ensure_ascii=False)
json.dump([], open(os.path.join(dst, "anuncios.json"), "w"))
meta_f = os.path.join(src, "meta", "estado.json")
meta = json.load(open(meta_f, encoding="utf-8")) if os.path.exists(meta_f) else {}
json.dump({"ultima_ronda": meta.get("ultima_ronda", "")}, open(os.path.join(dst, "meta.json"), "w", encoding="utf-8"))
print(f"notas={len(notas)} resumenes={len(res[:60])}")
