import os
import json

def leer_template_archivo(file_path):
    with open(file_path, 'r') as f:
        markdown_text = f.read()
        lines = markdown_text.split('\n')
        schema = {}

        for line in lines:
            if line.startswith('#'):
                label = line.strip().lstrip('#').strip()
                schema[label] = {
                    'type': 'object',
                    'properties': {},
                    'required': [],
                    'additionalProperties': {}
                }

        return schema

def generar_esquema(schema, labels):
    esquema_final = {}

    for label in labels:
        if label in schema:
            esquema_final[label] = {
                'type': schema[label]['type'],
                'properties': {},
                'required': [],
                'additionalProperties': {}
            }

            for section in schema[label].get('sections', []):
                propietario = section['proprietario']
                tipo = section.get('tipo', 'string')
                esquema_final[label][f'{propietario}'] = {
                    'type': tipo,
                    'description': '',
                    'format': ''
                }

            for etiqueta in schema[label].get('labels', []):
                propietario = etiqueta['proprietario']
                tipo = etiqueta.get('tipo', 'string')
                esquema_final[label][f'{propietario}'] = {
                    'type': tipo,
                    'description': '',
                    'format': ''
                }

    return esquema_final

def generar_json(schema):
    json_schema = {
        '$schema': 'http://json-schema.org/draft-07/schema#',
        'title': schema.get('title', ''),
        'description': schema.get('description', ''),
        'type': 'object',
        'properties': {},
        'required': [],
        'additionalProperties': {}
    }

    for label, properties in schema.items():
        json_schema['properties'][label] = {
            'type': properties['type'],
            'properties': {},
            'required': [],
            'additionalProperties': {}
        }

        for propietario, propiedades in properties.get('properties', {}).items():
            json_schema['properties'][f'{label}.{propietario}'] = {
                'type': propiedades['type'],
                'description': '',
                'format': ''
            }

    return json.dumps(json_schema, indent=4)

def main():
    file_path = 'templates/template.md'
    schema = leer_template_archivo(file_path)
    labels = ['label1', 'label2']

    esquema_final = generar_esquema(schema, labels)
    json_schema = generar_json(esquema_final)

    with open('schema-master-0.0.0.json', 'w') as f:
        f.write(json_schema)

if __name__ == '__main__':
    main()
