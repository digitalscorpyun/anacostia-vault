# Apply root categorization moves safely
# Moves a list of files from the vault root into category folders.
# Behavior:
# - If destination file exists, it will be moved to a .bak_TIMESTAMP
# - If source doesn't exist, a SKIPPED row is written to master log
# - Produces master_move_log_YYYYMMDD_HHmmss.csv in vault root

Set-StrictMode -Version Latest
$vaultRoot = (Get-Location).Path
$timestamp = Get-Date -Format 'yyyyMMdd_HHmmss'
$masterLog = Join-Path $vaultRoot ("master_move_log_{0}.csv" -f $timestamp)
"Source,Destination,Action,Timestamp,Note" | Out-File -FilePath $masterLog -Encoding utf8

# Helper: safe join that respects vault root
function Join-Root([string]$rel) {
    return Join-Path $vaultRoot $rel
}

# list of mappings: SourceName -> DestinationDir (relative to vault root)
$mappings = @(
    # Technology
    @{src='first_custom_rig_build.md'; dst='technology'},
    @{src='foundations_programming_terms.md'; dst='technology'},
    @{src='how_to_build_an_agent_digitalscorpyun_style.md'; dst='technology'},
    @{src='introduction_to_computers.md'; dst='technology'},
    @{src='lion_news_scraper.md'; dst='technology'},
    @{src='python_function_style_template.md'; dst='technology'},
    @{src='python_programming_fundamentals_glossary_ch_2.md'; dst='technology'},
    @{src='python-chapter4-exercises.md'; dst='technology'},
    @{src='qwen_echo_primer.md'; dst='technology'},
    @{src='refactor_script_manifest.md'; dst='technology'},

    # Africana Studies
    @{src='free_black_communities_underground_railroad.md'; dst='africana_studies'},
    @{src='freedmen_land_claims or a black_land_justice_scroll.md'; dst='africana_studies'},
    @{src='kindred.md'; dst='africana_studies'},
    @{src='matamba_economic_power_ai_era.md'; dst='africana_studies'},
    @{src='nzinga_and_the_logic_of_distributed_power_in_ai_ethics.md'; dst='africana_studies'},
    @{src='nzinga_diplomacy_ai_ethics.md'; dst='africana_studies'},
    @{src='nzinga_reign_achievements.md'; dst='africana_studies'},
    @{src='ritual_displacement_africa.md'; dst='africana_studies'},
    @{src='the_black_jacobins.md'; dst='africana_studies'},
    @{src='the_black_president.md'; dst='africana_studies'},

    # Policy Analysis
    @{src='georgia_2020_blueprint.md'; dst='policy_analysis'},
    @{src='governance_index.md'; dst='policy_analysis'},
    @{src='medicaid_expansion_battles.md'; dst='policy_analysis'},
    @{src='musk_omb_policies.md'; dst='policy_analysis'},
    @{src='on_tyranny_key_lessons.md'; dst='policy_analysis'},
    @{src='palestine_discussion.md'; dst='policy_analysis'},
    @{src='political_ai.md'; dst='policy_analysis'},
    @{src='politics_anticipatory_obedience.md'; dst='policy_analysis'},
    @{src='prop_50_la_micro_map_overlay_90018.md'; dst='policy_analysis'},
    @{src='rural_hospital_collapse.md'; dst='policy_analysis'},
    @{src='trump_second_term_chaos.md'; dst='policy_analysis'},

    # Systems
    @{src='goal_tracker_dashboard.md'; dst='systems'},
    @{src='grandmaster_protocol.md'; dst='systems'},
    @{src='learning_journal_index.md'; dst='systems'},
    @{src='legitimation_loop.md'; dst='systems'},
    @{src='manus_session_log.md'; dst='systems'},
    @{src='od_comply_personality_profile.md'; dst='systems'},
    @{src='orchestration_quote_flow.md'; dst='systems'},
    @{src='reading_log_schema.md'; dst='systems'},
    @{src='rebellion_code_changelog.md'; dst='systems'},
    @{src='rebellion_greeting.ps1.md'; dst='systems'},
    @{src='scorpyun_manifesto.md'; dst='systems'},
    @{src='system_audit_index.md'; dst='systems'},
    @{src='system_software_update_manifest.md'; dst='systems'},
    @{src='task_dashboard.md'; dst='systems'},
    @{src='the_lion_of_anacostia_bias_detection.md'; dst='systems'},
    @{src='value_systems.md'; dst='systems'},
    @{src='vault_etymology_index.md'; dst='systems'},
    @{src='vault_proxy_grok.md'; dst='systems'},

    # Learning
    @{src='epistolary_form.md'; dst='learning'},
    @{src='ethics_case_studies.md'; dst='learning'},
    @{src='hitler_and_the_nazis_evil_on_trial_ep_1_origin_of_evil.md'; dst='learning'},
    @{src='lord_of_the_rings_the_fellowship_of_the_ring.md'; dst='learning'},
    @{src='structure-note-soft-skills-for-it.md'; dst='learning'},

    # People
    @{src='resume_healthcare.md'; dst='people'},

    # Inbox
    @{src='note_three.md'; dst='_inbox'},
    @{src='online_articles.md'; dst='_inbox'},
    @{src='README.md'; dst='_inbox'}
)

$moveCount = 0
$skipped = 0
foreach ($m in $mappings) {
    $srcRel = $m.src
    $dstDirRel = $m.dst
    $srcPath = Join-Root $srcRel
    $dstDir = Join-Root $dstDirRel
    if (-not (Test-Path -LiteralPath $dstDir)) {
        New-Item -Path $dstDir -ItemType Directory -Force | Out-Null
    }
    $dstPath = Join-Path $dstDir (Split-Path $srcRel -Leaf)
    $now = Get-Date -Format 'o'
    if (-not (Test-Path -LiteralPath $srcPath)) {
        $row = "`"$srcPath`",`"$dstPath`",SKIPPED,$now,`"Source not found`""
        Add-Content -Path $masterLog -Value $row
        Write-Host "SKIPPED: $srcRel (not found)"
        $skipped++
        continue
    }
    # if destination exists, back it up
    if (Test-Path -LiteralPath $dstPath) {
        $bak = "$dstPath.bak_$timestamp"
        Write-Host "Backing up existing destination: $dstPath -> $bak"
        Move-Item -LiteralPath $dstPath -Destination $bak -Force
        $note = "Existing destination backed up to $bak"
    } else { $note = '' }
    # move source
    try {
        Move-Item -LiteralPath $srcPath -Destination $dstPath -Force
        $moveCount++
        $row = "`"$srcPath`",`"$dstPath`",MOVED,$now,`"$note`""
        Add-Content -Path $masterLog -Value $row
        Write-Host "MOVED: $srcRel -> $dstDirRel"
    } catch {
        $err = $_.Exception.Message -replace '"','""'
        $row = "`"$srcPath`",`"$dstPath`",ERROR,$now,`"$err`""
        Add-Content -Path $masterLog -Value $row
        Write-Host "ERROR moving $srcRel : $err"
    }
}
Write-Host "Done. Moved $moveCount files. Skipped $skipped files. Master log: $masterLog"
exit 0
