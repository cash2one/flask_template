#!/bin/sh
# エラーなら停止
set -eu

echo "conoha2 deploy start"
/Users/ikeda/.virtualenvs/py35/bin/py.test /Users/ikeda/punk/matome/matome/tests/tests_deploy.py
ssh -l root conoha2 "date"
ssh -l root conoha2 "cd /var/flask/matome/matome && git pull origin master"
ssh -l root conoha2 "cd /var/flask/matome/matome && /root/.virtualenvs/matome/bin/python manage.py -c ./config/production.py ins"
ssh -l root conoha2 "/usr/bin/supervisorctl -c /etc/supervisord.conf restart gunicorn"
echo "~~~~~~~~~~~~"
echo "deploy finish"
echo "~~~~~~~~~~~~"
echo ""
echo ""
echo "~~~~~~~~~~~~"
echo "HTTP STATUS CHECK"
echo "~~~~~~~~~~~~"
ab -n 300 -c 10 http://www.niku.tokyo/fallout4/
/Users/ikeda/.virtualenvs/py35/bin/py.test /Users/ikeda/punk/matome/matome/tests/tests_deploy.py
curl -LI http://www.niku.tokyo/fallout4/ -o /dev/null -w '%{http_code}\n' -s
curl -LI http://www.niku.tokyo/fallout4pc/ -o /dev/null -w '%{http_code}\n' -s
curl -LI http://www.niku.tokyo/phantom/ -o /dev/null -w '%{http_code}\n' -s
curl -LI http://www.niku.tokyo/fallout4/ -o /dev/null -w '%{http_code}\n' -s
curl -LI http://www.niku.tokyo/fallout4/ -o /dev/null -w '%{http_code}\n' -s
echo "~~~~~~~~~~~~"
echo "conoha2 deploy finish"
echo "~~~~~~~~~~~~"
