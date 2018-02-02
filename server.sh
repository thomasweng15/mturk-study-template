trap "trap - SIGTERM && kill -- -$$" SIGINT SIGTERM EXIT

WATCH_DIRS=( \
    ~/c/mturk-study-template/output
)

python -m SimpleHTTPServer 8000 &
server_pid=$!

inotifywait -m ${WATCH_DIRS[@]} -e close_write |
    while read path action file; do
        if [[ "$file" =~ "survey.html" ]]; then
            echo "$file modified, restarting server..."
            kill -9 $server_pid

            python -m SimpleHTTPServer 8000 &
            server_pid=$!
            echo "Server restarted."
        fi
    done

