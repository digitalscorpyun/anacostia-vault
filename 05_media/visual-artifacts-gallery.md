---
title: Visual Artifacts Gallery
type: index
tags:
  - visual_mythos
  - visual_artifacts
  - gallery
---

# 🎨 Visual Artifacts Gallery
type: visual_artifact
```dataview
table file.link as "Artifact", file.cday as "Created"
from ""
where type = "visual_artifact"
sort file.name asc
```

---

### How it works

- **Dataview plugin** reads all your notes.  
- **`where type = "visual_artifact"`** filters to only those notes.  
- **`table file.link, file.cday`** shows a link and creation date—you can replace `file.cday` with any other field (e.g. your custom `image` frontmatter) or add more columns.  
- **`from ""`** searches your entire vault; constrain it (e.g. `from "Attachments"` or `from "06_templates"`) if you want.

Once you save that note, you’ll have an always‑up‑to‑date gallery of all your Afrofuturist avatars, masks, and other Sacred‑Tech visuals.
```