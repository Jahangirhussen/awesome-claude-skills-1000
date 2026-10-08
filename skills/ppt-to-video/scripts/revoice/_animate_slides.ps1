param(
  [Parameter(Mandatory=$true)][string]$PptxPath,
  [Parameter(Mandatory=$true)][string]$DurationsJson,
  [Parameter(Mandatory=$true)][string]$OutDir,
  [double]$EffectDuration = 0.5,
  [double]$Stagger = 0.25,
  [int]$Width = 1920,
  [int]$Fps = 30
)
# PowerPoint 자체 렌더러로 슬라이드에 요소별 순차 페이드인을 입혀 슬라이드마다 개별 mp4로
# 내보낸다. HTML로 재현하지 않고 원본 폰트·사진·레이아웃 그대로 유지하면서 모션만 더하는 것이
# 목적 — 1차 제작 시도가 실패한 지점(HTML 재현으로 브랜드 룩이 어긋남)을 다시 밟지 않기 위함.
#
# 슬라이드를 하나씩만 보이게(Hidden 토글) 하고 CreateVideo를 호출하면 숨긴 슬라이드는 출력에서
# 완전히 빠진다(실측 확인됨) — 슬라이드마다 파일을 복사·재오픈할 필요 없이 한 세션에서 처리한다.

$ErrorActionPreference = 'Stop'
New-Item -ItemType Directory -Force $OutDir | Out-Null
$durations = Get-Content $DurationsJson -Raw | ConvertFrom-Json

$app = New-Object -ComObject PowerPoint.Application
$pres = $app.Presentations.Open($PptxPath, $false, $false, $false)

foreach ($prop in $durations.PSObject.Properties) {
  $slideNo = [int]$prop.Name
  $slide = $pres.Slides.Item($slideNo)
  $seq = $slide.TimeLine.MainSequence
  $n = $slide.Shapes.Count

  # 값이 숫자 하나면 예전 방식(균등 예산), 객체({duration,checkpoints})면 나레이션
  # 문장이 실제로 발화되는 시점에 맞춘 구간별 등장 — 아래에서 분기.
  $val = $prop.Value
  $isObj = $val.PSObject.Properties.Name -contains 'duration'
  $duration = if ($isObj) { [double]$val.duration } else { [double]$val }
  $checkpoints = if ($isObj -and $val.checkpoints) { @($val.checkpoints | ForEach-Object { [double]$_ }) } else { $null }

  if ($checkpoints -and $checkpoints.Count -gt 0) {
    # 나레이션 문장 수만큼 구간을 나누고, 화면 요소를 문서 순서 그대로 그 구간에 배분한다.
    # 각 구간의 요소들은 그 구간이 끝나는 시각(=그 문장이 다 말해지는 시각)까지 순차
    # 페이드인을 마치도록 간격을 역산 — "전부 처음 2초에 등장, 나머지는 정적"이던
    # 문제를 없애고 화면이 나레이션을 따라 계속 살아있게 만든다.
    $ngroups = [Math]::Min($checkpoints.Count, [Math]::Max(1, $n))
    $base = [Math]::Floor($n / $ngroups)
    $rem = $n % $ngroups
    $idx = 1
    $prevCp = 0.0
    for ($g = 0; $g -lt $ngroups; $g++) {
      $groupSize = $base + $(if ($g -ge ($ngroups - $rem)) { 1 } else { 0})
      if ($groupSize -lt 1) { continue }
      $target = $checkpoints[$g]
      $window = [Math]::Max(0.15, $target - $prevCp)
      $gap = if ($groupSize -gt 1) { [Math]::Max(0.06, [Math]::Min(1.2, $window / ($groupSize - 1))) }
             else { [Math]::Min(0.7, $window) }
      $effDur = $gap * 0.6
      $effDelay = $gap * 0.4
      for ($k = 0; $k -lt $groupSize; $k++) {
        if ($idx -gt $n) { break }
        $sh = $slide.Shapes.Item($idx)
        $eff = $seq.AddEffect($sh, 10, 0, 3)
        $eff.Timing.Duration = $effDur
        $eff.Timing.TriggerDelayTime = $effDelay
        $idx += 1
      }
      $prevCp = $target
    }
  } else {
    # 표 형태 슬라이드는 요소가 20개를 넘기도 해, 고정 스태거를 쓰면 전체 등장에 수십 초가
    # 걸린다(28개 x 0.75s ≈ 21초). 체크포인트가 없을 때의 대체 — 예산 안에서 균등 배분.
    $budget = [Math]::Min(2.2, 0.5 * $duration)
    $gap = if ($n -gt 1) { [Math]::Max(0.06, [Math]::Min(($EffectDuration + $Stagger), $budget / ($n - 1))) }
           else { $EffectDuration + $Stagger }
    $effDur = $gap * 0.6
    $effDelay = $gap * 0.4
    for ($i = 1; $i -le $n; $i++) {
      $sh = $slide.Shapes.Item($i)
      # msoAnimEffectFade=10, msoAnimTriggerAfterPrevious=3 — 앞 요소가 끝나야 다음이
      # 시작하는 진짜 순차 등장. (2=msoAnimTriggerWithPrevious는 전부 동시에 뜨는 것이라
      # 오작동이었음.) 튀는 모션(바운스·줌)은 클리셰 블랙리스트 취지에 안 맞아 단순
      # 페이드만 쓴다.
      $eff = $seq.AddEffect($sh, 10, 0, 3)
      $eff.Timing.Duration = $effDur
      $eff.Timing.TriggerDelayTime = $effDelay
    }
  }

  $slide.SlideShowTransition.AdvanceOnTime = 1
  $slide.SlideShowTransition.AdvanceTime = $duration
}

foreach ($i in 1..$pres.Slides.Count) { $pres.Slides.Item($i).SlideShowTransition.Hidden = 1 }

foreach ($prop in $durations.PSObject.Properties) {
  $slideNo = [int]$prop.Name
  $pres.Slides.Item($slideNo).SlideShowTransition.Hidden = 0
  $out = Join-Path $OutDir ("slide_{0:d2}.mp4" -f $slideNo)

  # CreateVideo가 산발적으로 실패한다(같은 슬라이드가 재실행하면 성공하는 경우도 관찰됨) —
  # 최대 2회 재시도한다. 기존에 잘 만들어진 $out은 새 렌더가 실제로 성공한 뒤에만
  # 덮어쓴다 — 먼저 지워버리면 재시도까지 실패했을 때 좋은 이전 버전마저 잃는다.
  # 시도마다 임시 파일명을 다르게 써서, 이전 시도의 파일이 아직 잠겨 있어도(안티바이러스
  # 스캔 등) 삭제하려다 스크립트 전체가 죽는 일이 없게 한다 — 삭제 실패는 청소 실패일
  # 뿐 치명적 오류가 아니므로 try/catch로 흡수한다.
  $status = 0
  $tmp = $null
  for ($attempt = 1; $attempt -le 2; $attempt++) {
    $tmp = "$out.attempt$attempt.tmp.mp4"
    try { if (Test-Path $tmp) { Remove-Item $tmp -Force -ErrorAction Stop } } catch { }
    $pres.CreateVideo($tmp, $true, 2, $Width, $Fps, 85)
    $deadline = (Get-Date).AddSeconds(120)
    do {
      Start-Sleep -Milliseconds 500
      $status = $pres.CreateVideoStatus
    } while ($status -eq 1 -and (Get-Date) -lt $deadline)
    if ($status -eq 3) { break }
    Write-Output "RETRY $slideNo attempt=$attempt status=$status"
  }

  if ($status -ne 3) {
    try { if (Test-Path $tmp) { Remove-Item $tmp -Force -ErrorAction Stop } } catch { }
    Write-Output "FAILED $slideNo status=$status"
  } else {
    Move-Item -Force $tmp $out
    Write-Output "RENDERED $slideNo $out"
  }
  $pres.Slides.Item($slideNo).SlideShowTransition.Hidden = 1
}

$pres.Close()
$app.Quit()
