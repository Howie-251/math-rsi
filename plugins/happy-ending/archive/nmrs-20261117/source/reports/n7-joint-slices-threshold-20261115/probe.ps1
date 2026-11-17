$ErrorActionPreference='Stop'
$fields=@{}
$raw=[IO.File]::ReadAllText('D:/科研/服务器/SSH连接信息.txt')
foreach($m in [regex]::Matches($raw,'^([^:：\r\n]+)[:：](.*)$','Multiline')){$fields[$m.Groups[1].Value.Trim()]=$m.Groups[2].Value.Trim()}
$oldAsk=$env:SSH_ASKPASS; $oldReq=$env:SSH_ASKPASS_REQUIRE; $oldDis=$env:DISPLAY
try {
 $env:SSH_ASKPASS='D:/科研/math agent/erdos-szekeres-sat-main/.math-rsi/transport/askpass.cmd'
 $env:SSH_ASKPASS_REQUIRE='force'; $env:DISPLAY='codex:0'
 $pi=[Diagnostics.ProcessStartInfo]::new()
 $pi.FileName='C:/Windows/System32/OpenSSH/ssh.exe'
 $pi.UseShellExecute=$false; $pi.CreateNoWindow=$true
 $pi.RedirectStandardInput=$true; $pi.RedirectStandardOutput=$true; $pi.RedirectStandardError=$true
 foreach($arg in @('-p','22','-o','StrictHostKeyChecking=yes','-o','UserKnownHostsFile=D:/科研/math agent/erdos-szekeres-sat-main/.math-rsi/transport/known_hosts','-o','ConnectTimeout=8','-o','ConnectionAttempts=1','-o','NumberOfPasswordPrompts=1','-o','PubkeyAuthentication=no','-o','PreferredAuthentications=password',($fields['用户名']+'@10.60.133.166'))){$pi.ArgumentList.Add($arg)}
 $pi.ArgumentList.Add('uname -s; test -d /data/ktqiu_hdd/math_agent && echo PROJECT_ROOT_PRESENT')
 $process=[Diagnostics.Process]::new(); $process.StartInfo=$pi
 [void]$process.Start(); $process.StandardInput.Close()
 $out=$process.StandardOutput.ReadToEndAsync(); $err=$process.StandardError.ReadToEndAsync()
 $timedOut=-not $process.WaitForExit(18000)
 if($timedOut){$process.Kill($true);$process.WaitForExit()}
 $receipt=[ordered]@{mode='read_only_internal_probe';endpoint='10.60.133.166:22';strict_host_key_checking=$true;trust_modified=$false;timeout=$timedOut;exit_code=$process.ExitCode;stdout=$out.GetAwaiter().GetResult();stderr=$err.GetAwaiter().GetResult();scientific_execution_requested=$false}
 [IO.File]::WriteAllText((Join-Path $PSScriptRoot 'probe-receipt.json'),($receipt|ConvertTo-Json -Depth 5))
 $receipt|ConvertTo-Json -Depth 5
}finally{$env:SSH_ASKPASS=$oldAsk;$env:SSH_ASKPASS_REQUIRE=$oldReq;$env:DISPLAY=$oldDis}
