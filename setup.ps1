$subjects = @('Biology', 'Chemistry', 'Physics', 'Combined-Maths')
$categories = @('Assignments', 'Past-Papers', 'Elaborations')

foreach ($s in $subjects) {
    foreach ($c in $categories) {
        $path = "subjects\$s\$c"
        New-Item -ItemType Directory -Force -Path $path
        Set-Content -Path "$path\README.md" -Value "# $c"
    }
}

git add .
git commit -m "Add subcategories"
git push origin master
