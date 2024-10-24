const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const templatesDir = path.join(__dirname, 'templates');
const outputDir = path.join(__dirname, 'schemas');

if (!fs.existsSync(outputDir)) {
  fs.mkdirSync(outputDir);
}

fs.readdirSync(templatesDir).forEach(file => {
  if (file.endsWith('.template')) {
    const filename = path.basename(file, '.template');
    const templatePath = path.join(templatesDir, file);
    const outputPath = path.join(outputDir, `${filename}-schema.json`);

    console.log(`Generando esquema de ${filename}`);
    execSync(`jsonschema generate --template "${templatePath}" -o "${outputPath}"`);
  }
});
