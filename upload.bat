git config --local user.name "PosetMage"
git config --local user.email "PosetMage@users.noreply.github.com"
git remote set-url origin git@POM:PosetMage/PosetMage.github.io.git

git pull
git add .
git commit -m "upload"
git push
