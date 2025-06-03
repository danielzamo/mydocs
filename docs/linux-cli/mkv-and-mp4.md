---
title: "Convertir formato mkv a mp4"
---

!!! warning "Nota del autor"
    
    - En este artículo se da por supuesto cumplido que se esta utilizando un sistema operativo basado en un derivado de Debian 12 o superior (ejemplo: Ubuntu, Linux Tuxedo, Linux Mint, etc).
    - En caso de poseer un Linux basado en derivados de RHEL (Ejemplo: Fedora, AlmaLinux, Oracle Linux, Rocky Linux, etc) o Arch Linux u otra distribuciones, el lector debe verificar su gestor de paquetes (`dnf`, `pkg`, etc) 

## Instalar ffmpeg (si no esta)

```bash
sudo apt update && sudo apt install ffmpeg -y
```

## Conversión básica de MKV a MP4

El comando más sencillo es:

```bash
ffmpeg -i mi.mkv -c:v copy -c:a copy mi.mp4
```

:heart: Donde:

- `-i mi.mkv` → Especifica el archivo de entrada.
- `-c:v copy` → Copia el flujo de vídeo sin reencodear (rápido y sin pérdida).
- `-c:a copy` → Copia el flujo de audio sin reencodear.
- `mi.mp4` → Nombre del archivo de salida.

## Si necesitas reencodear (por compatibilidad)

Si el códec de vídeo/audio no es compatible con MP4, puedes reencodear:

```bash
ffmpeg -i mi.mkv -c:v libx264 -crf 23 -c:a aac -b:a 192k mi.mp4
```

Donde: 

- `-c:v libx264` → Codifica el vídeo con H.264 (compatible con MP4).
- `-crf 23` → Calidad (18-28: menor número = mejor calidad).
- `-c:a aac` → Codifica el audio en AAC.
- `-b:a 192k` → Bitrate de audio (ajustable).

## Ver información del archivo (opcional)

Para ver los códecs y formatos de mi.mkv, usa:

```bash
ffmpeg -i mi.mkv
```

## Notas importantes

- Si el MKV ya tiene códecs compatibles con MP4 (H.264/AAC), la opción -c copy es la más rápida.
- Si el archivo tiene subtítulos, añade -c:s copy para copiarlos (o -sn para omitirlos).

