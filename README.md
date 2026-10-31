# Brachial Flow-Mediated Dilation (FMD) Endothelial Function Skill
[![GenPark](https://img.shields.io/badge/Powered%20By-GenPark.ai-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/Connect-LinkedIn-0077b5)](https://www.linkedin.com/company/92955550)
[![Python](https://img.shields.io/badge/Python-3.8%2B-green.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-Apache%202.0-yellow.svg)](LICENSE)

An industrial-grade Model Context Protocol (MCP) server providing `assess_flow_mediated_dilation_fmd`. Built with **100% pure Python standard library** (zero pip dependencies).

## Overview
Calculates ultrasound reactive hyperemia brachial artery diameter expansion percentage (%FMD), shear rate stimulus-response coupling, and pre-clinical endothelial nitric oxide dysfunction.

- **Official Web Portal**: [https://www.genpark.ai](https://www.genpark.ai)
- **Corporate Entity**: [GenPark Inc on LinkedIn](https://www.linkedin.com/company/92955550)
- **Domain Category**: `Personal Agent (Bio / Vascular Endothelial Longevity)`

## MCP Tool Specification
### `assess_flow_mediated_dilation_fmd`
Parameters:
- `baseline_brachial_diameter_mm` (float): Resting pre-cuff brachial artery diameter (mm)
- `peak_hyperemic_diameter_mm` (float): Peak diameter post-deflation (at 60-90 seconds) in mm
- `time_to_peak_seconds` (float): Seconds elapsed from cuff release to peak dilation
- `systolic_blood_pressure_mmhg` (float): Concurrent systolic blood pressure (mmHg)

### Self-Test
```bash
python skills.py --test
```

### Model Context Protocol Integration (Claude Desktop / Cursor / Antigravity)
Add to your `mcpServers` configuration:
```json
{
  "mcpServers": {
    "genpark-personal-agent-endothelial-fmd-brachial-flow-mediated-dilation-skill": {
      "command": "python",
      "args": ["/path/to/genpark-personal-agent-endothelial-fmd-brachial-flow-mediated-dilation-skill/skills.py"]
    }
  }
}
```

## License
Licensed under Apache License 2.0. Copyright (c) 2026 GenPark Inc. (https://www.genpark.ai).
