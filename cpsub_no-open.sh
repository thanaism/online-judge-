file_path=$1
file_name=$(basename ${file_path})
dir_name=$(dirname ${file_path})
extension=${file_name##*.}
echo $extension
problem_name=${file_name%.*}
test_dir=${dir_name}/test/${problem_name//-/_}
base_url=${problem_name%_*}

# read -p "処理を進めてよろしいですか？  (y/n) :" YN
# if [ "${YN}" = "n" ]; then
#   exit 1;
# fi

# GNU time
export PATH="/usr/local/opt/gnu-time/libexec/gnubin:$PATH"

# activate venv python
source .venv/bin/activate

# make test directory
full_url=https://atcoder.jp/contests/${base_url}/tasks/${problem_name//-/_}

if [ $extension = "py" ]; then
    if [ $2 = "pypy3" ]; then
        oj submit --guess-python-version 3 --guess-python-interpreter pypy --no-open $full_url $1 -y
    else
        oj submit --guess-python-version 3 --guess-python-interpreter cpython --no-open $full_url $1 -y
    fi
else
    oj submit --no-open $full_url $1 -y
fi

