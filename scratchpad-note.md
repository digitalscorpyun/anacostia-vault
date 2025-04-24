```dataview  
table file.name as "Note", tags  
from ""  
where contains(tags, "vault_index")  
sort file.name asc  
```
