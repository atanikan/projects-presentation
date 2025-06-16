import subprocess

mermaid_code = '''
graph TD
    A["User Portal"] -->|"Query (location, metric, time)"| B["GeoServer"]
    B -->|"Bounding Box"| C["Inference Gateway / FastAPI"]
    C -->|"Check Cache"| D["Postgres/Redis DB"]
    D -- "Cached" --> C
    C -- "Not Cached" --> K["Kubeflow Pipelines"]
    K -->|"Trigger Compute"| E["Globus Compute Job"]
    E -->|"Distributed I/O & Compute"| F["Polaris Compute"]
    F -->|"Results"| C
    C -->|"Cache Results"| D
    C -->|"Summary/Download"| A
'''

with open('climate_workflow.mmd', 'w') as f:
    f.write(mermaid_code)

# Use the full path to mmdc
subprocess.run([
    '/Users/adityatanikanti/.nvm/versions/node/v20.11.1/bin/mmdc',
    '-i', 'climate_workflow.mmd',
    '-o', 'assets/climate_workflow.svg',
    '-t', 'dark',
    '--backgroundColor', '#181818'
], check=True)

print('SVG diagram saved to assets/climate_workflow.svg') 