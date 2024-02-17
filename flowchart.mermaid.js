```mermaid
flowchart LR
    RG[(Repositorio\nGithub)]
    BB((BuildBot))
    CD((Codee))
    FE[Frontend]
    P[/Parser/]
    AF[/Autofixes/]

    RG --> BB --> CD --> FE --> AF
    CD --> P
    CD --> AF --> P --> RG
```