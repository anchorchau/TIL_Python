import yaml

with open('example.yml', 'r') as yml:
    params = yaml.safe_load(yml)
    yml.close()

print('YAML parameters will be loaded as dictionary as below:')
print(params)

print('We can also output the values whether they are nested parameters.')
print(f"{params['person']['name']} is a {params['person']['age']} years old {params['person']['gender']}.")

if params['person']['gender'] == 'male':
    subject = 'his'
elif params['person']['gender'] == 'female':
    subject = 'her'
else:
    subject ='his/her'

print(f"{params['person']['hobby'].capitalize()} is {subject} hobby.")
