while ($true) {
    $status = git status --porcelain
    if ($status) {
        git add .
        git commit -m "Auto-sync"
        git push origin master
    }
    Start-Sleep -Seconds 60
}
