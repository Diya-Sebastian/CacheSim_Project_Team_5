# LRU Cache Simulation – Flowchart

```mermaid
flowchart TD
    A([Start]) --> B[Read Cache Size]
    B --> C[Read Reference String]
    C --> D[Initialize LRU Cache (Empty List)]
    D --> E{More Blocks?}

    E -->|Yes| F[Read Next Block]
    F --> G{Block in Cache?}

    %% HIT case
    G -->|Yes| H[HIT]
    H --> I[Remove Block from Cache]
    I --> J[Append Block to Cache (Most Recently Used)]
    J --> K[Display Cache State]

    %% MISS case
    G -->|No| L[MISS]
    L --> M{Cache Full?}
    M -->|Yes| N[Evict LRU Block (Remove First Element)]
    N --> O[Append New Block to Cache]
    M -->|No| O
    O --> K

    %% Loop
    K --> E
    E -->|No| P([End])
