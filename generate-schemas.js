const fs = require('fs');
const path = require('path');
const { execFile } = require('child_process');

const templateRoot = path.join(__dirname, './templates');
const outputRoot = path.join(__dirname, './schemas');

if (!fs.existsSync(outputRoot)) {
  fs.mkdirSync(outputRoot);
}

fs.readdir(templateRoot).forEach((file) => {
  if (file.endsWith('.md')) {
    const filename = file;
    const templatePath = path.join(templateRoot, file);
    const outputPath = path.join(outputRoot, `${filename}-schema-masterv0.0.0.json`);

    console.log(`Generando esquema de ${filename}`);
    execFile('jsonschema', ['generate', '--template', templatePath, '-o', outputPath], (error) => {
      if (error) {
        console.error(error);
        return;
      }
      console.log(`Esquema generado con éxito en ${outputPath}`);
    });
  }
});
