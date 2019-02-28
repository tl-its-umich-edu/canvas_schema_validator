import json, urllib.request

file = open("reserved_words.txt", "r")
reserved_words = []
permitted_datatypes = []

# Populate reserved words and permitted datatypes
for line in open("reserved_words.txt", "r"):
    line = line.rstrip()
    if not line.startswith("#"):
        reserved_words.append(line.upper())

for line in open("data_types.txt"):
    line = line.rstrip()
    if not line.startswith("#"):
        permitted_datatypes.append(line.upper())

schema_file = "https://portal.inshosteddata.com/api/schema/latest"

with urllib.request.urlopen(schema_file) as url:
    json = json.loads(url.read().decode())

reserved_found = []
datatype_found = []
column_name_len = []

print (f"Schema version version {json.get('version')}")
print ("Scanning for schema errors in reserved words and datatypes")
for schema_key, schema_value in json.get('schema').items():
#    print (f"Checking {schema_key}")
    for column in schema_value.get("columns"):
        name = column.get("name").upper()
        datatype = column.get("type").upper()
        if name in reserved_words:
            reserved_found.append(f"{name} in {schema_key} is reserved!")
        if len(name) > 63:
            column_name_len.append("f{name} in {schema_key is too long {len(name)}")
        if datatype not in permitted_datatypes:
            datatype_found.append(f"{datatype} in {name} in {schema_key} is not permitted!")


if reserved_found:
    print (reserved_found)
else:
    print ("No problems with reserved words")
if datatype_found:
    print (datatype_found)
else:
    print ("No problems with reserved data types")
if column_name_len:
    print (column_name_len)
else:
    print ("No problems with column name length")
