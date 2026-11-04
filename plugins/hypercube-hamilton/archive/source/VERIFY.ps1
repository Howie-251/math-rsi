$ErrorActionPreference = 'Stop'
$packageRoot = $PSScriptRoot
$pythonExe = Join-Path $packageRoot 'runtime\python\python.exe'
if (-not (Test-Path -LiteralPath $pythonExe)) { throw 'Bundled runtime missing; see runtime/ACQUISITION.json' }
& $pythonExe (Join-Path $packageRoot 'verify_package.py')
if ($LASTEXITCODE -ne 0) { throw 'Validation failed; inspect verification_runs' }
