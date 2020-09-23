import sys 
import json

result = {
    'Name': sys.argv[1],
    'From': sys.argv[2]
  }

#print(type(result))
json = json.dumps(result)

print(str(json))
sys.stdout.flush()