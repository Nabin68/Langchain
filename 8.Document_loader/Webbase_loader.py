from langchain_community.document_loaders import WebBaseLoader

url="https://www.flipkart.com/apple-macbook-air-m2-16-gb-256-gb-ssd-macos-sequoia-mc7w4hn-a/p/itm2ea42dec44bca?pid=COMH64PYZU4ZZR79&lid=LSTCOMH64PYZU4ZZR79AHLYXY&marketplace=FLIPKART&cmpid=content_computer_22927808323_g_8965229628_gmc_pla&tgi=sem,1,G,11214002,g,search,,770553264708,,,,c,,,,,,,&entryMethod=22927808323&&cmpid=content_22927808323_gmc_pla&gad_source=1&gad_campaignid=22927808323&gbraid=0AAAAADxRY58tQcMMZsGyQ_CuPvvoYaHRT&gclid=CjwKCAiAuIDJBhBoEiwAxhgyFnZe4mqI6Yihwjrrz41faW5N2hhZ83A1Z42wq0WgSDVU-qLSCa8gTxoCuM0QAvD_BwE"

loader=WebBaseLoader(url)

docs=loader.load()

print(len(docs))
print(docs)