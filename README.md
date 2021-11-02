# Center for Equitable Policy in a Changing World
## Policy Spread: Comparing COVID-19 mask mandates to climate change, immigration, and other policy adoption across the US

### Data source
[Centers for Disease Control](https://data.cdc.gov/Policy-Surveillance/U-S-State-and-Territorial-Public-Mask-Mandates-Fro/62d6-pm5i), US State & Territorial mask mandates April 10, 2020-August 15, 2021

### Principal researchers
Richard W. Sharp\
Patrick W. Zimmerman

#### Codebase
Webpage: HTML & CSS\
Visualization: d3.v5, with jQuery 3.5.1 to selectively color\
Data prep: Python

#### Python Package requirements (as well as all their dependencies)
pandas

#### Other requirements
Webserver\
Note: This can also be run on a WordPress site either within the WP framework of a post or page (more complicated as you have to point to the script files and WP doesn't really play nice with JSONs. If you're going this route, put the body of the index.html file in the WP doc, load the correct scripts in the header and footer, and delete index.html) or create your own directory (such as ~/apps/wordpress/htdocs/policy-spread/) and dump everything in there (easier, your page will be the contents of the index.html file)