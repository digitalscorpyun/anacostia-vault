#!/bin/bash

echo "📁 Moving files to ScorpyunStyle target paths..."

declare -A files=(
  ["adinkra_encryption_protocols.md"]="sacred_tech/adinkra_encryption_protocols.md"
  ["africana_studies_black_music_cultural_resistance.md"]="africana_studies/black_music_cultural_resistance.md"
  ["africana-studies-civil-rights-movement.md"]="africana_studies/civil_rights_movement.md"
  ["africana-studies-harlem-renaissance.md"]="africana_studies/harlem_renaissance.md"
  ["africana-studies-overview.md"]="africana_studies/overview.md"
  ["ai_fairness_trenches.md"]="ai_ethics/ai_fairness_trenches.md"
  ["ai-ml-neural-networks.md"]="ai_ethics/neural_networks.md"
  ["ai-ml-overview.md"]="ai_ethics/overview.md"
  ["algebra-linear-equations-and-inequalities.md"]="mathematics/algebra/linear_equations_and_inequalities.md"
  ["algebra-overview.md"]="mathematics/algebra/overview.md"
  ["avm_ops_status.md"]="obsidian_fortress/avm_ops_status.md"
  ["biblical_theme_miner.md"]="sacred_texts/biblical_theme_miner.md"
  ["book_summaries.md"]="reading_systems/book_summaries.md"
  ["career_development_networking_strategies.md"]="personal_development/career_development_networking_strategies.md"
  ["dataview_query_black_identity_web.md"]="obsidian_fortress/dataview_queries/black_identity_web.md"
  ["dataview_table_of_nzinga_doctrine.md"]="obsidian_fortress/dataview_queries/table_of_nzinga_doctrine.md"
  ["debug_log.md"]="obsidian_fortress/_logs/debug_log.md"
)

for src in "${!files[@]}"; do
  dest="${files[$src]}"
  dest_dir=$(dirname "$dest")
  
  mkdir -p "$dest_dir"
  
  if [[ -f "$src" ]]; then
    mv "$src" "$dest"
    echo "✅ Moved: $src → $dest"
  else
    echo "⚠️ File not found: $src"
  fi
done

echo "🏁 All move operations attempted. Review above for any missing files."
