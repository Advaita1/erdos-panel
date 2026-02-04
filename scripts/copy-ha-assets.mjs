import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const root = path.resolve(__dirname, "..");

const distDir = path.join(root, "frontend", "dist");
const destDir = path.join(root, "custom_components", "erdos_panel", "frontend");

await fs.mkdir(destDir, { recursive: true });

const files = ["panel.js", "panel.css"];
for (const file of files) {
  const src = path.join(distDir, file);
  try {
    await fs.copyFile(src, path.join(destDir, file));
    process.stdout.write(`Copied ${file}\n`);
  } catch (error) {
    if (file === "panel.css") continue;
    throw error;
  }
}

