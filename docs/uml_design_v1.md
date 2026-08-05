# UML Design — V1: Color Palette Explorer
**Project:** AI Personal Styling Assistant  
**Version:** 1.0  
**Author:** Jennaya Horne  
**Date:** 2026-08-05  

---

## Overview

This document captures the structural and behavioral design of the V1 Color Palette Explorer using UML diagrams. It translates the SRS requirements into concrete modules, classes, and functions ready for implementation.

---

## 1. Module Architecture (Package Diagram)

```
src/
└── v1_color_explorer/
    ├── main.py              ← Entry point; orchestrates the full workflow
    ├── image_loader.py      ← FR-01, FR-02, FR-03 — Load & validate image input
    ├── region_selector.py   ← FR-04 — Let user select a region of interest (ROI)
    ├── color_extractor.py   ← FR-05 — Extract dominant colors from ROI
    ├── palette_display.py   ← FR-06 — Render visual color palette
    └── color_theory.py      ← FR-07, FR-08 — Identify and describe color relationships
```

Each module maps directly to one or more functional requirements from the SRS.

---

## 2. Class Diagram

```mermaid
classDiagram
    class Main {
        +run() None
    }

    class ImageLoader {
        -SUPPORTED_FORMATS: list~str~
        +load(file_path: str) ndarray
        -_validate_path(file_path: str) bool
        -_validate_format(file_path: str) bool
    }

    class RegionSelector {
        -image: ndarray
        +select_region() tuple~int,int,int,int~
        -_display_image(image: ndarray) None
        -_get_mouse_roi(image: ndarray) tuple
    }

    class ColorExtractor {
        -n_colors: int
        +extract(image_region: ndarray) list~Color~
        -_run_kmeans(pixels: ndarray) ndarray
        -_to_hex(rgb: ndarray) str
    }

    class Color {
        +hex: str
        +rgb: tuple~int,int,int~
        +hsl: tuple~float,float,float~
        +percentage: float
        +to_dict() dict
    }

    class PaletteDisplay {
        +show(colors: list~Color~, relationship: ColorRelationship) None
        -_draw_swatches(ax, colors: list~Color~) None
        -_draw_label(ax, relationship: ColorRelationship) None
    }

    class ColorTheory {
        +analyze(colors: list~Color~) ColorRelationship
        -_hue_distance(h1: float, h2: float) float
        -_is_complementary(colors: list~Color~) bool
        -_is_analogous(colors: list~Color~) bool
        -_is_monochromatic(colors: list~Color~) bool
        -_is_triadic(colors: list~Color~) bool
    }

    class ColorRelationship {
        +label: str
        +description: str
    }

    Main --> ImageLoader : uses
    Main --> RegionSelector : uses
    Main --> ColorExtractor : uses
    Main --> PaletteDisplay : uses
    Main --> ColorTheory : uses
    RegionSelector --> ImageLoader : receives image from
    ColorExtractor --> Color : creates
    ColorTheory --> Color : analyzes
    ColorTheory --> ColorRelationship : returns
    PaletteDisplay --> Color : renders
    PaletteDisplay --> ColorRelationship : renders
```

---

## 3. Sequence Diagram — Happy Path

```mermaid
sequenceDiagram
    actor User
    participant Main
    participant ImageLoader
    participant RegionSelector
    participant ColorExtractor
    participant ColorTheory
    participant PaletteDisplay

    User->>Main: python main.py
    Main->>User: Prompt for image file path
    User->>Main: /path/to/outfit.jpg

    Main->>ImageLoader: load(file_path)
    ImageLoader->>ImageLoader: _validate_path()
    ImageLoader->>ImageLoader: _validate_format()
    ImageLoader-->>Main: image (ndarray)

    Main->>RegionSelector: select_region(image)
    RegionSelector->>User: Display image window
    User->>RegionSelector: Draw rectangle (mouse drag)
    RegionSelector-->>Main: roi coordinates (x, y, w, h)

    Main->>ColorExtractor: extract(image[roi])
    ColorExtractor->>ColorExtractor: _run_kmeans(pixels)
    ColorExtractor-->>Main: list[Color]

    Main->>ColorTheory: analyze(colors)
    ColorTheory-->>Main: ColorRelationship

    Main->>PaletteDisplay: show(colors, relationship)
    PaletteDisplay->>User: Display palette + label
```

---

## 4. Error Flow Diagram

```mermaid
flowchart TD
    A([User runs main.py]) --> B[Prompt for file path]
    B --> C{Path valid?}
    C -- No --> D[Print error: File not found\nPrompt again]
    D --> B
    C -- Yes --> E{Format supported?\nJPG / PNG / BMP}
    E -- No --> F[Print error: Unsupported format\nExit cleanly]
    E -- Yes --> G[Load image]
    G --> H[Display image for ROI selection]
    H --> I{User selects region?}
    I -- Cancelled --> J[Print: No region selected\nExit cleanly]
    I -- Yes --> K[Extract dominant colors]
    K --> L[Analyze color relationships]
    L --> M[Display palette + description]
    M --> N([Done])
```

---

## 5. Module Responsibilities Summary

| Module | Key Responsibility | SRS Req |
|--------|-------------------|---------|
| `main.py` | Orchestrates all modules; entry point | — |
| `image_loader.py` | Accept file path, validate, load image | FR-01, FR-02, FR-03, NFR-05 |
| `region_selector.py` | Display image, let user draw ROI | FR-04 |
| `color_extractor.py` | Run K-Means on ROI pixels, return Color objects | FR-05 |
| `color_theory.py` | Classify palette (complementary, analogous, etc.) | FR-07, FR-08 |
| `palette_display.py` | Render visual palette with labels | FR-06 |

---

## 6. Key Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Color extraction algorithm | K-Means clustering (`sklearn` or manual `numpy`) | Industry-standard approach for dominant color extraction |
| ROI selection method | OpenCV `selectROI()` | Built-in, mouse-driven, works terminal-first |
| Color representation | Store as `hex`, `rgb`, and `hsl` | HSL needed for color theory math; hex/rgb for display |
| Color count (K) | Default `k=5` dominant colors | Balances detail and readability for outfit palettes |
| Color theory math | Hue-angle distance on HSL wheel | Standard colorimetry approach |

---

## 7. Open Questions

> [!IMPORTANT]
> These decisions will shape implementation and should be confirmed before coding.

1. **ROI Selection Method**: Should the user draw the region with a mouse (using `cv2.selectROI`), or would you prefer to also support text input of pixel coordinates as a fallback?
2. **K (number of dominant colors)**: Should the number of extracted colors be fixed at 5, user-configurable via a flag, or automatically determined?
3. **Color Theory Scope**: The SRS mentions complementary, monochromatic, and analogous. Should we also handle **triadic** and **split-complementary** in V1, or defer to V2?
4. **Palette Output Format**: Should the palette window stay open until the user closes it, or auto-close after a timeout?
