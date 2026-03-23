#!/bin/zsh
set -euo pipefail

if [[ $# -lt 2 ]]; then
  echo "Usage: render_svg_preview.sh <input.svg> <output.png> [size]" >&2
  exit 1
fi

svg_path="$1"
output_path="$2"
size="${3:-1600}"

mkdir -p "$(dirname "$output_path")"

if ! command -v node >/dev/null 2>&1; then
  echo "Node.js is required for SVG preview rendering with sharp." >&2
  exit 1
fi

sharp_module_path="${SHARP_MODULE_PATH:-}"
if [[ -z "$sharp_module_path" ]]; then
  search_dir="$PWD"
  while [[ "$search_dir" != "/" ]]; do
    for candidate in \
      "$search_dir/deeppresenter/html2pptx/node_modules/sharp" \
      "$search_dir/node_modules/sharp"
    do
      if [[ -d "$candidate" ]]; then
        sharp_module_path="$candidate"
        break 2
      fi
    done
    search_dir="$(dirname "$search_dir")"
  done
fi

if [[ -z "$sharp_module_path" ]]; then
  for candidate in \
    "$PWD/deeppresenter/html2pptx/node_modules/sharp" \
    "$PWD/node_modules/sharp"
  do
    if [[ -d "$candidate" ]]; then
      sharp_module_path="$candidate"
      break
    fi
  done
fi

if [[ -z "$sharp_module_path" ]]; then
  echo "Cannot find sharp. Set SHARP_MODULE_PATH or install sharp in the workspace." >&2
  exit 1
fi

SVG_PATH="$svg_path" OUTPUT_PATH="$output_path" PREVIEW_WIDTH="$size" SHARP_MODULE_PATH="$sharp_module_path" node - <<'JS'
const sharp = require(process.env.SHARP_MODULE_PATH);

async function main() {
  const input = process.env.SVG_PATH;
  const output = process.env.OUTPUT_PATH;
  const width = Number(process.env.PREVIEW_WIDTH || "1600");

  await sharp(input, { density: 144 })
    .resize({ width, withoutEnlargement: false })
    .png()
    .toFile(output);

  console.log(output);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
JS
