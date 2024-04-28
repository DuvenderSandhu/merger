# Merger

Merger is a tool designed to merge PDF files with identical names from different folders.

---

## Input Data

1. **Folder Data:** This is the folder containing files with identical names.
2. **Prefixes (optional):** If desired, users can specify prefixes to be included in the merged filename.

### Example

Consider merging the files from the following folders:

**File Structure:**

- **Cover Folder**
  - BHIC131.pdf
  - BHIC132.pdf
  - BHIC133.pdf

- **Assignments Folder**
  - BHIC131.pdf
  - BHIC132.pdf
  - BHIC133.pdf

**Note:** Filenames must match exactly for files to be merged.

---

## Input Format

In the first input, provide the folders (e.g., Cover, Assignments).
In the Prefixes field, users can add a prefix if necessary (e.g., "2002000810-BAG-").

---

## Output

The merged files will be organized with the specified prefix followed by the common filename, preserving the sequence of the folders provided in the first argument.

### Example Output

- 2002000810-BAG-BHIC131.pdf
- 2002000810-BAG-BHIC132.pdf
- 2002000810-BAG-BHIC133.pdf

---

This README provides clear instructions for utilizing the Merger tool, ensuring smooth operation and understanding for users.
