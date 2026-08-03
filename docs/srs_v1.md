# Software Requirements Specification
## Version 1 — Color Palette Explorer

**Project:** AI Personal Styling Assistant  
**Version:** 1.0  
**Author:** Jennaya Horne  
**Date:** 2026-08-03  
**Status:** Draft  

---

## 1. Purpose

Version 1 of the AI Personal Styling Assistant is a terminal-based Python application that allows a user to upload an outfit image, manually select clothing regions, and analyze the dominant colors present in those regions. The application will display a visual color palette and identify basic color relationships to help the user better understand the color composition of their outfit.

---

## 2. Scope

### 2.1 In Scope

The following features are included in Version 1:

- Accepting an image file provided by the user
- Displaying the uploaded image
- Allowing the user to manually select a region of the image (a clothing item)
- Extracting the dominant colors from the selected region
- Displaying a color palette visualizing those dominant colors
- Identifying and describing basic color relationships (e.g., complementary, monochromatic, analogous)

### 2.2 Out of Scope

The following features are explicitly **not** included in Version 1 and will be addressed in later versions:

- Automatic detection or identification of clothing articles (Version 2)
- A graphical user interface (GUI) window (future version)
- Saving or exporting analysis results to a file (future version)
- Database storage of any kind (Version 3)
- User accounts or profiles (Version 5)
- Outfit recommendations (Version 4)
- Weather or occasion-based suggestions (Version 4+)

---

## 3. Functional Requirements

The following requirements describe what the system **must do**.

| ID | Requirement |
|----|-------------|
| FR-01 | The system shall accept an image file path as input from the user via the terminal |
| FR-02 | The system shall support JPG, PNG, and BMP image formats |
| FR-03 | The system shall display the uploaded image to the user |
| FR-04 | The system shall allow the user to manually select a rectangular region of interest within the image |
| FR-05 | The system shall extract the dominant colors from the selected region using color analysis |
| FR-06 | The system shall display a visual color palette representing the dominant colors found |
| FR-07 | The system shall identify and label the basic color relationship of the extracted palette (e.g., monochromatic, complementary, analogous) |
| FR-08 | The system shall display a plain-language description of the identified color relationship |

---

## 4. Non-Functional Requirements

The following requirements describe **how** the system must perform.

| ID | Requirement |
|----|-------------|
| NFR-01 | The application shall run on any macOS machine with Python 3.11+ installed |
| NFR-02 | The application shall complete color extraction and display results within 5 seconds of user selection |
| NFR-03 | The codebase shall follow a modular structure with clearly separated responsibilities |
| NFR-04 | All functions shall include docstrings describing their purpose, parameters, and return values |
| NFR-05 | The application shall handle invalid file paths and unsupported formats gracefully with clear error messages |
| NFR-06 | The application shall not modify or overwrite the original uploaded image |

---

## 5. Constraints

| Constraint | Detail |
|------------|--------|
| Language | Python 3.11.5 |
| Libraries | OpenCV, NumPy, Pillow, Matplotlib |
| Platform | macOS (Apple Silicon and Intel compatible) |
| Interface | Terminal / command-line only |
| No internet required | All processing happens locally |

---

## 6. Assumptions

The following assumptions are made about the environment and user:

- The user has Python 3.11+ installed and the virtual environment activated before running the application
- The user provides a valid image file path when prompted
- The image contains at least one visible clothing item
- The user understands how to navigate a terminal

---

## 7. Acceptance Criteria

Version 1 is considered complete when all of the following are true:

- [ ] A user can run the script from the terminal with a valid image path
- [ ] The image is displayed on screen
- [ ] The user can select a region of the image using their mouse or by entering coordinates
- [ ] A color palette is displayed showing the dominant colors of the selected region
- [ ] The palette is accompanied by a label and plain-language description of the color relationship
- [ ] An invalid image path produces a clear, readable error message rather than a crash
- [ ] All source files include docstrings
- [ ] At least one unit test exists per module

---

## 8. Version History

| Version | Date | Author | Notes |
|---------|------|--------|-------|
| 0.1 | 2026-08-03 | Jennaya Horne | Initial draft |
